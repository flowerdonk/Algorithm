import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int C = Integer.parseInt(br.readLine());
        for (int i = 0; i < C; i++){
            StringTokenizer str = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(str.nextToken());
            int[] arr = new int[N];
            float total = 0;
            for (int j = 0; j < N; j++){
                int score = Integer.parseInt(str.nextToken());
                arr[j] = score;
                total += score;
            }
            float aver = total/N;
            float student = 0;
            for (int j = 0; j < N; j++){
                if (arr[j] > aver){
                    student += 1;
                }
            }
            float ans = student/N*100;
            System.out.printf("%.3f%%", ans);
            System.out.println();
        }
    }
}