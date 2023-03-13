import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] str = br.readLine().toCharArray();
        // 97 : a
        int[] alpha = new int[26];
        
        for (int i = 0; i < 26; i++) {
        	alpha[i] = -1;
        }
        for (int i = 0; i < str.length; i++) {
        	int idx = (int)str[i] - 97;
        	if (alpha[idx] == -1) {
        		alpha[idx] = i;        		
        	}
        }
        for(int n : alpha) {
        	System.out.print(n + " ");        	
        }
                
    }
}