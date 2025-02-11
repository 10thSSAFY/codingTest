import java.io.*;
import java.util.*;

public class Main {

    static int K;
    static int[] num;
    static ArrayList<Integer>[] tree;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        K = Integer.parseInt(br.readLine());

        num = new int[(int) Math.pow(2, K)];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int index = 1;
        while (st.hasMoreTokens())
            num[index++] = Integer.parseInt(st.nextToken());

        tree = new ArrayList[K + 1];
        for (int i = 0; i <= K; i++)
            tree[i] = new ArrayList<>();

        solution(1, 1, (int) (Math.pow(2, K) - 1));

        for (int i = 1; i <= K; i++) {
            for (int j = 0; j < tree[i].size(); j++)
                bw.write(tree[i].get(j) + " ");
            bw.newLine();
        }

        bw.flush();
        bw.close();
        br.close();
    }

    static void solution(int depth, int start, int end) {

        int mid = (start + end) / 2;
        tree[depth].add(num[mid]);

        if (depth == K)
            return;

        solution(depth + 1, start, mid - 1);
        solution(depth + 1, mid + 1, end);
    }
}
