import java.io.IOException;
import java.util.ArrayList;

public class Main {

    static boolean[] visited;
    static ArrayList<Integer>[] list;
    static int[] arr;
    public static void main(String[] args) throws IOException {

        int N = readInt();
        int M = readInt();

        list = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            list[i] = new ArrayList<>();
        }

        arr = new int[N + 1];
        for (int i = 0; i < M; i++) {
            int a = readInt();
            int b = readInt();
            list[a].add(b);
        }

        for (int i = 1; i <= N; i++) {
            visited = new boolean[N + 1];
            visited[i] = true;
            dfs(i);
        }

        int max = 0;
        for (int i = 1; i <= N; i++) {
            max = Math.max(arr[i], max);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            if (arr[i] == max) {
                sb.append(i + " ");
            }
        }
        System.out.println(sb);
    }

    private static void dfs(int n) {
        for (int lst : list[n]) {
            if (!visited[lst]) {
                arr[lst]++;
                visited[lst] = true;
                dfs(lst);
            }
        }
    }

    private static int readInt() throws IOException {
        int n = System.in.read() - '0';
        int c = System.in.read();
        while (c > ' ') {
            n = 10 * n + c - '0';
            c = System.in.read();
        }
        if (c == '\r') {
            System.in.read();
        }
        return n;
    }
}