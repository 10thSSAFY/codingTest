import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int cnt = 0;
        int newNum = N;

        while (true) {
            newNum = ((newNum % 10) * 10) + (((newNum / 10) + (newNum % 10)) % 10);
            cnt++;

            if (N == newNum) break;
        }

        System.out.println(cnt);
    }
}