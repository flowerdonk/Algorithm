import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long X = Long.parseLong(br.readLine());
        int N = Integer.parseInt(br.readLine());
        long ans = 0;

        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            long a = Long.parseLong(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            ans += a * b;
        }

        if (X == ans){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}