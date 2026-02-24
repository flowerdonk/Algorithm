import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static long[] lectures;

    /**
     * [이분 탐색]
     * devide
     */
    private static long devide(long maxLength, long totalLength) {
        long result = 0;
        long low = maxLength;
        long high = totalLength;

        while (low <= high) {
            long mid = (low + high) / 2;
            int count = 0;

            long tempSum = 0;
            for (int i = 0; i < N; i++) {
                if (tempSum + lectures[i] <= mid) {
                    tempSum += lectures[i];
                } else {
                    tempSum = lectures[i];
                    count++;
                }
            }
            if (tempSum != 0) count++;

            if (count <= M) {
                result = mid;
                high = mid - 1;
            } else if (count > M) {
                low = mid + 1;
            } 

        }



        return result;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        lectures = new long[N];
        long totalLength = 0;
        long maxLength = 0;
        token = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            long temp = Integer.parseInt(token.nextToken());
            maxLength = Math.max(maxLength, temp);
            totalLength += temp;
            lectures[i] = temp;
        }

        System.out.println(devide(maxLength, totalLength));
    }

}