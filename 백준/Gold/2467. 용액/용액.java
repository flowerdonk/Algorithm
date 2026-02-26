import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static long[] data;

    /**
     * [투포인터]
     * twoPointer
     */
    private static void twoPointer() {
        long minAbsSum = Integer.MAX_VALUE;
        long ansLeft = 0, ansRight = 0;
        int left = 0, right = N - 1; // idx

        while (left < right) {
            long temp = data[left] + data[right];

            if (minAbsSum > Math.abs(temp)) {
                minAbsSum = Math.abs(temp);
                ansLeft = data[left];
                ansRight = data[right];
            }

            if (temp > 0) right--;
            else if (temp < 0) left++;
            else break;
        }

        System.out.print(ansLeft + " " + ansRight);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer token = new StringTokenizer(br.readLine());
        data = new long[N];
        for (int i = 0; i < N; i++) {
            data[i] = Integer.parseInt(token.nextToken());
        }

        twoPointer();

    }

}