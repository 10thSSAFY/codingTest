import java.io.*;
import java.util.*;

public class Main {

    static int L, W, H, N;
    static int[][] arr;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        N = Integer.parseInt(br.readLine());
        arr = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        System.out.println(solution(L, W, H, arr));
    }

    static int solution(int l, int w, int h, int[][] blocks) {

        Arrays.sort(blocks, (a, b) -> b[0] - a[0]);
        long totalCount = 0;
        long volume = (long) l * w * h;
        long usedVolume = 0;

        for (int i = 0; i < blocks.length; i++) {
            long size = (1 << blocks[i][0]);
            int count = blocks[i][1];

            if (volume <= usedVolume)
                break;

            long maxCount = (l / size) * (w / size) * (h / size);
            maxCount -= usedVolume / (size * size * size);
            long useCount = Math.min(count, maxCount);

            usedVolume += useCount * (size * size * size);
            totalCount += useCount;
        }

        if (usedVolume == volume) {
            return (int) totalCount;
        } else {
            return -1;
        }
    }
}