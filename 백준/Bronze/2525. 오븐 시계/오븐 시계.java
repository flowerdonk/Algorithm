import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(br.readLine());
        int time = A * 60 + B + C;

        if (time >= 1440){
            time -= 1440;
        }
        System.out.print(time / 60);
        System.out.print(' ');
        System.out.print(time % 60);

    }
}