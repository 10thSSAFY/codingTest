import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int result;
    static int[] price;
    static int[] weight;
    static int[] parkingLot;
    static Queue<Integer> queue;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        price = new int[N];
        for (int i = 0; i < N; i++) {
            price[i] = Integer.parseInt(br.readLine());
        }

        weight = new int[M + 1];
        for (int i = 1; i <= M; i++) {
            weight[i] = Integer.parseInt(br.readLine());
        }

        parkingLot = new int[N];
        queue = new LinkedList<>();
        for (int i = 0; i < M * 2; i++) {
            int n = Integer.parseInt(br.readLine());
            if (n > 0) {
                parkIn(n);
            } else {
                parkOut(-n);
            }
        }

        System.out.println(result);
    }

    static void parkIn(int n) {
        for (int i = 0; i < N; i++) {
            if (parkingLot[i] == 0) {
                parkingLot[i] = n;
                result += price[i] * weight[n];
                return;
            }
        }

        queue.add(n);
    }

    static void parkOut(int n) {
        for (int i = 0; i < N; i++) {
            if (parkingLot[i] == n) {
                parkingLot[i] = 0;
                if (!queue.isEmpty()) {
                    n = queue.poll();
                    parkIn(n);
                }
                return;
            }
        }
    }
}