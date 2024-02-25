import java.io.*;
import java.util.*;

public class Main {
    private static int[] solve(int N, int L, int[] A) {
        int[] result = new int[N];

        Deque<Integer> deque = new LinkedList<>();

        for (int i = 0; i < N; ++i) {
            while (!deque.isEmpty() && deque.peekFirst() < i - L + 1) {
                deque.pollFirst();
            }

            while (!deque.isEmpty() && A[deque.peekLast()] > A[i]) {
                deque.pollLast();
            }

            deque.offerLast(i);

            result[i] = A[deque.peekFirst()];
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(in.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int[] A = new int[N];

        st = new StringTokenizer(in.readLine());

        for (int i = 0; i < N; ++i) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int[] result = solve(N, L, A);

        for (int number : result) {
            out.write(number + " ");
        }
        out.write('\n');

        in.close();
        out.close();
    }
}