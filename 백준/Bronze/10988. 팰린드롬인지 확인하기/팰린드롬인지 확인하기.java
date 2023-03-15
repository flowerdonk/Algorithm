import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arr = br.readLine().toCharArray();
        int ans = 1;

        for (int i = 0; i < arr.length / 2; i++){
            if (arr[i] != arr[arr.length - 1 - i]){
                ans = 0;
                break;
            }
        }
        System.out.println(ans);
    }
}