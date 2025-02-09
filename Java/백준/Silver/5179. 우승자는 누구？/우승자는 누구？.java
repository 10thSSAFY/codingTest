import java.io.*;
import java.util.*;

class Main {

    static int K, M, N, P, p, m, t, j;
    static StringTokenizer st;
    static boolean[][] solved;
    static int[][] failed, scores;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= K; tc++) {

            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            P = Integer.parseInt(st.nextToken());

            scores = new int[P + 1][2];
            solved = new boolean[P + 1][M];
            failed = new int[P + 1][M];
            for (int i = 0; i < N; i++) {

                st = new StringTokenizer(br.readLine());
                p = Integer.parseInt(st.nextToken());
                m = st.nextToken().charAt(0) - 'A';
                t = Integer.parseInt(st.nextToken());
                j = Integer.parseInt(st.nextToken());

                if (!solved[p][m]) {
                    if (j == 0) {
                        failed[p][m] += 1;
                    } else {
                        solved[p][m] = true;
                        scores[p][0] += 1;
                        scores[p][1] += t + (failed[p][m] * 20);
                    }
                }
            }

            PriorityQueue<Score> pq = new PriorityQueue<>();
            for (int i = 1; i <= P; i++) {
                pq.offer(new Score(i, scores[i][0], scores[i][1]));
            }

            System.out.println("Data Set " + tc + ":");
            while (!pq.isEmpty()) {
                Score curr = pq.poll();
                System.out.println(curr.identifier + " " + curr.solved + " " + curr.totalScore);
            }
            System.out.println();
        }
    }
}


class Score implements Comparable<Score> {

    int identifier;
    int solved;
    int totalScore;

    public Score(int identifier, int solved, int totalScore) {
        this.identifier = identifier;
        this.solved = solved;
        this.totalScore = totalScore;
    }

    @Override
    public int compareTo(Score o) {
        if (this.solved != o.solved) {
            return Integer.compare(o.solved, this.solved);
        }
        return Integer.compare(this.totalScore, o.totalScore);
    }
}
