import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] token = br.readLine().split(" ");
        int n = Integer.parseInt(token[0]);
        int m = Integer.parseInt(token[1]);

        if (m == 0) {
            bw.write("0");
            bw.close();
            return;
        }

        int[] list = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(list);

        int answer = Integer.MAX_VALUE;
        int left = 0, right = 0;

        while (right < n) {
            int diff = list[right] - list[left];
            if (diff >= m) {
                answer = Math.min(answer, diff);
                left++;
            } else {
                right++;
            }
        }

        bw.write(String.valueOf(answer));
        br.close();
        bw.close();
    }
}