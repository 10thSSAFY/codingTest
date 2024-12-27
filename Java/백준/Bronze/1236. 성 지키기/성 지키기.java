import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        char[][] arr = new char[N][M];
        for (int r = 0; r < N; r++) {
            String line = br.readLine();
            for (int c = 0; c < M; c++) {
                arr[r][c] = line.charAt(c);
            }
        }

        int cntN = N;
        int cntM = M;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (arr[r][c] == 'X') {
                    cntN -= 1;
                    break;
                }
            }
        }

        for (int c = 0; c < M; c++) {
            for (int r = 0; r < N; r++) {
                if (arr[r][c] == 'X') {
                    cntM -= 1;
                    break;
                }
            }
        }

        System.out.println(Math.max(cntN, cntM));
    }
}