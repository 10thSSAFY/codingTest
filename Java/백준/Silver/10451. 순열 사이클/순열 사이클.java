import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    static StringTokenizer st;
    static int cnt;
    static Stack<Integer> stack = new Stack<>();
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {

            int N = Integer.parseInt(br.readLine());

            int[] arr = new int[N + 1];
            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            cnt = 0;
            for (int i = 1; i <= N; i++) {
                if (arr[i] != 0) {
                    cnt ++;
                    find(i, arr);
                }
            }

            System.out.println(cnt);
        }
    }

    public static void find(int num, int arr[]) {

        stack.push(arr[num]);
        arr[num] = 0;
        while (!stack.isEmpty()) {
            int idx = stack.pop();
            if (arr[idx] != 0) {
                stack.push(arr[idx]);
                arr[idx] = 0;
            }
        }
    }
}