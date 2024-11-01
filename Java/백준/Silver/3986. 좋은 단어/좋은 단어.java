import java.io.*;
import java.util.*;

public class Main {

    static int result;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String S = br.readLine();
            solution(S);
        }

        System.out.println(result);
    }

    static void solution(String S) {

        if (S.length() % 2 == 1) {
            return;
        }

        Stack<Character> stack = new Stack<>();
        stack.push(S.charAt(0));
        for (int i = 1; i < S.length(); i++) {
            if (!stack.isEmpty() && stack.peek() == S.charAt(i)) {
                stack.pop();
            } else {
                stack.push(S.charAt(i));
            }
        }

        if (stack.isEmpty()) {
            result++;
        }
    }
}