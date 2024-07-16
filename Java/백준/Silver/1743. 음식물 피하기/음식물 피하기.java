import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static StringTokenizer st;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    static int[][] map;
    static int result = 0;
    static int tmp = 0;
    static int N;
    static int M;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            map[r - 1][c - 1] = 1;
        }

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (map[r][c] == 1) {
                    tmp = 0;
                    dfs(r, c);
                    result = Math.max(tmp, result);
                }
            }
        }

        System.out.println(result);
    }

    static void dfs(int r, int c) {
        map[r][c] = 0;
        tmp++;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (0 > nr || nr >= N || 0 > nc || nc >= M) {
                continue;
            }
            if (map[nr][nc] == 1) {
                dfs(nr, nc);
            }
        }
    }
}