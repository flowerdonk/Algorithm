import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static long[][] dp;
    static int[][] board;

    /**
     * dp
     * @param
     */
    private static long jump() {
        dp[0][0] = 1;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 0) break;
                int jump = board[i][j];
                if (j + jump < N) dp[i][j + jump] += dp[i][j];
                if (i + jump < N) dp[i + jump][j] += dp[i][j];
            }
        }
        return dp[N - 1][N - 1];
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer token;
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        dp = new long[N][N];
        System.out.println(jump());
    }

}