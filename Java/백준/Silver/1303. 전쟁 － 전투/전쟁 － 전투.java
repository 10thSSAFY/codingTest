import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int N, M, W, B, cnt;
    static char[][] A;
    static boolean[][] visited;

    static Queue<Node> q = new LinkedList<>();;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static class Node {

        int r, c;

        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        A = new char[M][N];
        visited = new boolean[M][N];

        for (int r = 0; r < M; r++) {
            String S = br.readLine();
            for (int c = 0; c < N; c++) {
                A[r][c] = S.charAt(c);
            }
        }

        for (int r = 0; r < M; r++) {
            for (int c = 0; c < N; c++) {
                if (!visited[r][c]) {
                    if (A[r][c] == 'W') {
                        int num = BFS(r, c, 'W');
                        W += num * num;
                    } else {
                        int num = BFS(r, c, 'B');
                        B += num * num;
                    }
                }
            }
        }

        System.out.println(W + " " + B);
    }

    static int BFS(int r, int c, char ch) {

        q.offer(new Node(r, c));
        visited[r][c] = true;
        cnt = 1;

        while (!q.isEmpty()) {
            Solution(ch);
        }

        return cnt;
    }

    static void Solution(char ch) {

        Node now = q.poll();

        for (int i = 0; i < 4; i++) {
            int nr = now.r + dr[i];
            int nc = now.c + dc[i];

            if (0 <= nr && nr < M && 0 <= nc && nc < N) {
                if (!visited[nr][nc] && A[nr][nc] == ch) {
                    q.offer(new Node(nr, nc));
                    visited[nr][nc] = true;
                    cnt++;
                }
            }
        }
    }
}