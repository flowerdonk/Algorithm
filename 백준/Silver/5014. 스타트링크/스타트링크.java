import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int F, S, G, U, D;
    static boolean[] visited;

    /**
     * bfs
     */
    private static int bfs() {
        Queue<int[]> queue = new ArrayDeque<>(); // [층, 이동 횟수]
        queue.offer(new int[]{S, 0});
        visited[S] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curFloor = current[0];
            int count = current[1];

            if (curFloor == G) return count;

            int nextUp = curFloor + U;
            if (nextUp <= F && !visited[nextUp]) {
                queue.offer(new int[]{nextUp, count + 1});
                visited[nextUp] = true;
            }

            int nextDown = curFloor - D;
            if (nextDown > 0 && !visited[nextDown]) {
                queue.offer(new int[]{nextDown, count + 1});
                visited[nextDown] = true;
            }
        }
        return -1;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        F = Integer.parseInt(token.nextToken()); // 건물 총 높이
        S = Integer.parseInt(token.nextToken()); // 현재 층
        G = Integer.parseInt(token.nextToken()); // 목표 층
        U = Integer.parseInt(token.nextToken()); // 위로 이동하는 높이
        D = Integer.parseInt(token.nextToken()); // 아래로 이동하는 높이

        visited = new boolean[F + 1];
        int ans = bfs();
        if (ans == -1) {
            System.out.println("use the stairs");
        } else System.out.println(ans);


    }

}