import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringBuilder sb = new StringBuilder();
        boolean flag = false;
        Stack<Character> myStack = new Stack<>();

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '<') {
                while (!myStack.isEmpty()) {
                    sb.append(myStack.pop());
                }
                flag = true;
            } else if (str.charAt(i) == '>') {
                flag = false;
                sb.append(str.charAt(i));
                continue;
            }

            if (flag) {
                sb.append(str.charAt(i));
            } else {
                if (str.charAt(i) == ' ') {
                    while (!myStack.isEmpty()) {
                        sb.append(myStack.pop());
                    }
                    sb.append(' ');
                    continue;
                } else {
                    myStack.push(str.charAt(i));
                }
            }

            if (i == str.length() - 1) {
                while (!myStack.isEmpty()) {
                    sb.append(myStack.pop());
                }
            }
        }

        System.out.println(sb);
    }
}
