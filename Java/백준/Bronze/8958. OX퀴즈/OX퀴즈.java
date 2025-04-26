import java.io.*;
import java.util.*;

public class Main {

    static int T, curr, score;
    static String S;
    
    public static void main(String []args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            S = br.readLine();
            curr = 0;
            score = 0;
            for (int j = 0; j < S.length(); j++) {
                if (S.charAt(j) == 'O') {
                    curr++;
                    score += curr;
                } else {
                    curr = 0;
                };
            };
            
            System.out.println(score);
        }
    }
}