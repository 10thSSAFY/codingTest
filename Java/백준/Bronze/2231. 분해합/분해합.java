import java.io.*;
import java.util.*;

public class Main {

    // 자릿수의 합을 계산하는 함수
    private static int digitSum(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int result = 0;

        for (int i = Math.max(1, N - String.valueOf(N).length() * 9); i < N; i++) {
            int decompositionSum = i + digitSum(i);  // 분해합 계산
            if (decompositionSum == N) {
                result = i;
                break;
            }
        }

        System.out.println(result);
    }
}