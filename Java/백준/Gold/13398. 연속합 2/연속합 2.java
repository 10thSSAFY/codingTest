import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        
        System.out.println(maxConsecutiveSum(n, arr));
    }

    public static int maxConsecutiveSum(int n, int[] arr) {

        int[] dp1 = new int[n];
        int[] dp2 = new int[n];

        dp1[0] = arr[0];
        dp2[0] = 0;
        int result = dp1[0];

        for (int i = 1; i < n; i++) {
            dp1[i] = Math.max(dp1[i-1] + arr[i], arr[i]);
            dp2[i] = Math.max(dp1[i-1], dp2[i-1] + arr[i]);
            result = Math.max(Math.max(result, dp1[i]), dp2[i]);
        }

        return result;
    }
}
