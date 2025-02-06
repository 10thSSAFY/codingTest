import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static int[][] arr;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            String S = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = S.charAt(j) - '0';
            }
        }

        int minLength = Math.min(N, M);

        for (int l = minLength; l >= 2; l--) {
            for (int r = 0; r <= N - l; r++) {
                for (int c = 0; c <= M - l; c++) {
                    int num = arr[r][c];
                    if (arr[r][c + l - 1] == num && arr[r + l - 1][c] == num && arr[r + l - 1][c + l - 1] == num) {
                        System.out.println(l * l);
                        return;
                    }
                }
            }
        }

        System.out.println(1);
    }
}
