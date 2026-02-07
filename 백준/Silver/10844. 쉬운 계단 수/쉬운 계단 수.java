import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N, mod;
    static int[][] stairs;

    /**
     * dp
     * @param
     */
    private static void dp() {

        // 1자리 계단 수
        for (int j = 0; j <= 9; j++) {
            stairs[1][j] = 1;
        }

        // 2~ 자리 계단 수
        for (int i = 2; i <= N; i++) { // i자리 계단 수
            for (int j = 0; j <= 9; j++) { // j로 시작하는 계단 수
                if (j == 0) { // 0으로 시작하는 계단 수
                    stairs[i][j] = stairs[i - 1][1] % mod;
                } else if (j == 9) { // 9으로 시작하는 계단 수
                    stairs[i][j] = stairs[i - 1][8] % mod;
                } else { // 2~8으로 시작하는 계단 수
                    stairs[i][j] = (stairs[i - 1][j - 1] % mod + stairs[i - 1][j + 1]) % mod;
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine()); // 자릿수 N
        stairs = new int[N + 1][10];
        mod = 1000000000;

        dp();
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            sum  = (sum + stairs[N][i]) % mod;
        }
        System.out.println(sum % mod);
    }

}