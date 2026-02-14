import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int M, N, K;
    static int[][] map;
    static boolean[][] visited;
    static ArrayList<Integer> stages;

    /**
     * bfs
     * @param x x 좌표
     * @param y y 좌표
     */
    private static void bfs(int x, int y) {
        int[] dirX = {-1, 0, 1, 0};
        int[] dirY = {0, 1, 0, -1};
        int count = 0;
        Queue<int[]> queue = new ArrayDeque();
        queue.offer(new int[]{x, y});
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] temp = queue.poll();
            count++;

            for (int d = 0; d < 4; d++) {
                int nextX = temp[0] + dirX[d];
                int nextY = temp[1] + dirY[d];
                if (0 <= nextX && nextX < M && 0 <= nextY && nextY < N) { // 범위 내
                    if (map[nextX][nextY] == 0 && !visited[nextX][nextY]) { // 조건 내
                        queue.offer(new int[]{nextX, nextY});
                        visited[nextX][nextY] = true;
                    }
                }
            }
        }


        stages.add(count);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        M = Integer.parseInt(token.nextToken());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());

        map = new int[M][N];
        for (int k = 0; k < K; k++) {
            token = new StringTokenizer(br.readLine());
            int leftX = Integer.parseInt(token.nextToken());
            int leftY = Integer.parseInt(token.nextToken());
            int rightX = Integer.parseInt(token.nextToken());
            int rightY = Integer.parseInt(token.nextToken());
            for (int i = leftX; i < rightX; i++) {
                for (int j = leftY; j < rightY; j++) {
                    map[j][i] = 1;
                }
            }
        }

        visited = new boolean[M][N];
        stages = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 0 && !visited[i][j]) {
                    bfs(i, j);
                }
            }
        }

        stages.sort(Comparator.naturalOrder());
        System.out.println(stages.size());
        for (int stage : stages) {
            System.out.print(stage + " ");
        }
    }

}