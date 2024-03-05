import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void main(String[] args) throws IOException {

        int T = readInt();

        for (int i = 0; i < T; i++) {
            int N = readInt();
            int M = readInt();

            Queue<int[]> queue = new LinkedList<>();

            for (int j = 0; j < N; j++) {
                int num = readInt();
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

    private static int readInt() throws IOException {
        int n = System.in.read() - '0';
        int c = System.in.read();
        while (c > ' ') {
            n = 10 * n + c - '0';
            c = System.in.read();
        }
        if (c == '\r') {
            System.in.read();
        }
        return n;
    }
}