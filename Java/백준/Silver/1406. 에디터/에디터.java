import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String initialString = br.readLine();
        int M = Integer.parseInt(br.readLine());

        Stack<Character> leftStack = new Stack<>();
        Stack<Character> rightStack = new Stack<>();

        for (char c : initialString.toCharArray()) {
            leftStack.push(c);
        }

        for (int i = 0; i < M; i++) {
            String command = br.readLine();

            if (command.equals("L")) {  // 커서 왼쪽 이동
                if (!leftStack.isEmpty()) {
                    rightStack.push(leftStack.pop());
                }
            } else if (command.equals("D")) {  // 커서 오른쪽 이동
                if (!rightStack.isEmpty()) {
                    leftStack.push(rightStack.pop());
                }
            } else if (command.equals("B")) {  // 커서 왼쪽 문자 삭제
                if (!leftStack.isEmpty()) {
                    leftStack.pop();
                }
            } else if (command.startsWith("P")) {  // 문자 삽입
                char c = command.split(" ")[1].charAt(0);
                leftStack.push(c);
            }
        }

        for (char c : leftStack) {
            bw.write(c);
        }
        while (!rightStack.isEmpty()) {
            bw.write(rightStack.pop());
        }

        bw.flush();
        bw.close();
    }
}
