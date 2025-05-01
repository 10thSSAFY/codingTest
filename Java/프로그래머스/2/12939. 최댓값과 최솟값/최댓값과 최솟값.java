class Solution {
    
    static int n, min, max;
    static String[] A;
    
    public String solution(String s) {
        A = s.split(" ");
        
        min = max = Integer.parseInt(A[0]);
        for (int i = 1; i < A.length; i++) {
            n = Integer.parseInt(A[i]);
            min = Math.min(min, n);
            max = Math.max(max, n);
        }
        
        String answer = min + " " + max;
        return answer;
    }
}
