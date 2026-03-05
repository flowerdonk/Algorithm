import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, H;
    static int[] bottom;
    static int[] top;

    /**
     * [누적합]
     * prefixSum
     */
    private static void prefixSum() {

        for (int i = H - 1; i > 0; i--) {
            top[i] += top[i + 1];
            bottom[i] += bottom[i + 1];
        }

        int minResult = Integer.MAX_VALUE;
        int count = 0;
        for (int h = 1; h < H + 1; h++) {
            int result = top[H - h + 1] + bottom[h];

            if (result < minResult) {
                minResult = result;
                count = 1;
            } else if (result == minResult) {
                count++;
            }
        }

        System.out.print(minResult + " " + count);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        N = Integer.parseInt(token.nextToken());
        H = Integer.parseInt(token.nextToken());

        bottom = new int[H + 1];
        top = new int[H + 1];
        for (int i = 1; i < N + 1; i++) {
            int tempH = Integer.parseInt(br.readLine());
            if (i % 2 == 0) top[tempH] += 1;
            else bottom[tempH] += 1;

        }

        prefixSum();

    }

}