import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        String S = br.readLine();
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[S.length() + 1][26];

        for (int i = 0; i < S.length(); i++) {
            int alphabet = S.charAt(i) - 'a';
            for (int j = 0; j < 26; j++) {
                int beforeValue = arr[i][j];
                arr[i + 1][j] = (j == alphabet ? beforeValue + 1 : beforeValue);
            }
        }

        for (int tc = 0; tc < N; tc++) {
            st = new StringTokenizer(br.readLine());

            int a = st.nextToken().charAt(0) - 'a';
            int l = Integer.parseInt(st.nextToken()) + 1;
            int r = Integer.parseInt(st.nextToken()) + 1;

            bw.write((arr[r][a] - arr[l - 1][a] + "\n"));
        }

        bw.flush();
    }
}