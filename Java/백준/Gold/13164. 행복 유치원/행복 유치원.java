import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static StringTokenizer st;
    public static void main(String[] args) throws Exception {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(bf.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] subArr = new int[N - 1];
        for (int i = 0; i < N-1; i++) {
            subArr[i] = arr[i+1] - arr[i];
        }

        Arrays.sort(subArr);
        int res = 0;
        for (int i = 0; i <= N - M - 1; i++) {
            res += subArr[i];
        }

        System.out.println(res);
    }
}