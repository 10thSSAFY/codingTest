class Solution {
    public String solution(int a, int b) {
        String[] days = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};
        int[] months = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30};
        int answer = 0;
        
        for (int i = 0; i < a; i++) {
            answer += months[i];
        }
        answer += b;
        
        return days[(answer) % 7];
    }
}