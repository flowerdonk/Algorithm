import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int ans;

        if (A == B && B == C){
            ans = 10000 + A * 1000;
        } else if (A == B || A == C) {
            ans = 1000 + A * 100;
        } else if (B == C) {
            ans = 1000 + B * 100;
        } else{
            if (A > B){
                if (A > C){
                    ans = A * 100;
                }else {
                    ans = C * 100;
                }
            }else{
                if (B > C){
                    ans = B * 100;
                }
                else{
                    ans = C * 100;
                }
            }
        }

        System.out.println(ans);
    }
}