import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] house;
    static int[][][] dp;

    /**
     * dp
     * @param
     */
    private static int pipe() {
        // dp[x][y][n] : (x, y) 좌표의 방향 n
        // 0 = 가로, 1 = 세로, 2 = 대각선
        dp[1][2][0] = 1;
        for (int i = 1; i <= N; i++) {
            for (int j = 2; j <= N; j++) {
                if (i == 1 && j <= 2) continue; // 기저값 스킵
                if (house[i][j] == 1) continue; // 벽일 경우 스킵
                // 가로
                dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2];
                // 세로
                if (i == 1) continue; // 세로, 가로는 첫 줄에서 실행 X
                dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2];
                // 대각선
                if (house[i - 1][j] == 1 || house[i][j - 1] == 1) continue;
                dp[i][j][2] = dp[i - 1][j - 1][2] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][0];
            }
        }

        return (dp[N][N][0] + dp[N][N][1] + dp[N][N][2]);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); // 집 크기 N
        house = new int[N + 1][N + 1];

        StringTokenizer token;
        for (int i = 1; i <= N; i++) {
            token = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                house[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        dp = new int[N + 1][N + 1][3];
        System.out.println(pipe());
    }

}