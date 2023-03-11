import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()) / 4;

        for(int i = 0; i < N; i++){
            System.out.print("long ");
        }
        System.out.println("int");
    }
}