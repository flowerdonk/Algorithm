import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static boolean[] visited;
    static int result = 0;

    /**
     * BFS
     * @param start     시작 위치(수빈)
     * @param target    타겟 위치(동생)
    */

    public static void bfs(int start, int target) {
        Queue<int[]> queue = new ArrayDeque<>(); // [start, time]
        visited[start] = true;
        queue.offer(new int[]{start, 0});

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int now = curr[0];
            int time = curr[1];

            if (now == target) {
                result = time;
                return;
            }

            int[] dirs = {now + 1, now - 1, now * 2};
            for (int dir : dirs) {
                if (dir >= 0 && dir < 100001 && !visited[dir]) {
                    queue.offer(new int[]{dir, time + 1});
                    visited[dir] = true;
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());

        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        visited = new boolean[100001];

        bfs(N, K);

        System.out.println(result);
    }
}