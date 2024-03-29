import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] lst = new int[N + 1];
        for (int i = 1; i < N + 1; i++)
            lst[i] = i;

        for (int r = 0; r < M; r++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int a = lst[i];
            int b = lst[j];
            lst[i] = b;
            lst[j] = a;
        }

        for (int i = 1; i <= N; i++) {
            System.out.print(lst[i] + " ");
        }
    }
}