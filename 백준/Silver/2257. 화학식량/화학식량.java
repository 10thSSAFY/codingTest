import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] agrs) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        Stack<Integer> myStack = new Stack<>();
        int res = 0;

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == '(') {
                myStack.push(0);
            } else if (c == ')') {
                int temp = 0;
                while (true) {
                    int n = myStack.pop();
                    if (n == 0) break;
                    temp += n;
                }
                myStack.push(temp);
            } else if (49 < (int) c && (int) c <= 57) {
                int temp = myStack.pop();
                temp *= (int) c - '0';
                myStack.push(temp);
            } else {
                switch (c) {
                    case 'H':
                        myStack.push(1);
                        break;
                    case 'C':
                        myStack.push(12);
                        break;
                    case 'O':
                        myStack.push(16);
                        break;
                }
            }
        }

        while (!myStack.isEmpty()) {
            res += myStack.pop();
        }

        System.out.println(res);
    }
}