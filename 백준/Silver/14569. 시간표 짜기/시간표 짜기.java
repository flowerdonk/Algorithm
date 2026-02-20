import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static ArrayList<Integer>[] lec;
    static boolean[][] students;

    /**
     * [brute force]
     * available
     * @param studentId 학생 번호
     */
    private static int available(int studentId) {
        int count = 0;

        for (int i = 0; i < N; i++) {
            boolean flag = true;
            for (int time : lec[i]) {
                if (!students[studentId][time]) flag = false;
            }
            if (flag) count++;
        }

        return count;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        lec = new ArrayList[N];
        StringTokenizer token;
        for (int i = 0; i < N; i++) {
            lec[i] = new ArrayList<>();
            token = new StringTokenizer(br.readLine());
            int temp = Integer.parseInt(token.nextToken());
            for (int j = 0; j < temp; j++) {
                lec[i].add(Integer.parseInt(token.nextToken()));
            }
        }

        M = Integer.parseInt(br.readLine());
        students = new boolean[M][51];
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(br.readLine());
            int temp = Integer.parseInt(token.nextToken());
            for (int j = 0; j < temp; j++) {
                int time = Integer.parseInt(token.nextToken());
                students[i][time] = true;
            }
        }

        for (int i = 0; i < M; i++) {
            System.out.println(available(i));
        }

    }

}