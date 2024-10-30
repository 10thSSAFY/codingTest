import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();

        while (N > 0) {
            if (N % B < 10) {
                sb.append(N % B);
            } else {
                sb.append((char) ((N % B) + 55));
            }
            N /= B;
        }

        System.out.println(sb.reverse().toString());
    }
}