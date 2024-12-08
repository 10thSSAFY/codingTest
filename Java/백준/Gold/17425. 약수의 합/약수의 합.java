import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        long[] fx = new long[1000001];
        long[] gx = new long[1000001];

        Arrays.fill(fx, 1);

        for (int i = 2; i < 1000001; i++) {
            for (int j = 1; i * j < 1000001; j++) {
                fx[i * j] += i;
            }
        }

        for (int i = 1; i < 1000001; i++) {
            gx[i] = gx[i - 1] + fx[i];
        }

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            sb.append(gx[Integer.parseInt(br.readLine())] + "\n");
        }

        System.out.println(sb);
    }
}