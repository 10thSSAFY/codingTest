import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		String A = st.nextToken();
		String B = st.nextToken();

		long result = 0;
		for(int i = 0; i < A.length(); i++) {
			for(int j = 0; j < B.length(); j++) {
				result += (A.charAt(i) - '0') * (B.charAt(j) - '0');
			}
		}
		System.out.println(result);
	}

}