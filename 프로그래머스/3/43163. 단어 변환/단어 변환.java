import java.util.*;

public class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        int N = words.length;
        int wordLen = begin.length();
        boolean[] visited = new boolean[N];
        
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(begin, 0));
        
        while (!q.isEmpty()) {
            Pair current = q.poll();
            String word = current.word;
            int cnt = current.cnt;
            
            if (word.equals(target)) {
                answer = cnt;
                break;
            }
            
            for (int n = 0; n < N; n++) {
                if (!visited[n]) {
                    int temp = 0;
                    for (int l = 0; l < wordLen; l++) {
                        if (word.charAt(l) != words[n].charAt(l)) {
                            temp++;
                        }
                    }
                    if (temp == 1) {
                        q.add(new Pair(words[n], cnt + 1));
                        visited[n] = true;
                    }
                }
            }
        }
        
        return answer;
    }
    
    private class Pair {
        String word;
        int cnt;
        
        Pair(String word, int cnt) {
            this.word = word;
            this.cnt = cnt;
        }
    }
}
