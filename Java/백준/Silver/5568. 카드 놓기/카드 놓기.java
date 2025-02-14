import java.io.*;
import java.util.*;

class Main {

    static int n, k;
    static String[] arr;
    static boolean[] bit;
    static HashSet<String> hashSet;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine();
        }

        bit = new boolean[n];
        hashSet = new HashSet<>();

        solution(0, "");
        System.out.println(hashSet.size());
    }

    static void solution(int depth, String s) {

        if (depth == k) {
            hashSet.add(s);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!bit[i]) {
                bit[i] = true;
                solution(depth + 1, s + String.valueOf(arr[i]));
                bit[i] = false;
            }
        }
    }
}
