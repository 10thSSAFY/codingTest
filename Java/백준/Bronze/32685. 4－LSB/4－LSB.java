import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String num1 = toBinary(Integer.parseInt(br.readLine()));
        String num2 = toBinary(Integer.parseInt(br.readLine()));
        String num3 = toBinary(Integer.parseInt(br.readLine()));

        int toDecimal = Integer.parseInt(num1 + num2 + num3, 2);
        String result = String.format("%04d", toDecimal);

        System.out.println(result);
    }

    static String toBinary(int num) {

        String binaryString = Integer.toBinaryString(num);
        if (binaryString.length() > 4) {
            binaryString = binaryString.substring(binaryString.length() - 4);
        } else {
            binaryString = String.format("%04d", Integer.parseInt(binaryString));
        }

        return binaryString;
    }
}