import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


class Ice {
    int r;
    int c;

    public Ice(int r, int c) {
        this.r = r;
        this.c = c;
    }
}


class Main {

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    static StringTokenizer st;

    static int N, M;
    static int[][] map;
    static boolean[][] visited;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int time = 0;
        while (true) {
            int result = countIsland();

            if (result >= 2) {
                break;
            } else if (result == 0) {
                time = 0;
                break;
            }

            bfs();
            time++;
        }

        System.out.println(time);
    }

    public static int countIsland() {

        boolean[][] visited = new boolean[N][M];
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] > 0 && !visited[i][j]) {
                    dfs(i, j, visited);
                    cnt++;
                }
            }
        }

        return cnt;
    }

    public static void dfs(int r, int c, boolean[][] visited) {

        visited[r][c] = true;

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                if (map[nr][nc] > 0 && !visited[nr][nc]) {
                    dfs(nr, nc, visited);
                }
            }
        }
    }

    public static void bfs() {
        Queue<Ice> q = new LinkedList<>();
        boolean[][] visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] > 0) {
                    q.add(new Ice(i, j));
                    visited[i][j] = true;
                }
            }
        }

        while (!q.isEmpty()) {
            Ice ice = q.poll();

            int sea = 0;

            for (int i = 0; i < 4; i++) {
                int nr = ice.r + dr[i];
                int nc = ice.c + dc[i];

                if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                    if (!visited[nr][nc] && map[nr][nc] == 0) {
                        sea++;
                    }
                }
            }

            if (map[ice.r][ice.c] - sea < 0) {
                map[ice.r][ice.c] = 0;
            } else {
                map[ice.r][ice.c] -= sea;
            }
        }
    }
}
