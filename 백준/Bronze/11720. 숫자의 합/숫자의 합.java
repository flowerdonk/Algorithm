import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long total = 0;
        char[] str = br.readLine().toCharArray();
        for (int i = 0; i < N; i++) {
        	total += (int)str[i] - '0';
        }
        System.out.println(total);
                
    }
}