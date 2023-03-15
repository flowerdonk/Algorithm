import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        int[] new_arr = new int[N];
        for (int i = 1; i <= N; i++){
            arr[i - 1] = i;
            new_arr[i - 1] = i;
        }
        for (int i = 0; i < M; i++){
            StringTokenizer str = new StringTokenizer(br.readLine(), " ");
            int s = Integer.parseInt(str.nextToken());
            int e = Integer.parseInt(str.nextToken());
            int k = Integer.parseInt(str.nextToken());

            System.arraycopy(arr, k - 1, new_arr, s - 1, e - k + 1);
            System.arraycopy(arr, s - 1, new_arr, s + e - k, k - s);
            for (int n = 0; n < N; n++){
                arr[n] = new_arr[n];
            }
        }

        for (int n = 0; n < N; n++){
            System.out.print(arr[n] + " ");
        }
    }
}