import java.io.*;
import java.util.*;

class Main {

    static int N, testCase;
    static String[] names;
    static boolean[] count;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while ((N = Integer.parseInt(br.readLine())) != 0) {
            names = new String[N + 1];
            count = new boolean[N + 1];

            for (int i = 1; i <= N; i++) {
                names[i] = br.readLine();
            }

            for (int i = 1; i <= N * 2 - 1; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int n = Integer.parseInt(st.nextToken());
                if (!count[n]) {
                    count[n] = true;
                } else {
                    count[n] = false;
                }
            }

            for (int i = 1; i <= N; i++) {
                if (count[i]) {
                    sb.append(++testCase).append(" ").append(names[i]).append('\n');
                }
            }
        }

        System.out.println(sb);
    }
}
