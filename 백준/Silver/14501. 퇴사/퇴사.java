import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] schedule;

    /**
     * dp
     * @param
     */
    private static int dp() {
        int[] maxP = new int[N + 1];

        for (int i = 0; i < N; i++) {
            if (i + schedule[i][0] <= N) {
                maxP[i + schedule[i][0]] = Math.max(maxP[i + schedule[i][0]], maxP[i] + schedule[i][1]);
            }
            maxP[i + 1] = Math.max(maxP[i], maxP[i + 1]);
        }

        return maxP[N];
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine()); // 퇴사 날

        schedule = new int[N][2];
        StringTokenizer token;
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(br.readLine());
            schedule[i][0] = Integer.parseInt(token.nextToken());
            schedule[i][1] = Integer.parseInt(token.nextToken());
        }

        System.out.println(dp());
    }

}