import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int M = 0;

        for(int i = 1; i <= N; i++) {
            int number = i;
            int res = 0;

            while(number > 0){
                res += number % 10;
                number /= 10;
            }

            if(res + i == N){
                M = i;
                break;
            }
        }
        System.out.println(M);
    }
}