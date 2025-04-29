import java.io.*;
import java.util.*;

public class Main {

    static int N, L;
    static int[] A;
    static StringTokenizer st;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(A);
        int currL = L;
        for (int i = 0; i < N; i++) {
            if (A[i] <= currL) {
                currL++;
            } else {
                break;
            }
        }

        System.out.println(currL);
    }
}