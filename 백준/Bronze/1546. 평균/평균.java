import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        double[] arr = new double[N];
        double mx = 0;
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
        	arr[i] = Integer.parseInt(st.nextToken());
        	if (arr[i] >= mx) {
        		mx = arr[i];
        	}
        }
        
        double aver = 0;
        for (int i = 0; i < N; i++) {
        	arr[i] = arr[i] / mx * 100;
        	aver += arr[i];
        }
        
        System.out.println(aver/N);
        
    }
}