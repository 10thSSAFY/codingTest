import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static StringTokenizer st;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        int[] CList = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            CList[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < M; i++) {
            int K = Integer.parseInt(br.readLine());
            if (K < N) {
                System.out.println(CList[K]);
            } else {
                System.out.println(CList[(K - (V - 1)) % (N - V + 1) + (V - 1)]);
            }
        }
    }
}