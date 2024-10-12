import java.io.*;
import java.util.*;


public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int D = gcd(A, B);

        System.out.println(D);
        System.out.println(A * B / D);
    }

    public static int gcd(int A, int B) {

        while (B != 0) {
            int r = A % B;

            A = B;
            B = r;
        }

        return A;
    }
}