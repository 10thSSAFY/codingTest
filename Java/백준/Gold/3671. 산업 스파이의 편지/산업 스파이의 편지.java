import java.io.*;
import java.util.*;

public class Main {

    static int c, len, result;
    static boolean[] prime = new boolean[10000000];
    static Set<Integer> set;
    static int[] paper;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        setPrime();

        c = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < c; tc++) {
            String str = br.readLine();
            len = str.length();
            set = new HashSet<>();
            result = 0;
            paper = new int[len];
            for (int i = 0; i < len; i++) {
                paper[i] = str.charAt(i) - '0';
            }

            solution(1, 0, 0);
            sb.append(result).append('\n');
        }

        System.out.println(sb);
    }


    public static void setPrime() {
        Arrays.fill(prime, true);
        prime[0] = prime[1] = false;
        for (int i = 2; i < 3164; i++) {
            if (prime[i]) {
                int n = i * 2;
                while (n < 10000000) {
                    prime[n] = false;
                    n += i;
                }
            }
        }
    }


    public static void solution(int order, int num, int visit) {

        if (!set.contains(num)) {
            set.add(num);
            if (prime[num]) result++;
        }

        for (int i = 0; i < len; i++) {
            if ((visit & (1 << i)) != 0) continue;
            solution(order * 10, num + paper[i] * order, visit | (1 << i));
        }
    }
}