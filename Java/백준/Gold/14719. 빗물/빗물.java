import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[W];
        for (int i = 0; i < W; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int result = 0;
        for (int h = 0; h < H; h++) {
            boolean flag = false;
            int count = 0;
            for (int w = 0; w < W; w++) {
                if (arr[w] <= h) {
                    count++;
                } else if (flag){
                    result += count;
                    count = 0;
                } else {
                    flag = true;
                    count = 0;
                }
            }
        }
        System.out.println(result);
    }
}