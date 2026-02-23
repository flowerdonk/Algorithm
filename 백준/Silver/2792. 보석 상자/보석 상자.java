import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static long[] jewel;

    /**
     * [이분 탐색]
     * cut
     */
    private static long devide(long maxAmount) {
        long result = 0;
        long low = 1;
        long high = maxAmount;

        while (low <= high) {
            long mid = (low + high) / 2;
            long count = 0;

            for (int i = 0; i < M; i++) {
                count += (jewel[i] + mid - 1) / mid;
            }


            if (count > N) {
                low = mid + 1;
            } else {
                high = mid - 1;
                result = mid;
            }
        }


        return result;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        jewel = new long[M];
        long maxAmount = 0;
        for (int i = 0; i < M; i++) {
            long temp = Integer.parseInt(br.readLine());
            maxAmount = Math.max(maxAmount, temp);
            jewel[i] = temp;
        }

        System.out.println(devide(maxAmount));
    }

}