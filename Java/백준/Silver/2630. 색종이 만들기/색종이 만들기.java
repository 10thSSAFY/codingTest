import java.io.*;
import java.util.*;

public class Main {

    static int[][] arr;
    static int white = 0;
    static int blue = 0;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solution(0, 0, N);

        System.out.println(white);
        System.out.println(blue);
    }

    static void solution(int r, int c, int size) {

        if (check(r, c, size)) {
            if (arr[r][c] == 1) {
                blue++;
            } else {
                white++;
            }
            return;
        }

        size /= 2;
        solution(r, c, size);
        solution(r + size, c, size);
        solution(r, c + size, size);
        solution(r + size, c + size, size);
    }

    static boolean check(int r, int c, int size) {

        int color = arr[r][c];

        for (int i = r; i < r + size; i++) {
            for (int j = c; j < c + size; j++) {
                if (arr[i][j] != color) {
                    return false;
                }
            }
        }

        return true;
    }
}