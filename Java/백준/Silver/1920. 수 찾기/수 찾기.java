import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static int[] arr, queries;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        M = Integer.parseInt(br.readLine());
        queries = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(arr);

        for (int query : queries) {
            if (binarySearch(arr, query)) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }

    public static boolean binarySearch(int[] arr, int target) {

        int left = 0, right = arr.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] == target) {
                return true;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}