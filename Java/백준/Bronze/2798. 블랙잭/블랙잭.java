import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static int[] cards;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 입력 처리
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        cards = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }
        br.close();

        // 가능한 조합 탐색
        int maxSum = 0;
        for (int i = 0; i < n - 2; i++) {  // 첫 번째 카드 선택
            for (int j = i + 1; j < n - 1; j++) {  // 두 번째 카드 선택
                for (int k = j + 1; k < n; k++) {  // 세 번째 카드 선택
                    int currentSum = cards[i] + cards[j] + cards[k];
                    if (currentSum <= m) {
                        maxSum = Math.max(maxSum, currentSum);
                    }
                }
            }
        }

        // 결과 출력
        System.out.println(maxSum);
    }
}
