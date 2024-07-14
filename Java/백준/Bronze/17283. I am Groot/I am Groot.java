import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(br.readLine());
        int R = Integer.parseInt(br.readLine());

        int total = 0;
        int branchLength = L;
        int branchNum = 1;
        while (branchLength * R / 100 > 5) {
            branchLength = branchLength * R / 100;
            branchNum *= 2;
            total += branchLength * branchNum;
        }

        System.out.println(total);
    }
}