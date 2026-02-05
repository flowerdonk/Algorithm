import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int N;
    static int[] predicts;

    /**
     * 그리디 알고리즘
     * @param
     */


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        predicts = new int[N];
        for (int i = 0; i < N; i++) {
            predicts[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(predicts);

        long result = 0;
        for (int i = 0; i < N; i++) {
            result += Math.abs((i + 1) - predicts[i]);
        }
        System.out.println(result);

    }
}