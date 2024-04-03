import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static StringTokenizer st;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[1000001];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            dp[Integer.parseInt(st.nextToken())] += 1;
        }

        int result = 0;
        int num;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            num = Integer.parseInt(st.nextToken());
            if (dp[num] > 0) {
                dp[num] -= 1;
            } else {
                result += 1;
            }
        }
        
        System.out.println(result);
    }
}