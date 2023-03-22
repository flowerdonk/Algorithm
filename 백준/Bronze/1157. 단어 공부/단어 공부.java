import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String sent = br.readLine().toUpperCase();
        int[] letter = new int[26];
        for (int i = 0; i < sent.length(); i++){
            int idx = sent.charAt(i) - 'A';
            letter[idx] += 1;
        }

        int max = 0;
        char max_chr = 'a';
        for (int i = 0; i < 26; i++){
            if (letter[i] >= max){
                max = letter[i];
                max_chr = (char)(i + 'A');
            }
        }

        for (int i = 0; i < 26; i++){
            if (letter[i] == max && (char)(i + 'A') != max_chr){
                max_chr = '?';
                break;
            }
        }
        System.out.println(max_chr);
    }
}