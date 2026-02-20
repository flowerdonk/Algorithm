import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static long[] lectures;
    static long[] students;

    /**
     * [brute force]
     * available
     */
    private static void available() {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            int count = 0;
            for (int j = 0; j < N; j++) {
                if ((lectures[j] & students[i]) == lectures[j]) count++;
            }
            sb.append(count).append("\n");
        }
        System.out.println(sb);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        lectures = new long[N];
        StringTokenizer token;
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(br.readLine());
            int temp = Integer.parseInt(token.nextToken());
            long mask = 0L;
            for (int j = 0; j < temp; j++) {
                int time = Integer.parseInt(token.nextToken());
                mask |= (1L << time);
            }
            lectures[i] = mask;
        }

        M = Integer.parseInt(br.readLine());
        students = new long[M];
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(br.readLine());
            int temp = Integer.parseInt(token.nextToken());
            long mask = 0L;
            for (int j = 0; j < temp; j++) {
                int time = Integer.parseInt(token.nextToken());
                mask |= (1L << time);
            }

            students[i] = mask;
        }

        available();
    }

}