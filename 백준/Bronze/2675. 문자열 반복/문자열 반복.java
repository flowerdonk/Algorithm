import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < T; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        	int R = Integer.parseInt(st.nextToken());
        	char[] str = st.nextToken().toCharArray();
        	
        	for(char n : str) {
	        	for (int j = 0; j < R; j++) {
	        		System.out.print(n); 
	        	}
        	}
        	System.out.print('\n'); 
        }
                      
    }
}