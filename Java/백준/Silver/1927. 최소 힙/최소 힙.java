import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if (priorityQueue.isEmpty()) {
                    sb.append(0).append('\n');
                } else {
                    sb.append(priorityQueue.poll()).append('\n');
                }
            } else {
                priorityQueue.add(x);
            }
        }
        System.out.println(sb);
    }
}