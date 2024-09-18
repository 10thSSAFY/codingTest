import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());

        int val = A * B * C;
        String str = String.valueOf(val);

        int arr[] = new int[10];
        for (int i = 0; i < str.length(); i++) {
            arr[str.charAt(i) - 48]++;
        }

        for (int v : arr) {
            System.out.println(v);
        }
    }
}