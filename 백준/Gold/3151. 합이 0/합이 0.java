import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[] data;

    /**
     * [투포인터]
     * twoPointer
     */
    private static long twoPointer() {
        long result = 0;

        if (N < 3) return 0;

        for (int i = 0; i < N - 2; i++) {
            int left = i + 1, right = N - 1;
            while (left < right) {
                int sum = data[i] + data[left] + data[right];

                if (sum == 0) {
                    // 1. left = right
                    if (data[left] == data[right]) {
                        int n = right - left + 1;
                        result += (long) n * (n - 1) / 2;
                        break;
                    }
                    // 2. left != right
                    int leftData = data[left];
                    int rightData = data[right];
                    int leftCount = 0;
                    int rightCount = 0;

                    while (data[left] == leftData) {
                        leftCount++;
                        left++;
                    }
                    while (data[right] == rightData) {
                        rightCount++;
                        right--;
                    }
                    result += (long) leftCount * rightCount;
                }
                else if (sum < 0) left++;
                else right--;
            }
        }

        return result;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer token = new StringTokenizer(br.readLine());
        data = new int[N];
        for (int i = 0; i < N; i++) {
            data[i] = Integer.parseInt(token.nextToken());
        }
        Arrays.sort(data);

        System.out.println(twoPointer());;

    }

}