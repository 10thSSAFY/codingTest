import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        solution(1, 0, "");
    }

    static void solution(int num, int depth, String result) {
        if (depth == M) {
            System.out.println(result.trim());
            return;
        }

        for (int i = num; i <= N; i++) {
            solution(i, depth + 1, result + " " + Integer.toString(i));
        }
    }
}