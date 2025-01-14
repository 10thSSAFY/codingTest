import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int R = park.length;
        int C = park[0].length();
        int w = 0;
        int h = 0;
        for (int r = 0; r < park.length; r++) {
            String line = park[r];
            for (int c = 0; c < line.length(); c++) {
                if (line.charAt(c) == 'S') {
                    h = r;
                    w = c;
                }
            }
        }
        
        for (String route : routes) {
            StringTokenizer st = new StringTokenizer(route);
            String d = st.nextToken();
            int l = Integer.parseInt(st.nextToken());
            
            if (d.equals("E")) {
                if (C <= w + l) {
                    continue;
                }
                
                if (canGo(h, w, 0, 1, l, park)) {
                    continue;
                }
                
                w += l;
            }
            
            else if (d.equals("W")) {
                if (w - l < 0) {
                    continue;
                }
                
                if (canGo(h, w, 0, -1, l, park)) {
                    continue;
                }
                
                w -= l;
            }
            
            else if (d.equals("S")) {
                if (R <= h + l) {
                    continue;
                }
                
                if (canGo(h, w, 1, 0, l, park)) {
                    continue;
                }
                
                h += l;
            }
            
            else if (d.equals("N")) {
                if (h - l < 0) {
                    continue;
                }
                
                if (canGo(h, w, -1, 0, l, park)) {
                    continue;
                }
                
                h -= l;
            }
        }
        
        int[] answer = {h, w};
        return answer;
    }
    
    static boolean canGo(int r, int c, int dr, int dc, int L, String[] park) {
        for (int i = 1; i <= L; i++) {
            if (park[r + dr * i].charAt(c + dc * i) == 'X') {
                return true;
            }
        }
        return false;
    }
}