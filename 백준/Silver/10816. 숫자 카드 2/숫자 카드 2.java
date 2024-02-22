import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        for (int i = 0; i < N; i++) {
            int in = Integer.parseInt(st.nextToken());
            if (hash.get(in) == null) {
                hash.put(in, 1);
            } else {
                hash.put(in, hash.get(in) + 1);
            }
        }

        StringBuilder sb = new StringBuilder();
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int in = Integer.parseInt(st.nextToken());
            if (hash.get(in) == null) {
                sb.append(0).append(" ");
            } else {
                sb.append(hash.get(in)).append(" ");
            }
        }
        System.out.println(sb);
    }
}
