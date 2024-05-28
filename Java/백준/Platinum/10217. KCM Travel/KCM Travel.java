import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            List<List<int[]>> graph = new ArrayList<>();
            for (int i = 0; i <= N; i++) {
                graph.add(new ArrayList<>());
            }

            int[][] knapsack = new int[N + 1][M + 1];
            for (int i = 0; i <= N; i++) {
                Arrays.fill(knapsack[i], Integer.MAX_VALUE);
            }

            if (M == 0) {
                sb.append("Poor KCM").append('\n');
                continue;
            }

            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                int d = Integer.parseInt(st.nextToken());
                graph.get(u).add(new int[]{v, c, d});
            }

            knapsack[1][0] = 0;
            Deque<int[]> q = new ArrayDeque<>();
            q.add(new int[]{1, 0, 0});

            while (!q.isEmpty()) {
                int[] current = q.poll();
                int city = current[0];
                int cost = current[1];
                int time = current[2];

                if (time > knapsack[city][cost]) {
                    continue;
                }

                for (int[] edge : graph.get(city)) {
                    int newCity = edge[0];
                    int newCost = edge[1];
                    int newTime = edge[2];
                    int calCost = cost + newCost;
                    int calTime = time + newTime;

                    if (calCost <= M && calTime < knapsack[newCity][calCost]) {
                        for (int nCost = calCost; nCost <= M; nCost++) {
                            if (calTime < knapsack[newCity][nCost]) {
                                knapsack[newCity][nCost] = calTime;
                            } else {
                                break;
                            }
                        }
                        q.add(new int[]{newCity, calCost, calTime});
                    }
                }
            }

            int result = Integer.MAX_VALUE;
            for (int i = 0; i <= M; i++) {
                result = Math.min(result, knapsack[N][i]);
            }

            sb.append(result == Integer.MAX_VALUE ? "Poor KCM" : result).append('\n');
        }

        System.out.print(sb.toString());
    }
}
