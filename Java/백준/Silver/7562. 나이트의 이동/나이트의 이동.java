import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static StringTokenizer st;
    static int[] dr = {-2, -1, 1, 2, 2, 1, -1, -2};
    static int[] dc = {1, 2, 2, 1, -1, -2, -2, -1};

    static boolean[][] visited;
    static int[][] map;
    static int T, l, sr, sc, er, ec;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            l = Integer.parseInt(br.readLine());
            map = new int[l][l];
            visited = new boolean[l][l];
            st = new StringTokenizer(br.readLine());
            sr = Integer.parseInt(st.nextToken());
            sc = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            er = Integer.parseInt(st.nextToken());
            ec = Integer.parseInt(st.nextToken());

            int result = BFS(sr, sc);
            System.out.println(result);
        }
    }

    static int BFS(int r, int c) {
        if (r == er && c == ec) {
            return 0;
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{r, c, 1});
        visited[r][c] = true;
        while (!queue.isEmpty()) {
            int now[] = queue.poll();
            for (int d = 0; d < 8; d++) {
                int nr = now[0] + dr[d];
                int nc = now[1] + dc[d];
                if (nr == er && nc == ec) {
                    return now[2];
                }
                if (0 <= nr && nr < l && 0 <= nc && nc < l) {
                    if (!visited[nr][nc]) {
                        visited[nr][nc] = true;
                        queue.add(new int[]{nr, nc, now[2] + 1});
                    }
                }
            }
        }
        return 0;
    }
}
