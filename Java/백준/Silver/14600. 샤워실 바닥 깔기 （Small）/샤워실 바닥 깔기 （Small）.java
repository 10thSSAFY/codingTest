import java.io.*;
import java.util.*;

class Main {

    static int N, x, y;
    static int[][] map;
    static int count;

    public static void main(String[] args) throws Exception {

        init();
        solution(1, 1, N);
        answer();
    }

    static void init() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());

        N = (int) Math.pow(2, N);
        map = new int[N + 1][N + 1];
        map[y][x] = -1;
    }

    static void solution(int x, int y, int size) {

        count++;
        int ns = size / 2;
        int nx = x + ns;
        int ny = y + ns;

        if (check(x, y, ns))
            map[nx - 1][ny - 1] = count;
        if (check(nx, y, ns))
            map[nx][ny - 1] = count;
        if (check(x, ny, ns))
            map[nx - 1][ny] = count;
        if (check(nx, ny, ns)) {
            map[nx][ny] = count;
        }

        if (size == 2)
            return;

        solution(x, y, ns);
        solution(nx, y, ns);
        solution(x, ny, ns);
        solution(nx, ny, ns);
    }

    static boolean check(int x, int y, int s) {

        for (int i = x; i < x + s; i++) {
            for (int j = y; j < y + s; j++) {
                if (map[i][j] != 0)
                    return false;
            }
        }

        return true;
    }

    static void answer() {

        StringBuilder sb = new StringBuilder();

        for (int i = N; i >= 1; i--) {
            for (int j = 1; j <= N; j++) {
                sb.append(map[i][j]).append(" ");
            }
            sb.append('\n');
        }

        System.out.println(sb);
    }
}