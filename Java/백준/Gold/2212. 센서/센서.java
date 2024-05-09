import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            list.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(list);

        ArrayList<Integer> subList = new ArrayList<>();
        for (int i = 1; i < N; i++) {
            subList.add(list.get(i) - list.get(i - 1));
        }
        Collections.sort(subList);

        int result = Solution(subList, N, M);
        System.out.println(result);
    }

    private static int Solution(ArrayList<Integer> subList, int N, int M) {
        if (N <= M) {
            return 0;
        }
        for (int i = 2; i <= M; i++) {
            subList.remove(N - i);
        }
        int result = 0;
        for (int r : subList) {
            result += r;
        }
        return result;
    }
}