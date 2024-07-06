import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Integer> s = new Stack<>();

        int now = 1;

        for (int i = 0; i < n; i++) {
            if (arr[i] == now) {
                now++;
                while (!s.isEmpty()) {
                    if (s.peek() == now) {
                        s.pop();
                        now++;
                    } else {
                        break;
                    }
                }
            } else {
                s.push(arr[i]);
            }
        }

        System.out.println(s.isEmpty() ? "Nice" : "Sad");
    }
}