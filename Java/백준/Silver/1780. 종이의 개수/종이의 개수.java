import java.io.*;
import java.util.*;

public class Main {

    static int[][] board;
    static int res1, res2, res3 = 0;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        part(0, 0, N);

        System.out.println(res1);
        System.out.println(res2);
        System.out.println(res3);
    }

    public static void part(int r, int c, int d) {

        if (check(r, c, d)) {
            if (board[r][c] == -1) {
                res1++;
            } else if (board[r][c] == 0) {
                res2++;
            } else {
                res3++;
            }

            return;
        }

        int div = d / 3;

        part(r , c , div);
        part(r, c + div, div);
        part(r, c + 2 * div, div);

        part(r + div, c, div);
        part(r + div, c + div, div);
        part(r + div, c + 2 * div, div);

        part(r + 2 * div, c, div);
        part(r + 2 * div, c + div, div);
        part(r + 2 * div, c + 2 * div, div);
    }

    public static boolean check(int r, int c, int d) {

        int num = board[r][c];

        for (int i = r; i < r + d; i++) {
            for (int j = c; j < c + d; j++) {
                if (num != board[i][j]) {
                    return false;
                }
            }
        }

        return true;
    }
}