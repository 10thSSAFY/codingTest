import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int num = 0;
        int curr = 1;
        int cnt = 1;

        while (N > curr) {
            num += 6;
            curr += num;
            cnt++;
        }

        System.out.println(cnt);
    }
}