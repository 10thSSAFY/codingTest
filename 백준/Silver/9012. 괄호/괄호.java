import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] agrs) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            Stack<Character> myStack = new Stack<>();
            boolean res = true;
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                if (c == '(') {
                    myStack.push(c);
                } else {
                    if (myStack.isEmpty()) {
                        System.out.println("NO");
                        res = false;
                        break;
                    }
                    char cp = myStack.pop();
                    if (cp == ')') {
                        System.out.println("NO");
                        res = false;
                        break;
                    }
                }
            }
            if (res) {
                if (!myStack.isEmpty()) {
                    System.out.println("NO");
                } else {
                    System.out.println("YES");
                }
            }
        }
    }
}