import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String[] before = {"apa", "epe", "ipi", "opo", "upu"};
        String[] after = {"a", "e", "i", "o", "u"};
        for (int i = 0; i < 5; i++) {
            str = str.replaceAll(before[i], after[i]);
        }
        System.out.println(str);
    }
}