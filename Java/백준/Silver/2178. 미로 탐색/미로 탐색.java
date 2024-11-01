import java.io.*;
import java.util.*;

public class Main {

    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};

    static int N, M;
    static int[][] arr;
    static boolean[][] visited;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(line.substring(j, j + 1));
            }
        }

        BFS(0, 0);
        System.out.println(arr[N - 1][M - 1]);
    }

    static void BFS(int r, int c) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{r, c});
        visited[r][c] = true;
        while (!queue.isEmpty()) {
            int now[] = queue.poll();
            for (int d = 0; d < 4; d++) {
                int nr = now[0] + dr[d];
                int nc = now[1] + dc[d];

                if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                    if (arr[nr][nc] == 1 && !visited[nr][nc]) {
                        visited[nr][nc] = true;
                        arr[nr][nc] = arr[now[0]][now[1]] + 1;
                        queue.offer(new int[]{nr, nc});
                    }
                }
            }
        }
    }
}