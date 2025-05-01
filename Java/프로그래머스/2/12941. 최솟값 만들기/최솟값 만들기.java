import java.util.Arrays;

class Solution {
    
    static int len, answer;
    
    public int solution(int[] A, int[] B) {

        Arrays.sort(A);
        Arrays.sort(B);
        
        len = A.length;
        for (int i = 0; i < len; i++) {
            answer += A[i] * B[len - i - 1];
        }
        
        return answer;
    }
}