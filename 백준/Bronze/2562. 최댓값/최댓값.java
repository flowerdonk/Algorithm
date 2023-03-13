import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[9];
        int mx = 0;
        int idx = 0;
        for (int i = 0; i < arr.length; i++) {
        	arr[i] = Integer.parseInt(br.readLine());
        	if (arr[i] >= mx) {
        		mx = arr[i];
        		idx = i + 1;
        	}
        }

        
        System.out.println(mx);
        System.out.println(idx);
    }
}