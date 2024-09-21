import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] numbers = br.readLine().split(":");
        int N = Integer.parseInt(numbers[0]);
        int M = Integer.parseInt(numbers[1]);

        int gcd = Gcd(Math.max(N, M), Math.min(N, M));
        System.out.println(N / gcd + ":" + M / gcd);
    }

    public static int Gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return Gcd(b, a % b);
    }
}