import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    static StringTokenizer st;
    static int[][] map;
    static int[] selected;
    static Set<String> result;

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        map = new int[5][5];
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        selected = new int[6];
        result = new HashSet<>();
        for (int r = 0; r < 5; r++) {
            for (int c = 0; c < 5; c++) {
                dfs(r, c, 0);
            }
        }

        System.out.println(result.size());
    }

    static void dfs(int r, int c, int depth) {

        if (depth == 6) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 6; i++) {
                sb.append(selected[i]);
            }
            result.add(sb.toString());
            return;
        }

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (0 <= nr && nr < 5 && 0 <= nc && nc < 5) {
                selected[depth] = map[nr][nc];
                dfs(nr, nc, depth + 1);
            }
        }
    }
}