import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();

        long totalSum = 0;
        long currentNumber = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {  // 숫자인 경우
                currentNumber = currentNumber * 10 + (c - '0');  // 숫자 조합(확장)
            } else {
                totalSum += currentNumber;
                currentNumber = 0;
            }
        }

        totalSum += currentNumber;

        System.out.println(totalSum);

        br.close();
    }
}
