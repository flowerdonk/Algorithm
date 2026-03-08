import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int M, N;
    static int[][] data;

    /**
     * [bfs]
     *
     */
    private static int bfs(Queue<int[]> queue, int count) {
        int[] dirX = new int[]{-1, 0, 1, 0};
        int[] dirY = new int[]{0, 1, 0, -1};
        boolean[][] visited = new boolean[N][M];
        int result = 0, tempCount = queue.size();

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            visited[now[0]][now[1]] = true;
            result = now[2];

            for (int d = 0; d < 4; d++) {
                int nextX = now[0] + dirX[d];
                int nextY = now[1] + dirY[d];
                if (nextX >= 0 && nextX < N && nextY >= 0 && nextY < M && !visited[nextX][nextY]) {
                    if (data[nextX][nextY] == 0){
                        queue.offer(new int[]{nextX, nextY, now[2] + 1});
                        visited[nextX][nextY] = true;
                        tempCount++;
                    }
                }
            }

        }

        if (tempCount == count) return result;
        else return -1;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        M = Integer.parseInt(token.nextToken());
        N = Integer.parseInt(token.nextToken());
        int count = 0;

        data = new int[N][M];
        Queue<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int temp = Integer.parseInt(token.nextToken());
                if (temp != -1) {
                    count++;
                    if (temp == 1) queue.offer(new int[]{i, j, 0});
                }
                data[i][j] = temp;
            }
        }

        System.out.println(bfs(queue, count));;

    }

}