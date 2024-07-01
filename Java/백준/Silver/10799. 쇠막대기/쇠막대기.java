import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        Stack<Character> stack = new Stack<>();

        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push('(');
            } else if (s.charAt(i) == ')') {
                if (s.charAt(i - 1) == '(') {
                    stack.pop();
                    result += stack.size();
                } else if (s.charAt(i - 1) == ')') {
                    result += 1;
                    stack.pop();
                }
            }
        }
        System.out.println(result);
    }
}
