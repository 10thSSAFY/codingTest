import java.io.*;
import java.util.*;

public class Main {

    static int T, N;
    static int[] dp = new int[1001];

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Arrays.fill(dp, -1);
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= 1000; i++) {
            if (i % 2 == 0)
                dp[i] = dp[i - 1] + dp[i / 2];
            else
                dp[i] = dp[i - 1];
        }

        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            N = Integer.parseInt(br.readLine());
            System.out.println(dp[N]);
        }
    }
}
