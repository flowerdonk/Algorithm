import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] price;
    static int[] dp;

    /**
     * dp
     * @param
     */
    private static int card() {

        for (int i = 1 ; i <= N; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] = Math.max(dp[i], price[j] + dp[i - j]);
            }
        }

        return dp[N];
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); // 카드 수 N

        StringTokenizer token = new StringTokenizer(br.readLine());
        price = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            price[i] = Integer.parseInt(token.nextToken());
        }

        dp = new int[N + 1];
        System.out.println(card());
    }

}