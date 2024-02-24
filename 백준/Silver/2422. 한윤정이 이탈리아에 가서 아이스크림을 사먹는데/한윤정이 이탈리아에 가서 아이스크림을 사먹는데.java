import java.io.IOException;

public class Main {
    private static boolean[][] pair;
    public static void main(String[] args) throws IOException {
        int N = readInt(), M = readInt();
        pair = new boolean[N][N];
        for (int i = 0; i < M; i++) {
            int a = readInt(), b = readInt();
            pair[a - 1][b - 1] = true;
            pair[b - 1][a - 1] = true;
        }

        int cnt = 0;
        for (int i = 1; i <= N - 2; i++) {
            for (int j = i + 1; j <= N - 1; j++) {
                if (pair[i - 1][j - 1]) continue;
                for (int k = j + 1; k <= N; k++) {
                    if (pair[i - 1][k - 1] || pair[j - 1][k - 1]) continue;
                    cnt++;
                }
            }
        }

        System.out.println(cnt);
    }

    private static int readInt() throws IOException {
        int val = 0;
        int c = System.in.read();
        while (c <= ' ') {
            c = System.in.read();
        } do {
            val = 10 * val + c - 48;
        } while ((c = System.in.read()) >= 48 && c <= 57);
        return val;
    }
}