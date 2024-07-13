import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static StringTokenizer st;
    static boolean[] visited;
    static int max = 0;
    static ArrayList<Integer[]> graph[];
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        graph = new ArrayList[n + 1];

        for (int i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph[node1].add(new Integer[]{node2, cost});
            graph[node2].add(new Integer[]{node1, cost});
        }

        visited = new boolean[n + 1];
        for (int i = 1; i < n + 1; i++) {
            Arrays.fill(visited, false);
            dfs(i, 0);
        }

        System.out.println(max);
    }

    public static void dfs(int node, int sum) {
        visited[node] = true;
        max = Math.max(sum, max);

        for (Integer[] temp : graph[node]) {
            int next = temp[0];
            int cost = temp[1];
            if (!visited[next]) {
                dfs(next, sum + cost);
            }
        }
    }
}
