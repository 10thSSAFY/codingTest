import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String S = br.readLine();

        int[] lst = new int[N];
        for (int i = 0; i < N; i++) {
            lst[i] = Integer.parseInt(br.readLine());
        }

        Stack<Double> stack = new Stack<>();
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            if ('A' <= c && c <= 'Z') {
                double d = lst[c - 'A'];
                stack.push(d);
            } else {
                double s2 = stack.pop();
                double s1 = stack.pop();
                double s3 = 0.0;
                if (c == '+') {
                    s3 = s1 + s2;
                } else if (c == '-') {
                    s3 = s1 - s2;
                } else if (c == '*') {
                    s3 = s1 * s2;
                } else if (c == '/') {
                    s3 = s1 / s2;
                }

                stack.push(s3);
            }
        }
        System.out.printf("%.2f", stack.pop());
    }
}