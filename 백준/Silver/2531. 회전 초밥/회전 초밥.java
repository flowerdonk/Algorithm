import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, D, K, C;
    static int[] belts;
    static int[] visited;

    /**
     * [slidingWindow]
     * slidingWindow
     */
    private static int slidingWindow() {
        int count = 0, result = 0;
        visited = new int[D + 1];

        for (int i = 0; i < K; i++) {
            if (visited[belts[i]] == 0) count++;
            visited[belts[i]]++;
        }

        if (visited[C] == 0) result++;
        else result = count;

        for (int i = 0; i < N; i++) {
            int out = belts[i];
            visited[out]--;
            if (visited[out] == 0) count--;

            int in = belts[(i + K) % N];
            if (visited[in] == 0) count++;
            visited[in]++;

            int tempCount = count;
            if (visited[C] == 0) tempCount++;

            result = Math.max(result, tempCount);

            if (result == K + 1) break;
        }

        return result;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        N = Integer.parseInt(token.nextToken()); // 접시 수
        D = Integer.parseInt(token.nextToken()); // 초밥 가짓 수 (1 ~ D)
        K = Integer.parseInt(token.nextToken()); // 연속해서 먹는 접시 수
        C = Integer.parseInt(token.nextToken()); // 쿠폰 번호

        belts = new int[N];
        for (int i = 0; i < N; i++) {
            belts[i] = Integer.parseInt(br.readLine());
        }

        System.out.println(slidingWindow());

    }

}