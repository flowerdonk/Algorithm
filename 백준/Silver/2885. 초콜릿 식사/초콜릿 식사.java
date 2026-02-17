import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        int msbValue = Integer.highestOneBit(N);
        if (msbValue < N) msbValue <<= 1;

        int count = 0;
        if (msbValue != N) {
            int total = Integer.numberOfTrailingZeros(msbValue);
            int last = Integer.numberOfTrailingZeros(N);
            count = total - last;
        }

        System.out.print(msbValue + " " + count);
    }

}