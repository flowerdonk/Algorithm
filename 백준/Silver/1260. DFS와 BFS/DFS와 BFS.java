import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M, V;
    static boolean[] visited;
    static boolean[][] graph;

    /**
     * BFS, DFS
     * @param v 시작 정점 번호
     */

    public static void dfs(int v) {
        visited[v] = true;
        System.out.print(v + " ");

        for (int i = 1; i < N + 1; i++) {
            if (graph[v][i] && !visited[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs(int v) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(v);
        visited[v] = true;
        System.out.print(v + " ");

        while (!queue.isEmpty()) {
            int temp = queue.poll();
            for (int i = 0; i < N + 1; i++) {
                if (graph[temp][i] && !visited[i]) {
                    queue.offer(i);
                    visited[i] = true;
                    System.out.print(i + " ");
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());

        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        V = Integer.parseInt(token.nextToken());

        graph = new boolean[N + 1][N + 1];
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(token.nextToken());
            int v = Integer.parseInt(token.nextToken());
            graph[u][v] = graph[v][u] = true;
        }

        visited = new boolean[N + 1];
        dfs(V);

        System.out.println();

        visited = new boolean[N + 1];
        bfs(V);

    }
}