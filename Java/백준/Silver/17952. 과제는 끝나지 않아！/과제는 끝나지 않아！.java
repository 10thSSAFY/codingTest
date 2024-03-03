import java.io.IOException;
import java.util.Stack;

public class Main {

    private static int totalScore = 0;
    private static Stack<Assignment> myStack;
    static class Assignment {

        private final int score;
        private final int time;

        public Assignment(int score, int time) {
            this.score = score;
            this.time = time;
        }
    }

    public static void main(String[] args) throws IOException {

        int N = readInt();
        myStack = new Stack<>();

        for (int i = 0; i < N; i++) {
            int check = readInt();

            if (check == 0) {
                if (myStack.isEmpty()) continue;

                Assignment current = myStack.pop();
                checkTime(current);
            } else {
                int score = readInt();
                int time = readInt();

                checkTime(new Assignment(score, time));
            }
        }
        System.out.println(totalScore);
    }

    private static void checkTime(Assignment assignment) {

        int score = assignment.score;
        int time = assignment.time;

        if (time == 1) {
            totalScore += score;
        } else {
            myStack.push(new Assignment(score, time - 1));
        }
    }

    private static int readInt() throws IOException {
        int n = System.in.read() - '0';
        int c = System.in.read();
        while (c > ' ') {
            n = 10 * n + c - '0';
            c = System.in.read();
        }
        if (c == '\r') {
            System.in.read();
        }
        return n;
    }
}