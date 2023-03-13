import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        
        for (int i = 0; i < M; i++) {
        	StringTokenizer str = new StringTokenizer(br.readLine(), " ");
        	int s = Integer.parseInt(str.nextToken());
        	int e = Integer.parseInt(str.nextToken());
        	int v = Integer.parseInt(str.nextToken());
        	for (int j = s - 1; j < e ; j++) {
        		arr[j] = v;        		
        	}

        }
        
        for (int n : arr) {
        	System.out.print(n + " ");
        }
    }
}