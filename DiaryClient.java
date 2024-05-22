import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpRequest.BodyPublishers;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Map;
import java.util.stream.Collectors;

public class DiaryClient {
    public static void main(String[] args) throws IOException, InterruptedException {
        String url = "http://localhost:5000/upload_diary";
        Map<Object, Object> data = Map.of(
                "name", "Attack Target 1",
                "team", "Red",
                "from_user", "alex",
                "location", "HA NOI",
                "time", "2024-05-20T12:34");
        String imgPath = "./toUpload/map.png";
        Path filePath = Paths.get(imgPath);

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
                .POST(ofMimeMultipartData(data, filePath))
                .build();

        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.statusCode());
        System.out.println(response.body());
    }

    private static HttpRequest.BodyPublisher ofMimeMultipartData(Map<Object, Object> data, Path filePath)
            throws IOException {
        var boundary = "---011000010111000001101001";
        var byteArrays = data.entrySet().stream()
                .map(entry -> {
                    var key = entry.getKey();
                    var value = entry.getValue();
                    return ("--" + boundary + "\r\nContent-Disposition: form-data; name=\"" + key
                            + "\"\r\n\r\n" + value + "\r\n").getBytes();
                })
                .collect(Collectors.toList());

        byteArrays.add(("--" + boundary + "\r\nContent-Disposition: form-data;name=\"media\"; filename=\""
                + filePath.getFileName() + "\"\r\nContent-Type:" + Files.probeContentType(filePath) + "\r\n\r\n")
                .getBytes());
        byteArrays.add(Files.readAllBytes(filePath));
        byteArrays.add(("\r\n--" + boundary + "--\r\n").getBytes());

        return BodyPublishers.ofByteArrays(byteArrays);
    }
}
