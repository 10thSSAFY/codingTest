import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        final int MOD = 1000000;
        int[] dp = new int[str.length() + 1];
        dp[0] = 1;

        for (int i = 1; i <= str.length(); i++) {
            int now = str.charAt(i - 1) - '0';
            if (1 <= now && now <= 9) {
                dp[i] += dp[i - 1];
                dp[i] %= MOD;
            }

            if (i == 1) continue;

            int prev = str.charAt(i - 2) - '0';
            if (prev == 0) continue;

            int value = prev * 10 + now;
            if (10 <= value && value <= 26) {
                dp[i] += dp[i - 2];
                dp[i] %= MOD;
            }
        }

        System.out.println(dp[str.length()]);
    }
}