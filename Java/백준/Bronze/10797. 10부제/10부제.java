import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int result = 0;
        for (int i = 0; i < 5; i++) {
            if (N == Integer.parseInt(st.nextToken())) {
                result++;
            }
        }

        System.out.println(result);
    }
}