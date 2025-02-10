import java.io.*;
import java.util.*;

public class Main {

    static int N, K;
    static int[] sensors;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());
        sensors = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(sensors);

        System.out.println(solution());
    }


    public static int solution() {

        ArrayList<Integer> distances = new ArrayList<>();
        for (int i = 1; i < N; i++) {
            distances.add(sensors[i] - sensors[i-1]);
        }
        Collections.sort(distances);

        int result = sensors[N - 1] - sensors[0];
        for (int i = 0; i < Math.min(K - 1, N - 1); i++) {
            result -= distances.get(distances.size() - i - 1);
        }

        return Math.max(0, result);
    }
}
