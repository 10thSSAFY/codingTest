import java.io.*;
import java.util.*;

public class Main {

    static int N, M, result;
    static boolean[] arr;
    static int[] dp;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new boolean[N];

        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            int n = Integer.parseInt(br.readLine());
            arr[n - 1] = true;
        }

        dp = new int[41];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < 41; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        result = 1;
        int curr = 0;
        for (int i = 0; i < N; i++) {
            if (!arr[i]) {
                curr++;
            } else {
                result *= dp[curr];
                curr = 0;
            }
        }
        result *= dp[curr];

        System.out.println(result);
    }
}