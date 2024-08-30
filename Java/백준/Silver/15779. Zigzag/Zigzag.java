import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int result = 2;
        int cnt = 2;
        for (int i = 0; i < N - 2; i++) {
            if (arr[i] <= arr[i + 1] && arr[i + 1] <= arr[i + 2]) {
                cnt = 2;
            } else if (arr[i] >= arr[i + 1] && arr[i + 1] >= arr[i + 2]) {
                cnt = 2;
            } else {
                cnt += 1;
            }

            result = Math.max(result, cnt);
        }

        System.out.println(result);
    }
}