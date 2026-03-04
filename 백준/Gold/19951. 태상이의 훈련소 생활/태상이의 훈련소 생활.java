import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static int[] data;
    static int[] dataSum;

    /**
     * [누적합]
     * prefixSum
     */
    private static void prefixSum() {

        for (int i = 1; i < N + 2; i++) {
            dataSum[i] += dataSum[i - 1];
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < N + 1; i++) {
            sb.append(data[i] + dataSum[i]).append(" ");
        }

        System.out.println(sb);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        data = new int[N + 2];
        token = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            data[i] = Integer.parseInt(token.nextToken());
        }

        dataSum = new int[N + 2];
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            int k = Integer.parseInt(token.nextToken());
            dataSum[a] += k;
            dataSum[b + 1] -= k;
        }

        prefixSum();

    }

}