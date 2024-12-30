import java.io.*;
import java.util.*;

public class Main {

    static long result;
    static long[] list;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());

            list = new long[l];
            for (int i = 0; i < l; i++) {
                list[i] = Long.parseLong(st.nextToken());
            }

            result = 0;
            solution(l);

            System.out.println(result);
        }
    }

    static void solution(int l) {
        for (int i = 0; i < l - 1; i++) {
            for (int j = i + 1; j < l; j++) {
                gcd(list[i], list[j]);
            }
        }
    }

    static void gcd(long a, long b) {
        long n;
        while (b != 0) {
            n = a % b;
            a = b;
            b = n;
        }

        result += a;
    }
}