import java.io.*;
import java.util.*;

public class Main {

    static int T, x1, y1, x2, y2, n, cx, cy, r;
    static StringTokenizer st;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(br.readLine());
            
            int result = 0;
            for (int tn = 0; tn < n; tn++) {
                st = new StringTokenizer(br.readLine());
                cx = Integer.parseInt(st.nextToken());
                cy = Integer.parseInt(st.nextToken());
                r = Integer.parseInt(st.nextToken());
                
                boolean start = ((cx - x1) * (cx - x1) + (cy - y1) * (cy - y1) < r * r);
                boolean arrive = ((cx - x2) * (cx - x2) + (cy - y2) * (cy - y2) < r * r);
                if (start && !arrive || !start && arrive) {
                    result++;
                }
            }
            
            System.out.println(result);
        }
    }
}