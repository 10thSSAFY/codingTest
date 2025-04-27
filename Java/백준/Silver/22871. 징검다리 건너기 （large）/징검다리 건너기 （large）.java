import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static long power;
    static long[] A, dp;
    static StringTokenizer st;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        A = new long[N];
        dp = new long[N];
        Arrays.fill(dp, Long.MAX_VALUE);
        dp[0] = 0;
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < i; j++) {
                power = Math.max(dp[j], (i - j) * (1 + Math.abs(A[i] - A[j])));
                dp[i] = Math.min(dp[i], power);
            }
        }

        System.out.println(dp[N - 1]);
    }
}