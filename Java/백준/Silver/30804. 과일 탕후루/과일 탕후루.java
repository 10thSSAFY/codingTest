import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[] A;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        A = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++)
            A[i] = Integer.parseInt(st.nextToken());

        HashMap<Integer, Integer> hashMap = new HashMap<>();
        int result = 0;
        int left = 0;

        for (int i = 0; i < N; i++) {
            hashMap.put(A[i], hashMap.getOrDefault(A[i], 0) + 1);

            while (hashMap.size() > 2) {
                hashMap.put(A[left], hashMap.get(A[left]) - 1);

                if (hashMap.get(A[left]) == 0) {
                    hashMap.remove(A[left]);
                }

                left++;
            }
            result = Math.max(result, i - left + 1);
        }
        System.out.println(result);
    }
}