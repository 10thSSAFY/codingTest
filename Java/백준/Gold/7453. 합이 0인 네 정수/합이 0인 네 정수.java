import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int n, abPoint, cdPoint;
    static long abValue, cdValue, result, cnt, cntX, cntY;
    static int[][] arr;
    static int[] AB, CD;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());

        arr = new int[n][4];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        AB = new int[n * n];
        CD = new int[n * n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                AB[i * n + j] = arr[i][0] + arr[j][1];
                CD[i * n + j] = arr[i][2] + arr[j][3];
            }
        }

        Arrays.sort(AB);
        Arrays.sort(CD);
        abPoint = 0;
        cdPoint = n * n - 1;
        cnt = 0;
        while (abPoint < n * n && cdPoint > -1) {
            abValue = AB[abPoint];
            cdValue = CD[cdPoint];
            result = abValue + cdValue;

            if (result < 0) {
                abPoint += 1;
            } else if (result > 0) {
                cdPoint -= 1;
            } else {
                cntX = 0;
                cntY = 0;
                while (abPoint < n * n && abValue == AB[abPoint]) {
                    abPoint++;
                    cntX++;
                }
                while (cdPoint > -1 && cdValue == CD[cdPoint]) {
                    cdPoint--;
                    cntY++;
                }
                cnt += cntX * cntY;
            }
        }

        System.out.println(cnt);
    }
}