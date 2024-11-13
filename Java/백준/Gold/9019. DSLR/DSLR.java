import java.io.*;
import java.util.*;

public class Main {
	
	static String result;
	public static void main(String[] agrs) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			
			boolean[] visited = new boolean[10000];
			Queue<tuple> queue = new LinkedList<tuple>();
			queue.add(new tuple(A, ""));
			while (!queue.isEmpty()) {
				tuple t = queue.poll();
				int num = t.num;
				String cmd = t.cmd;
				
				if (num == B) {
					result = cmd;
					break;
				}
				
				int d = (num * 2) % 10000;
				if (!visited[d]) {
					visited[d] = true;
					queue.add(new tuple(d, cmd + "D"));
				}
				
				int s = num == 0 ? 9999 : num - 1;
				if (!visited[s]) {
					visited[s] = true;
					queue.add(new tuple(s, cmd + "S"));
				}
				
				int l = num / 1000 + (num % 1000) * 10;
				if (!visited[l]) {
					visited[l] = true;
					queue.add(new tuple(l, cmd + "L"));
				}
				
				int r = num / 10 + (num % 10) * 1000;
				if (!visited[r]) {
					visited[r] = true;
					queue.add(new tuple(r, cmd + "R"));
				}
			}
			
			System.out.println(result);
		}		
	}
}

class tuple {
	int num;
	String cmd;
	tuple (int num, String cmd) {
		this.num = num;
		this.cmd = cmd;
	}
}