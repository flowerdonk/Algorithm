import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int[] arr = new int[6];
        for(int i = 0; i < 6; i++) {
        	arr[i] = Integer.parseInt(st.nextToken());
        }
        int[] chess = new int[] {1, 1, 2, 2, 2, 8};
        
        for (int i = 0; i < arr.length; i++) {
        	System.out.print(chess[i] - arr[i] + " ");
        }      
                      
    }
}