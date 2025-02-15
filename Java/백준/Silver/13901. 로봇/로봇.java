import java.io.*;
import java.util.*;

public class Main {

    static int R, C, k, sr, sc;
    static int[][] map;
    static boolean[][] visited;
    static int[] moves = new int[4];

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new int[R][C];
        visited = new boolean[R][C];

        k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            map[r][c] = 2;
        }

        st = new StringTokenizer(br.readLine());
        sr = Integer.parseInt(st.nextToken());
        sc = Integer.parseInt(st.nextToken());
        visited[sr][sc] = true;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++)
            moves[i] = Integer.parseInt(st.nextToken());

        solution();
        System.out.println(sr + " " + sc);
    }


    static void solution() {

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{sr, sc});
        int idx = 0;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nr = curr[0] + dr[moves[(idx + i) % 4] - 1];
                int nc = curr[1] + dc[moves[(idx + i) % 4] - 1];

                if (nr < 0 || R <= nr || nc < 0 || C <= nc || visited[nr][nc] || map[nr][nc] == 2)
                    continue;

                visited[nr][nc] = true;
                queue.offer(new int[]{nr, nc});
                idx = (idx + i) % 4;
                sr = nr;
                sc = nc;
                break;
            }
        }
    }
}
