import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<String> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            String text = br.readLine();
            String[] temp = text.split(" ");
            for (int j = 0; j < temp.length; j++) {
                stack.push(temp[j]);
            }
            sb.append("Case #" + i + ": ");
            for (int k = 0; k < temp.length; k++) {
                sb.append(stack.pop()).append(" ");
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}