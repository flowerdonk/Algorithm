import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[] data;
    static long[] dataSum;

    /**
     * [누적합]
     * prefixSum
     */
    private static long prefixSum() {
        long result = 0;

        dataSum[0] = data[0];
        for (int i = 1; i < N; i++) {
            dataSum[i] = dataSum[i - 1] + data[i];
        }

        // case 1. 벌 벌 집
        for (int i = 1; i < N - 1; i++) {
            long temp = (dataSum[N - 1] - data[0] - data[i]) + (dataSum[N - 1] - dataSum[i]);
            result = Math.max(result, temp);
        }

        // case 2. 집 벌 벌
        for (int i = 1; i < N - 1; i++) {
            long temp = (dataSum[i - 1]) + (dataSum[N - 2] - data[i]);
            result = Math.max(result, temp);
        }

        // case 3. 벌 집 벌
        for (int i = 1; i < N - 1; i++) {
            long temp = (dataSum[i] - data[0]) + (dataSum[N - 2] - dataSum[i - 1]);
            result = Math.max(result, temp);
        }

        return result;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        data = new int[N];
        dataSum = new long[N];
        StringTokenizer token = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            data[i] = Integer.parseInt(token.nextToken());
        }

        System.out.println(prefixSum());

    }

}