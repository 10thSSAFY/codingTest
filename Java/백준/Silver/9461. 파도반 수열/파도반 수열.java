import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[] lst = new long[101];
        lst[0] = 0;
        lst[1] = 1;
        lst[2] = 1;
        lst[3] = 1;
        lst[4] = 2;
        lst[5] = 2;

        for (int i = 6; i < 101; i++) {
            lst[i] = lst[i - 1] + lst[i - 5];
        }

        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            int N = Integer.parseInt(br.readLine());
            System.out.println(lst[N]);
        }
    }
}