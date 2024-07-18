import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Queue<Integer> queue = new LinkedList<>();
        int size = 0;

        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == -1) {
                break;
            } else if (n == 0) {
                queue.poll();
                size--;
            } else if (N > size) {
                queue.add(n);
                size++;
            }
        }

        if (!queue.isEmpty()) {
            for (int i = 0; i < size; i++) {
                int q = queue.poll();
                System.out.print(q + " ");
            }
        } else {
            System.out.println("empty");
        }
    }
}