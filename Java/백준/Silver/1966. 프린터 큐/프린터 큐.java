import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int N, M;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            Queue<int[]> queue = new LinkedList<>();

            for (int j = 0; j < N; j++) {
                int num = Integer.parseInt(st.nextToken());
                queue.add(new int[]{j, num});
            }

            int cnt = 0;
            while (true) {
                int[] num = queue.poll();
                boolean check = true;

                for (int[] n : queue) {
                    if (n[1] > num[1]) {
                        check = false;
                        break;
                    }
                }

                if (check) {
                    cnt++;
                    if (num[0] == M) break;
                } else {
                    queue.add(num);
                }
            }

            System.out.println(cnt);
        }
    }
}