import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int target = Integer.parseInt(st.nextToken());
            System.out.println(findMinSteps(start, target));
        }
    }

    public static String findMinSteps(int start, int target) {

        Map<Integer, Integer> visited = new HashMap<>();
        Queue<Integer> q = new LinkedList<>();

        visited.put(start, 0);
        q.offer(start);

        while (!q.isEmpty()) {
            int curr = q.poll();

            if (curr == target) {
                return String.valueOf(visited.get(curr));
            }

            String currStr = String.valueOf(curr);
            for (int i = 0; i < 4; i++) {
                String prefix = currStr.substring(0, i);
                String suffix = currStr.substring(i + 1);

                for (int j = 0; j < 10; j++) {
                    if (i == 0 && j == 0) continue;
                    if (j == Character.getNumericValue(currStr.charAt(i))) continue;

                    int nextNum = Integer.parseInt(prefix + j + suffix);
                    if (isPrime(nextNum) && !visited.containsKey(nextNum)) {
                        visited.put(nextNum, visited.get(curr) + 1);
                        q.offer(nextNum);
                    }
                }
            }
        }

        return "Impossible";
    }

    public static boolean isPrime(int n) {

        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
