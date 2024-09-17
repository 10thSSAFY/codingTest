import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<Integer, String> map1 = new HashMap<>();
        Map<String, Integer> map2 = new HashMap<>();

        for (int i = 1; i <= N; i++) {
            String name = br.readLine();
            map1.put(i, name);
            map2.put(name, i);
        }

        for (int i = 0; i < M; i++) {
            String s = br.readLine();
            if (49 <= s.charAt(0) && s.charAt(0) <= 57) {
                sb.append(map1.get(Integer.parseInt(s))).append('\n');
            } else {
                sb.append(map2.get(s)).append('\n');
            }
        }

        System.out.println(sb);
    }
}