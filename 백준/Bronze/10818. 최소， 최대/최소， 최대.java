import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int[] arr = new int[N];
        for (int i = 0; i < arr.length; i++) {
        	arr[i] = Integer.parseInt(st.nextToken());
        }
        
        int mx = -1000000;
        int mn = 1000000;
        for (int i = 0; i < arr.length; i++) {
        	if (arr[i] <= mn) {
        		mn = arr[i];
        	}
        	if (arr[i] >= mx) {
        		mx = arr[i];
        	}
        }
        
        System.out.print(mn + " " + mx);
    }
}