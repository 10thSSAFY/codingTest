import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static StringTokenizer st;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Queue<Integer> queue = new LinkedList<>();
        int maxSize = 0;
        int minQueue = 100001;
        int lastQueue = 100001;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int q = Integer.parseInt(st.nextToken());
            if (q == 1) {
                lastQueue = Integer.parseInt(st.nextToken());
                queue.add(lastQueue);
                if (queue.size() > maxSize) {
                    maxSize = queue.size();
                    minQueue = lastQueue;
                } else if (queue.size() == maxSize) {
                    minQueue = Math.min(lastQueue, minQueue);
                }
            } else {
                queue.poll();
            }
        }

        System.out.println(maxSize + " " + minQueue);
    }
}