import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] minmiles;

    /**
     * 그리디 알고리즘
     * @param
     */


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());

        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        minmiles = new int[N];

        int P, L;
        int[] miles;

        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(br.readLine());
            P = Integer.parseInt(token.nextToken()); // 신청 인원
            L = Integer.parseInt(token.nextToken()); // 수강 인원

            miles = new int[P];
            token = new StringTokenizer(br.readLine());
            for (int j = 0; j < P; j++) {
                miles[j] = Integer.parseInt(token.nextToken());
            }
            Arrays.sort(miles);

            int minMile;
            if (P >= L) {
                minMile = miles[P - L];
            } else {
                minMile = 1;
            }

            minmiles[i] = minMile;
        }

        Arrays.sort(minmiles);
        int result = 0;
        int count = 0;
        for (int i = 0; i < N; i++) {
            if (result + minmiles[i] <= M) {
                result += minmiles[i];
                count++;
            } else {
                break;
            }
        }
        System.out.println(count);

    }
}