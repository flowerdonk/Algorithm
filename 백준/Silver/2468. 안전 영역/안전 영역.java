import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] map;
    static boolean[][] visited;
    static int maxH;

    /**
     * dfs
     * @param h 높이
     * @param x x 좌표
     * @param y y 좌표
     */
    private static void dfs(int h, int x, int y) {
        int[] dirX = new int[]{-1, 0, 1, 0};
        int[] dirY = new int[]{0, -1, 0, 1};

        for (int k = 0; k < 4; k++) {
            int nextX = x + dirX[k];
            int nextY = y + dirY[k];
            // 다음 이동 좌표 범위 확인
            if (0 <= nextX && nextX < N && 0 <= nextY && nextY < N && !visited[nextX][nextY]) {
                // 잠기는 높이인지 확인
                if (map[nextX][nextY] > h) {
                    visited[nextX][nextY] = true;
                    dfs(h, nextX, nextY);
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer token;
        map = new int[N][N];
        maxH = 0;
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int parseInt = Integer.parseInt(token.nextToken());
                map[i][j] = parseInt;
                maxH = Math.max(maxH, parseInt);
            }
        }

        int ans = 1;
        for (int h = 1; h < maxH; h++) {
            visited = new boolean[N][N];
            int temp = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (map[i][j] > h && !visited[i][j]) {
                        visited[i][j] = true;
                        dfs(h, i, j);
                        temp++;
                    }
                }
            }
            ans = Math.max(ans, temp);
        }

        System.out.println(ans);
    }

}