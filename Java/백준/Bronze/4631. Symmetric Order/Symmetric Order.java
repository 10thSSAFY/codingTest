import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int cnt = 0;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;

            String[] arr = new String[n];
            for (int i = 0; i < n; i++) {
                if (i % 2 == 0)
                    arr[i / 2] = br.readLine();
                else
                    arr[n - 1 - i / 2] = br.readLine();
            }

            System.out.println("SET" + " " + ++cnt);
            for (int i = 0; i < n; i++)
                System.out.println(arr[i]);
        }
    }
}
