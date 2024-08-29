import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

    static int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
    static int[] dc = {-1, 0, 1, -1, 1, -1, 0 ,1};
    static boolean[][] visited;
    static int[][] A;
    static int w, h, nr, nc;
    static int result;
    static StringTokenizer st;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            if (w == 0 && h == 0) {
                break;
            }

            A = new int[h][w];
            visited = new boolean[h][w];
            for (int r = 0; r < h; r++) {
                st = new StringTokenizer(br.readLine());
                for (int c = 0; c < w; c++) {
                    A[r][c] = Integer.parseInt(st.nextToken());
                }
            }

            result = 0;
            for (int r = 0; r < h; r++) {
                for (int c = 0; c < w; c++) {
                    if (!visited[r][c] && A[r][c] == 1) {
                        result++;
                        DFS(r, c);
                    }
                }
            }
            System.out.println(result);
        }
    }

    public static void DFS(int r, int c) {
        visited[r][c] = true;

        for (int d = 0; d < 8; d++) {
            nr = dr[d] + r;
            nc = dc[d] + c;

            if (range() && !visited[nr][nc] && A[nr][nc] == 1) {
                DFS(nr, nc);
            }
        }
    }

    static boolean range() {
        return (0 <= nr && nr < h && 0 <= nc && nc < w);
    }
}