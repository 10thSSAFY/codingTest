import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        ArrayList<BigInteger> arrayList = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String S = br.readLine();
            BigInteger num = new BigInteger("0");
            BigInteger mul = new BigInteger("10");
            boolean flag = false;
            for (int j = 0; j < S.length(); j++) {
                if ('0' <= S.charAt(j) && S.charAt(j) <= '9') {
                    num = mul.multiply(num).add(BigInteger.valueOf(S.charAt(j) - '0'));
                    flag = true;
                } else if (flag) {
                    arrayList.add(num);
                    num = new BigInteger("0");
                    flag = false;
                }
            }

            if (flag) {
                arrayList.add(num);
            }
        }

        Collections.sort(arrayList);

        StringBuilder sb = new StringBuilder();
        for (BigInteger n : arrayList) {
            sb.append(n).append('\n');
        }

        System.out.println(sb);
    }
}