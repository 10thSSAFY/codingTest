import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String S1 = br.readLine();
        String S2 = br.readLine();

        int[][] dp = new int[S1.length()][S2.length()];
        for (int i = 0; i < S1.length(); i++) {
            for (int j = 0; j < S2.length(); j++) {
                if (S1.charAt(i) == S2.charAt(j)) {
                    if (i == 0 || j == 0) {
                        dp[i][j] = 1;
                    } else {
                        dp[i][j] = dp[i - 1][j - 1] + 1;
                    }
                }
            }
        }

        int result = 0;
        for (int i = 0; i < S1.length(); i++) {
            int[] numbers = dp[i];
            result = Math.max(result, Arrays.stream(numbers).max().getAsInt());
        }

        System.out.println(result);
    }
}
