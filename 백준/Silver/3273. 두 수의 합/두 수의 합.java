import java.io.IOException;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {

        int n = readInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = readInt();
        }
        Arrays.sort(A);
        int x = readInt();

        int cnt = 0;
        int start = 0;
        int end = n - 1;
        while (start < end) {
            if (A[start] + A[end] < x) {
                start++;
            } else if (A[start] + A[end] > x) {
                end--;
            } else {
                cnt++;
                start++;
                end--;
            }
        }
        System.out.println(cnt);
    }

    private static int readInt() throws IOException {
        int c;
        int n = System.in.read() - '0';
        c = System.in.read();
        while (c > ' ') {
            n = 10 * n + c - '0';
            c = System.in.read();
        }
        if (c == '\r') {
            System.in.read();
        }
        return n;
    }
}