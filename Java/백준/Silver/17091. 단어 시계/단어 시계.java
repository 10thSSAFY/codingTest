import java.io.*;
import java.util.*;

class Main {

    static int h, m;
    static String[] hs = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "one"};
    static String[] ms = {" o' clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
            "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        h = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        System.out.println(solution(h, m));
    }

    static String solution(int h, int m) {

        if (m == 0)
            return hs[h] + ms[m];
        else if (1 <= m && m <= 30) {
            if (m == 1)
                return ms[m] + " minute past " + hs[h];
            if (m != 15 && m != 30)
                return ms[m] + " minutes past " + hs[h];
            return ms[m] + " past " + hs[h];
        } else {
            m = 60 - m;
            if (m == 1)
                return ms[m] + " minute to " + hs[h + 1];
            if (m != 15)
                return ms[m] + " minutes to " + hs[h + 1];
            return ms[m] + " to " + hs[h + 1];
        }
    }
}
