import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    /**
     * @param balls 공
     * @param N 공 갯수
    */

    public int solution(String balls, int N) {
        int answer = Integer.MAX_VALUE;

        // Red <--
        answer = moveLeft(answer, 'R', 'B', N, balls);

        // Red -->
        answer = moveRight(answer, 'R', 'B', N, balls);

        // Blue <--
        answer = moveLeft(answer, 'B', 'R', N, balls);

        // Blue -->
        answer = moveRight(answer, 'B', 'R', N, balls);

        return answer;
    }

    public int moveLeft(int minMove, char color, char otherColor, int N, String balls) {
        int cnt = 0;
        boolean flag = false;

        for (int i = 0; i < N; i++) {
            if (flag && balls.charAt(i) == color) {
                cnt++;
                continue;
            }
            if (balls.charAt(i) == otherColor) flag = true;
        }

        return Math.min(cnt, minMove);
    }

    public int moveRight(int minMove, char color, char otherColor, int N, String balls) {
        int cnt = 0;
        boolean flag = false;

        for (int i = N - 1; i >= 0; i--) {
            if (flag && balls.charAt(i) == color) {
                cnt++;
                continue;
            }
            if (balls.charAt(i) == otherColor) flag = true;
        }

        return Math.min(cnt, minMove);
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String balls = br.readLine();
        System.out.println(main.solution(balls, N)); // 결과: 4
    }
}