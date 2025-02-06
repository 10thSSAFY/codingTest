import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int[] arr, result;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        result = new int[M];
        dfs(0, 0);
        System.out.println(sb);
    }

    static void dfs(int start, int depth) {
        if(depth == M) {
            for(int i = 0; i < M; i++) {
                sb.append(result[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        int standard = -1;
        for(int i = start; i < N; i++) {
            int now = arr[i];
            if(standard != now) {
                standard = now;
                result[depth] = arr[i];
                dfs(i, depth + 1);
            }
        }
    }
}
