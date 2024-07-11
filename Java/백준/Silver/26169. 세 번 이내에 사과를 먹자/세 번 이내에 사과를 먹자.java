import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int dr[] = {-1, 0, 1, 0};
    static int dc[] = {0, 1, 0, -1};
    static int map[][] = new int[5][5];
    static int r, c;
    static int result;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        find(r, c, 0, 0);

        System.out.println(result);
    }

    static void find(int r, int c, int depth, int apple) {
        if (map[r][c] == 1) {
            apple++;
        }

        if (depth == 3) {
            if (apple >= 2) {
                result = 1;
            }
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (0 > nr || nr >= 5 || 0 > nc || nc >= 5 || map[nr][nc] == -1) {
                continue;
            }

            map[r][c] = -1;
            find(nr, nc, depth + 1, apple);
            map[r][c] = 0;
        }
    }
}