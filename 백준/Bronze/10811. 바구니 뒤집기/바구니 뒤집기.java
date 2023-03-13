import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        
        for (int i = 0; i < N; i++) {
        	arr[i] = i + 1;
        }
        
        for (int i = 0; i < M; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine(), " ");
            int s = Integer.parseInt(str.nextToken()) - 1;
            int e = Integer.parseInt(str.nextToken()) - 1;
            
        	for (int j = 0; j < (e - s + 1) / 2; j++) {
        		int temp = arr[s + j];
        		arr[s + j] = arr[e - j];
        		arr[e - j] = temp;
        	}
        }
        
        for (int n : arr) {
        	System.out.print(n + " ");        	
        }
        
    }
}