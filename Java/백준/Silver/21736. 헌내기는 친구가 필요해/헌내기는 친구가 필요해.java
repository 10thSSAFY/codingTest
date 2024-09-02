import java.io.*;
import java.util.*;

public class Main{

    static StringTokenizer st;
    static int N, M, result;
    static int[][] arr;
    static boolean[][] visited;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        visited = new boolean[N][M];
        Queue<int[]> q = new LinkedList<>();

        for (int r = 0; r < N; r++) {
            String S = br.readLine();

            for (int c = 0; c < M; c++) {
                arr[r][c] = S.charAt(c);

                if (arr[r][c] == 'I') {
                    q.add(new int[] {r, c});
                    visited[r][c] = true;
                }
            }
        }

        result = 0;

        while (!q.isEmpty()) {
            int[] nPos = q.poll();
            int r = nPos[0], c = nPos[1];

            if (arr[r][c] == 'P') {
                result++;
            }

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr < 0 || N <= nr || nc < 0 || M <= nc || visited[nr][nc]) {
                    continue;
                }

                if (arr[nr][nc] == 'X') {
                    continue;
                }

                q.add(new int[] {nr, nc});
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