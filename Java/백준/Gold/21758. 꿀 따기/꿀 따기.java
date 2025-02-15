import java.io.*;
import java.util.*;

public class Main {

    static int N, result;
    static int[] arr, sum_arr;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        sum_arr = new int[N + 1];
        for (int i = 1; i <= N; i++)
            sum_arr[i] = arr[i - 1] + sum_arr[i - 1];

        case1();
        case2();
        case3();

        System.out.println(result);
    }

    static void case1() {
        int tmp = sum_arr[N] - sum_arr[1];
        for (int i = 2; i < N; i++) {
            int res = tmp - arr[i - 1] + sum_arr[N] - sum_arr[i];
            result = Math.max(result, res);
        }
    }

    static void case2() {
        for (int i = 2; i < N; i++) {
            int res = sum_arr[i] - sum_arr[1] + sum_arr[N - 1] - sum_arr[i - 1];
            result = Math.max(result, res);
        }
    }

    static void case3() {
        int tmp = sum_arr[N - 1];
        for (int i = 2; i < N; i++) {
            int res = tmp - arr[i - 1] + sum_arr[i - 1];
            result = Math.max(result, res);
        }
    }
}