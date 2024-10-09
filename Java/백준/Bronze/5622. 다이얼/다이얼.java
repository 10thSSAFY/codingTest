import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int cnt = 0;

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (ch == 'A' || ch == 'B' || ch == 'C') {
                cnt += 3;
            } else if (ch == 'D' || ch == 'E' || ch == 'F') {
                cnt += 4;
            } else if (ch == 'G' || ch == 'H' || ch == 'I') {
                cnt += 5;
            } else if (ch == 'J' || ch == 'K' || ch == 'L') {
                cnt += 6;
            } else if (ch == 'M' || ch == 'N' || ch == 'O') {
                cnt += 7;
            } else if (ch == 'P' || ch == 'Q' || ch == 'R' || ch == 'S') {
                cnt += 8;
            } else if (ch == 'T' || ch == 'U' || ch == 'V') {
                cnt += 9;
            } else if (ch == 'W' || ch == 'X' || ch == 'Y' || ch == 'Z') {
                cnt += 10;
            }
        }

        System.out.println(cnt);
    }
}
