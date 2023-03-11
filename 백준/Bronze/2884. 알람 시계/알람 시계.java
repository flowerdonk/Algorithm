import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int time = A * 60 + B - 45;

        if (time < 0){
            time += 1440;
        }

        System.out.print(time / 60);
        System.out.print(' ');
        System.out.print(time % 60);
    }
}