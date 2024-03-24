import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int i = 1;
        int num = 0;
        while (i <= N) {
            num += i++;
        }

        System.out.println(num);
    }
}