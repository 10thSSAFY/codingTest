import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < n; tc++) {
            HashMap<String, Integer> hm = new HashMap<>();
            int N = Integer.parseInt(br.readLine());
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String cloth = st.nextToken();
                String kind = st.nextToken();

                if (hm.containsKey(kind)) {
                    hm.put(kind, hm.get(kind) + 1);
                } else {
                    hm.put(kind, 1);
                }
            }

            int result = 1;
            for (int v : hm.values()) {
                result *= v + 1;
            }

            sb.append(result - 1).append('\n');
        }
        System.out.println(sb);
    }
}