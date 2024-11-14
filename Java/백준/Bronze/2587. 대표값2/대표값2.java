import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;
        int mid = 0;
        int[] arr = new int[5];
        for (int i = 0; i < 5; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[i] = num;
            sum += num;
        }
        Arrays.sort(arr);
        
        int avg = sum / 5;
        mid = arr[2];
        System.out.println(avg);
        System.out.println(mid);
    }
}