import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int R, C;
    static char[][] arr;
    static boolean[] visited = new boolean[26];
    static int answer = 1;
    static StringTokenizer st;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        arr = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                arr[i][j] = line.charAt(j);
            }
        }

        visited[arr[0][0] - 'A'] = true;
        dfs(0, 0, 1);

        System.out.println(answer);
    }

    public static void dfs(int r, int c, int count) {
        answer = Math.max(answer, count);

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int[] d : directions) {
            int nr = d[0] + r;
            int nc = d[1] + c;

            if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

            if (!visited[arr[nr][nc] - 'A']) {
                visited[arr[nr][nc] - 'A'] = true;
                dfs(nr, nc, count + 1);
                visited[arr[nr][nc] - 'A'] = false;
            }
        }
    }
}
