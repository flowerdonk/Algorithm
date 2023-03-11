import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = A * B;
        for (int i = B % 10; B > 0; B /= 10, i = B % 10){
            System.out.println(A * i);
        }
        System.out.println(C);
    }
}