import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    private static int totalScore = 0;
    private static Stack<Assignment> myStack;
    static class Assignment {

        private int score;
        private int time;

        public Assignment(int score, int time) {
            this.score = score;
            this.time = time;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        myStack = new Stack<>();
        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int check = Integer.parseInt(st.nextToken());

            if (check == 0) {
                if (myStack.isEmpty()) continue;

                Assignment current = myStack.pop();
                checkTime(current);
            } else {
                int score = Integer.parseInt(st.nextToken());
                int time = Integer.parseInt(st.nextToken());

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
}