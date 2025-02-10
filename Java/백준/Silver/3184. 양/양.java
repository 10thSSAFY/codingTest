import java.io.*;
import java.util.*;

class Main {

    static int R, C, O, V;
    static char[][] arr;
    static boolean[][] visit;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        arr = new char[R][];
        for (int i = 0; i < R; i++) {
            arr[i] = br.readLine().toCharArray();
        }

        visit = new boolean[R][C];
        O = 0;
        V = 0;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (!visit[r][c] && arr[r][c] != '#') {
                    visit[r][c] = true;
                    solution(r, c);
                }
            }
        }

        System.out.println(O + " " + V);
    }


    static void solution(int r, int c) {

        int tmpO = 0;
        int tmpV = 0;

        Stack<Pos> stack = new Stack<>();
        stack.push(new Pos(r, c));

        if (arr[r][c] == 'o') {
            tmpO++;
        } else if (arr[r][c] == 'v') {
            tmpV++;
        }

        while (!stack.isEmpty()) {
            Pos curr = stack.pop();
            for (int i = 0; i < 4; i++) {
                int nr = curr.r + dr[i];
                int nc = curr.c + dc[i];

                if (nr < 0 || R <= nr || nc < 0 || C <= nc || visit[nr][nc] || arr[nr][nc] == '#') continue;

                visit[nr][nc] = true;
                if (arr[nr][nc] == 'o') {
                    tmpO++;
                } else if (arr[nr][nc] == 'v') {
                    tmpV++;
                }
                stack.push(new Pos(nr, nc));

            }
        }

        if (tmpO > tmpV) {
            O += tmpO;
        } else {
            V += tmpV;
        }
    }
}

class Pos {

    int r;
    int c;

    Pos(int r, int c) {

        this.r = r;
        this.c = c;
    }
}
