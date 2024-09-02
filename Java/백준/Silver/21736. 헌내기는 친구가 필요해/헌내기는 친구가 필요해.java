import java.io.*;
import java.util.*;

public class Main{

    static StringTokenizer st;
    static int N, M, result;
    static int[][] arr;
    static boolean[][] visited;
    static point iPos;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    static class point {
        int r, c;

        public point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        visited = new boolean[N][M];

        for (int r = 0; r < N; r++) {
            String S = br.readLine();

            for (int c = 0; c < M; c++) {
                arr[r][c] = S.charAt(c);

                if (arr[r][c] == 'I') {
                    iPos = new point(r, c);
                }
            }
        }

        Queue<point> q = new LinkedList<>();
        q.add(iPos);
        visited[iPos.r][iPos.c] = true;
        result = 0;

        while (!q.isEmpty()) {
            point nPos = q.poll();

            if (arr[nPos.r][nPos.c] == 'P') {
                result++;
            }

            for (int d = 0; d < 4; d++) {
                int nr = nPos.r + dr[d];
                int nc = nPos.c + dc[d];

                if (nr < 0 || N <= nr || nc < 0 || M <= nc || visited[nr][nc]) {
                    continue;
                }

                if (arr[nr][nc] == 'X') {
                    continue;
                }

                q.add(new point(nr, nc));
                visited[nr][nc] = true;
            }
        }

        if (result == 0) {
            System.out.println("TT");
        } else {
            System.out.println(result);
        }
    }
}