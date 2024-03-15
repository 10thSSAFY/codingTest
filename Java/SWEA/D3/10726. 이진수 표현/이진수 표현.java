import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int testcase = 1; testcase <= T; testcase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int lastNBit = (1 << N) - 1;  // 111...1 (길이 N)

            if (lastNBit == (M & lastNBit)) {
                System.out.println("#" + testcase + " " + "ON");
            } else {
                System.out.println("#" + testcase + " " + "OFF");
            }
        }
    }
}