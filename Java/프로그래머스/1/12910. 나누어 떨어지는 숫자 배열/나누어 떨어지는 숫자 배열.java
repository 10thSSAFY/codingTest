import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer;
        
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (int num : arr) {
            if (num % divisor == 0) {
                arrayList.add(num);
            }
        }
        
        int N = arrayList.size();
        if (N == 0) {
            answer = new int[1];
            answer[0] = -1;
        }
        else {
            answer = new int[N];
            for (int i = 0; i < N; i++) {
                answer[i] = arrayList.get(i);
            }

            Arrays.sort(answer);
        }
        
        return answer;
    }
}