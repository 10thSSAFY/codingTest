import java.io.*;
import java.util.*;

public class Main {

    static int N, distance, G, result;
    static int[] list;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        list = new int[N];

        for (int i = 0; i < N; i++) {
            list[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < N - 1; i++) {
            distance = list[i + 1] - list[i];
            G = gcd(distance, G);
        }

        result = (list[N - 1] - list[0]) / G + 1 - N;
        System.out.println(result);
    }

    static int gcd(int A, int B) {
        while (B != 0) {
            int R = A % B;
            A = B;
            B = R;
        }

        return A;
    }
}