import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int dist = b - a;
            int result = (int) Math.sqrt(dist);

            if (result == Math.sqrt(dist)) {
                System.out.println(result * 2 - 1);
            } else if (dist <= result * result + result) {
                System.out.println(result * 2);
            } else {
                System.out.println(result * 2 + 1);
            }
        }
    }
}