import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        scanner.close();

        int bagCount = 0;

        while (n >= 0) {
            if (n % 5 == 0) {
                bagCount += n / 5;
                System.out.println(bagCount);
                return;
            }
            bagCount++;
            n = n - 3;  // 3kg 봉지 하나 추가
        }

        // 정확히 나눌 수 없는 경우
        System.out.println(-1);
    }
}