import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] A = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);
        int x = Integer.parseInt(br.readLine());

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
        br.close();
    }
}