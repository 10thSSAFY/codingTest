import java.io.*;
import java.util.*;

public class Main {

    static int result;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        result = 0;
        for (int i = 0; i < N; i++) {
            String S = br.readLine();
            solution(S);
        }

        System.out.println(result);
    }

    public static void solution(String S) {
        Set<Character> set = new HashSet<>();
        char C = S.charAt(0);
        set.add(C);

        for (int i = 1; i < S.length(); i++) {
            char newC = S.charAt(i);
            if (newC == C) {
                continue;
            } else {
                if (!set.contains(newC)) {
                    set.add(newC);
                    C = newC;
                } else {
                    return;
                }
            }
        }

        result++;
    }
}