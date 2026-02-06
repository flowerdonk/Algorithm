import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static boolean[][] nodes;
    static boolean[] visited;

    /**
     * bfs
     * @param
     */
    private static int bfs() {
        int answer = 0;
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(1);
        visited[1] = true;

        while (!queue.isEmpty()) {
            int temp = queue.poll();
            answer++;

            for (int i = 1; i < N + 1; i++) {
                if (nodes[temp][i] && !visited[i]) {
                    queue.offer(i);
                    visited[i] = true;
                }
            }

        }

        return answer - 1;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine()); // 컴퓨터 수
        M = Integer.parseInt(br.readLine()); // 컴퓨터 쌍 수

        StringTokenizer token;
        nodes = new boolean[N + 1][N + 1];
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(token.nextToken());
            int v = Integer.parseInt(token.nextToken());

            nodes[u][v] = nodes[v][u] = true;
        }

        visited = new boolean[N + 1];

        System.out.println(bfs());
    }

}