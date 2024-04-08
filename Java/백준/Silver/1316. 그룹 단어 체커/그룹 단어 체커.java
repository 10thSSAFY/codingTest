import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        char tmp = '?';
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            int len = word.length();
            HashSet<Character> chars = new HashSet<>();
            boolean res = true;
            for (int j = 0; j < len; j++) {
                Character newChar = word.charAt(j);
                if (!chars.contains(newChar)) {
                    chars.add(newChar);
                    tmp = newChar;
                    continue;
                } else if (tmp == newChar) {
                    continue;
                } else {
                    res = false;
                    break;
                }
            }
            if (res) {
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}