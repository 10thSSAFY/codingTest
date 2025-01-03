import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            int N = Integer.parseInt(br.readLine());
            String result = "";
            int maxNum = 0;
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String name = st.nextToken();
                int num = Integer.parseInt(st.nextToken());
                if (num > maxNum) {
                    maxNum = num;
                    result = name;
                }
            }
            System.out.println(result);
        }
    }
}