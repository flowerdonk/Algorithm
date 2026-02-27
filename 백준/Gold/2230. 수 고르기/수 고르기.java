import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static long[] data;

    /**
     * [투포인터]
     * twoPointer
     */
    private static long twoPointer() {
        long result = Long.MAX_VALUE;
        int left = 0, right = 1;

        while (right < N) {
            long diff = data[right] - data[left];
            if (diff == M) {
                result = diff;
                break;
            } else if (diff > M) {
                left++;
                result = Math.min(result, diff);
            } else right++;
        }

        return result;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        data = new long[N];
        for (int i = 0; i < N; i++) {
            data[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(data);

        System.out.println(twoPointer());;

    }

}