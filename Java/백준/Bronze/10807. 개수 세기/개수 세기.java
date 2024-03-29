import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] lst = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++)
            lst[i] = Integer.parseInt(st.nextToken());

        int v = Integer.parseInt(br.readLine());
        int cnt = 0;
        for (int num : lst) {
            if (num == v)
                cnt++;
        }

        System.out.println(cnt);
    }
}