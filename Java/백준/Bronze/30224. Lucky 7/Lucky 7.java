import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String number = br.readLine();

        int result = 0;
        if (number.contains("7")) {
            result += 2;
        }
        if (Integer.parseInt(number) % 7 == 0) {
            result += 1;
        }

        System.out.println(result);
    }
}