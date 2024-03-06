import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    static class Reader {
        BufferedReader br;
        StringTokenizer st;
        public Reader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        String rstr() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int rint() {return Integer.parseInt(rstr());}
    }
    static BufferedWriter br = new BufferedWriter(new OutputStreamWriter(System.out));
    static ArrayList<Integer>[] gr;
    static int[] ind, sid;
    static ArrayDeque<Integer> ad;
    static int cnt, snt, N;
    static long[][] tar;
    static boolean[] ist, isf;
    static final int siz=164;
    static TreeSet<Integer>[] g2;

    public static void main(String[] args) throws IOException {
        Reader s=new Reader();
        N = s.rint(); int m=s.rint();
        init();
        int[][] list=new int[m][2];
        for(int i=0;i<m;i++){
            int a=s.rint(), b=s.rint();
            gr[b].add(a);
            list[i][0]=b; list[i][1]=a;
        }
        for (int i = 1; i <= N; i++) {
            if (ind[i] == -1) tam(i);
        }
        gr=null;
        g2=new TreeSet[snt];
        for (int i = 0; i < snt; i++) {
            g2[i] = new TreeSet();
        }
        ist=new boolean [snt];
        isf=new boolean [snt];
        tar=new long[snt][siz];
        for (int i = 1; i <= N; i++) {
            tar[sid[i]][i / 62] |= 1L << (i % 62);
        }
        for (int i = 0; i < m; i++) {
            int a = sid[list[i][0]], b = sid[list[i][1]];
            if (a == b) continue;
            isf[b] = true;
            g2[a].add(b);
        }
        int max=0;
        int[] gae=new int[snt];
        for(int i=0;i<snt;i++){
            if(isf[i]) continue;
            dfs(i);
            int c=0;
            for(int j=0;j<siz;j++) c+=Long.bitCount(tar[i][j]);
            max=Math.max(max, c);
            gae[i]=c;
        }
        for (int i = 1; i <= N; i++) {
            if (gae[sid[i]] == max) wis(i);
        }
        br.flush();
        br.close();
    }

    static void dfs(int i) {
        ist[i]=true;
        for(int c: g2[i]){
            if(!ist[c]) dfs(c);
            for (int a = 0; a < siz; a++) {
                tar[i][a] |= tar[c][a];
            }
        }
    }

    static void init() {
        gr=new ArrayList[N+1];
        for (int i = 0; i <= N; i++) {
            gr[i] = new ArrayList<>();
        }
        sid=new int[N+1]; ind=new int[N+1];
        Arrays.fill(sid, -1); Arrays.fill(ind, -1);
        cnt=snt=0;
        ad=new ArrayDeque<>();
    }

    static int tam(int i){
        int mv=ind[i]=cnt++;
        ad.add(i);
        for(int c: gr[i]){
            if (ind[c] == -1) {
                mv = Math.min(mv, tam(c));
            } else if (sid[c] == -1) {
                mv = Math.min(mv, ind[c]);
            }
        }
        if (mv == ind[i]) {
            while (true) {
                int te = ad.pollLast();
                sid[te] = snt;
                if (te == i) break;
            }
            snt++;
        }
        return mv;
    }

    static void wis(long i) throws IOException {
        br.write(i+" ");
    }
}
