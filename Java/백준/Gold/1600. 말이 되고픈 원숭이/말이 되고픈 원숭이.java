import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int K, W, H;
    static int[][] A;
    static boolean[][][] visited;
    static int[] hdr = {-2, -2, -1, -1, 1, 1, 2, 2};
    static int[] hdc = {-1, 1, -2, 2, -2, 2, -1, 1};
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static class Node {

        int r, c, cnt, k;

        public Node(int r, int c, int cnt, int k) {
            this.r = r;
            this.c = c;
            this.cnt = cnt;
            this.k = k;
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        A = new int[H][W];
        visited = new boolean[H][W][K + 1];
        for (int r = 0; r < H; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < W; c++) {
                A[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        int result = bfs(0, 0);
        System.out.println(result);
    }

    public static int bfs(int r, int c) {
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(r, c, 0, K));
        visited[r][c][K] = true;

        while (!q.isEmpty()) {
            Node curr = q.poll();

            if (curr.r == H - 1 && curr.c == W - 1) {
                return curr.cnt;
            }

            for (int d = 0; d < 4; d++) {
                int nr = curr.r + dr[d];
                int nc = curr.c + dc[d];

                if (nr < 0 || H <= nr || nc < 0 || W <= nc || visited[nr][nc][curr.k] || A[nr][nc] == 1) {
                    continue;
                }

                visited[nr][nc][curr.k] = true;
                q.offer(new Node(nr, nc, curr.cnt + 1, curr.k));
            }

            if (curr.k > 0) {
                for (int d = 0; d < 8; d++) {
                    int nr = curr.r + hdr[d];
                    int nc = curr.c + hdc[d];

                    if (nr < 0 || H <= nr || nc < 0 || W <= nc || visited[nr][nc][curr.k - 1] || A[nr][nc] == 1) {
                        continue;
                    }

                    visited[nr][nc][curr.k - 1] = true;
                    q.offer(new Node(nr, nc, curr.cnt + 1, curr.k - 1));
                }
            }
        }

        return -1;
    }
}