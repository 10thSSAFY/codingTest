import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int last = -1;
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            switch (s) {
                case "push":
                    int n = Integer.parseInt(st.nextToken());
                    last = n;
                    queue.add(n);
                    break;
                case "pop":
                    if (!queue.isEmpty()) {
                        System.out.println(queue.poll());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case "size":
                    System.out.println(queue.size());
                    break;
                case "empty":
                    if (queue.isEmpty()) {
                        System.out.println(1);
                    } else {
                        System.out.println(0);
                    }
                    break;
                case "front":
                    if (!queue.isEmpty()) {
                        System.out.println(queue.peek());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case "back":
                    if (!queue.isEmpty()) {
                        System.out.println(last);
                    } else {
                        System.out.println(-1);
                    }
                    break;
            }
        }
    }
}