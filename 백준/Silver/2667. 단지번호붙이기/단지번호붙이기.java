import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[][] map;
    static boolean[][] visited;

    /**
     * dfs
     */
    private static ArrayList<Integer> bfs() {
        int[] dirX = new int[]{-1, 0, 1, 0};
        int[] dirY = new int[]{0, -1, 0, 1};
        ArrayList<Integer> house = new ArrayList<>();
        Queue<int[]> queue = new ArrayDeque();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    queue.offer(new int[]{i, j});
                    visited[i][j] = true;
                    int temp = 0;
                    while (!queue.isEmpty()) {
                        int[] now = queue.poll();
                        temp++;
                        for (int dir = 0; dir < 4; dir++) {
                            int nextX = now[0] + dirX[dir];
                            int nextY = now[1] + dirY[dir];
                            if (nextX >= 0 && nextX < N && nextY >= 0 && nextY < N && !visited[nextX][nextY] && map[nextX][nextY] == 1) {
                                queue.offer(new int[]{nextX, nextY});
                                visited[nextX][nextY] = true;
                            }
                        }
                    }
                    house.add(temp);
                }
            }
        }

        house.sort(Comparator.naturalOrder());
        return house;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        map = new int[N][N];
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < N; j++) {
                map[i][j] = str.charAt(j) - '0';
            }
        }

        visited = new boolean[N][N];
        ArrayList<Integer> answer = bfs();
        System.out.println(answer.size());
        for (Integer a : answer) {
            System.out.println(a);
        }
    }

}
