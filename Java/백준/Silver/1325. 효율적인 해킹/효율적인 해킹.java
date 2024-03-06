import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    static int cnt, max = -1;
    static boolean[] visited;
    static ArrayList<ArrayList<Integer>> list;
    public static void main(String[] args) throws IOException {

        StringBuilder sb = new StringBuilder();

        int N = readInt();
        int M = readInt();

        list = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            list.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            int a = readInt();
            int b = readInt();
            list.get(b).add(a);
        }

        int[] result = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            visited = new boolean[N + 1];
            cnt = 0;
            bfs(i);
            result[i] = cnt;
            max = Math.max(cnt, max);
        }

        for (int i = 1; i <= N; i++) {
            if (result[i] == max) {
                sb.append(i + " ");
            }
        }

        System.out.println(sb);
    }

    private static void bfs(int n) {
        Queue<Integer> q = new LinkedList<>();
        q.add(n);
        visited[n] = true;
        while (!q.isEmpty()) {
            int nn = q.poll();
            for (int i : list.get(nn)) {
                if (!visited[i]) {
                    q.add(i);
                    visited[i] = true;
                    cnt++;
                }
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