import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[][] stuffs;

    /**
     * bitMask
     */
    private static int bitMask() {
        int minDiff = Integer.MAX_VALUE;

        for (int i = 1; i < (1 << N); i++) {
            int sour = 1;
            int bitter = 0;
            for (int j = 0; j < N; j++) {
                if ((i & (1 << j)) != 0) {
                    sour *= stuffs[j][0];
                    bitter += stuffs[j][1];
                }
            }
            minDiff = Math.min(minDiff, Math.abs(sour - bitter));
        }
        return minDiff;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        stuffs = new int[N][2];
        StringTokenizer token;
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(br.readLine());
            stuffs[i][0] = Integer.parseInt(token.nextToken()); // 신 맛
            stuffs[i][1] = Integer.parseInt(token.nextToken()); // 쓴 맛
        }

        System.out.println(bitMask());

    }

}