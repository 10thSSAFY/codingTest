import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] st = br.readLine().split(" ");
        int N = Integer.parseInt(st[0]);
        int M = Integer.parseInt(st[1]);

        boolean[][] pairs = new boolean[N+1][N+1];
        for (int i = 0; i < M; i++) {
            st = br.readLine().split(" ");
            int a = Integer.parseInt(st[0]);
            int b = Integer.parseInt(st[1]);
            pairs[a][b] = true;
            pairs[b][a] = true;
        }

        int result = 0;
        for (int i = 1; i <= N; i++) {
            for (int j = i + 1; j <= N; j++) {
                if (pairs[i][j]) continue;
                for (int k = j + 1; k <= N; k++) {
                    if (!pairs[j][k] && !pairs[k][i]) {
                        result++;
                    }
                }
            }
        }

        System.out.println(result);
    }
}