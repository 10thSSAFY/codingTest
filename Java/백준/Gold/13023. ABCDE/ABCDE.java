import java.io.*;
import java.util.*;

public class Main {

    static ArrayList<Integer>[] arr;
    static boolean[] visited;
    static boolean result;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        arr = new ArrayList[N];
        visited = new boolean[N];
        for (int i = 0; i < N; i++) {
            arr[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b);
            arr[b].add(a);
        }

        for (int i = 0; i < N; i++) {
            DFS(i, 1);
            if (result) {
                break;
            }
        }

        System.out.println(result ? 1 : 0);
    }

    static void DFS(int now, int depth) {

        if (depth == 5 || result) {
            result = true;
            return;
        }

        visited[now] = true;
        for (int i : arr[now]) {
            if (!visited[i]) {
                DFS(i, depth + 1);
            }
        }
        visited[now] = false;
    }
}