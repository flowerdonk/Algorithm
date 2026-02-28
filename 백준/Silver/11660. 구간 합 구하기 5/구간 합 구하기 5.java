import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] data;
    static int[][] dataSum;

    /**
     * [누적합]
     * prefixSum
     */
    private static void prefixSum() {

        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                dataSum[i][j] = data[i][j] + dataSum[i - 1][j] + dataSum[i][j - 1] - dataSum[i - 1][j - 1];
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        data = new int[N + 1][N + 1];
        dataSum = new int[N + 1][N + 1];
        for (int i = 1; i < N + 1; i++) {
            token = new StringTokenizer(br.readLine());
            for (int j = 1; j < N + 1; j++) {
                data[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        prefixSum();

        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(token.nextToken());
            int y1 = Integer.parseInt(token.nextToken());
            int x2 = Integer.parseInt(token.nextToken());
            int y2 = Integer.parseInt(token.nextToken());
            System.out.println(dataSum[x2][y2] - dataSum[x2][y1 - 1] - dataSum[x1 - 1][y2] + dataSum[x1 - 1][y1 - 1]);
        }
    }

}