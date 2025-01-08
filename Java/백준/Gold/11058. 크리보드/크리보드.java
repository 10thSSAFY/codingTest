import java.io.*;
import java.util.*;

class Main {

    static long[] dp;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        dp = new long[N + 1];
        for (int i = 0; i < Math.min(N + 1, 6); i++) {
            dp[i] = i;
        }

        for (int i = 6; i <= N; i++) {
            dp[i] = Math.max(Math.max(dp[i - 3] * 2, dp[i - 4] * 3), dp[i - 5] * 4);
        }

        System.out.println(dp[N]);
    }
}