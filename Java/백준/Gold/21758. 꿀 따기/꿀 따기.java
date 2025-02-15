import java.io.*;
import java.util.*;

public class Main {

    static int N, result;
    static int[] arr, sum_arr;
    static boolean[] bit;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        sum_arr = new int[N + 1];
        for (int i = 1; i <= N; i++)
            sum_arr[i] = arr[i - 1] + sum_arr[i - 1];

        bit = new boolean[N + 1];
        solution(0, -1, -1, -1);

        System.out.println(result);
    }


    static void solution(int depth, int b1, int b2, int h) {

        if (depth == 3) {
            check(b1, b2, h);
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (!bit[i]) {
                bit[i] = true;
                if (depth == 0)
                    solution(1, i, b2, h);
                else if (depth == 1)
                    solution(2, b1, i, h);
                else
                    solution(3, b1, b2, i);
                bit[i] = false;
            }
        }
    }


    static void check(int b1, int b2, int h) {

        int tmp = 0;

        if (b1 < h) {
            tmp += sum_arr[h] - sum_arr[b1];
            if (b1 < b2 && b2 < h) {
                tmp -= arr[b2 - 1];
            }
        }

        if (b2 < h) {
            tmp += sum_arr[h] - sum_arr[b2];
            if (b2 < b1 && b1 < h) {
                tmp -= arr[b1 - 1];
            }
        }

        if (h < b1) {
            tmp += sum_arr[b1 - 1] - sum_arr[h - 1];
            if (h < b2 && b2 < b1) {
                tmp -= arr[b2 - 1];
            }
        }

        if (h < b2) {
            tmp += sum_arr[b2 - 1] - sum_arr[h - 1];
            if (h < b1 && b1 < b2) {
                tmp -= arr[b1 - 1];
            }
        }

        result = Math.max(result, tmp);
    }
}