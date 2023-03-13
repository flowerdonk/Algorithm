import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        StringTokenizer str = new StringTokenizer(br.readLine(), " ");
        int[] arr = new int[N];
        for (int i = 0; i < arr.length; i++) {
        	arr[i] = Integer.parseInt(str.nextToken());
        }
        
        int cnt = 0;
        for (int i = 0; i < arr.length; i++) {
        	if (arr[i] < X) {
        		System.out.print(arr[i] + " ");
        	}
        }
        
    }
}