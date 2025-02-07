import java.io.*;
import java.util.*;

public class Main {

    static int R, C;
    static int[][] arr, visit;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        arr = new int[R][C];

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        if (arr[0][0] == -1 || arr[R - 1][C - 1] == -1) {
            System.out.println(-1);
            return;
        }

        visit = new int[R][C];
        for (int i = 0; i < R; i++) {
            Arrays.fill(visit[i], 1000001);
        }

        int result = solution(0, 0);
        System.out.println(result);
    }

    public static int solution(int r, int c) {
        visit[r][c] = arr[r][c];
        PriorityQueue<Pos> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
        pq.offer(new Pos(r, c, visit[r][c]));

        while (!pq.isEmpty()) {
            Pos curr = pq.poll();
            if (curr.r == R - 1 && curr.c == C - 1)
                return visit[curr.r][curr.c];

            if (visit[curr.r][curr.c] < curr.cost)
                continue;

            for (int i = 0; i < 4; i++) {
                int nr = curr.r + dr[i];
                int nc = curr.c + dc[i];
                if (0 <= nr && nr < R && 0 <= nc && nc < C && arr[nr][nc] != -1) {
                    int cost = arr[nr][nc] + curr.cost;
                    if (visit[nr][nc] > cost) {
                        visit[nr][nc] = cost;
                        pq.offer(new Pos(nr, nc, cost));
                    }
                }
            }
        }
        return -1;
    }
}

class Pos {
    int r;
    int c;
    int cost;

    public Pos(int r, int c, int cost) {
        this.r = r;
        this.c = c;
        this.cost = cost;
    }
}
