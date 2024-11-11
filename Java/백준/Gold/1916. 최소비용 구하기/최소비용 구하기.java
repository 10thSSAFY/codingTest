import java.io.*;
import java.util.*;

public class Main {
	
	static int N, M, S, E;
	static int[] distance;
	static boolean[] visited;
	static ArrayList<Edge>[] list;
	static PriorityQueue<Edge> q = new PriorityQueue<Edge>();
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		
		list = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			list[i] = new ArrayList<Edge>();
		}
		
		distance = new int[N + 1];
		visited = new boolean[N + 1];
		for (int i = 0; i <= N; i++) {
			distance[i] = Integer.MAX_VALUE;
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			list[u].add(new Edge(v, w));
		}
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		S = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		q.add(new Edge(S, 0));
		distance[S] = 0;
		while (!q.isEmpty()) {
			Edge current = q.poll();
			int c_v = current.vertex;
			if (visited[c_v]) {
				continue;
			}
			visited[c_v] = true;
			for (int i = 0; i < list[c_v].size(); i++) {
				Edge tmp = list[c_v].get(i);
				int next = tmp.vertex;
				int value = tmp.value;
				if (distance[next] > distance[c_v] + value) {
					distance[next] = distance[c_v] + value;
					q.add(new Edge(next, distance[next]));
				}
			}
		}
		
		System.out.println(distance[E]);
	}
	
}

class Edge implements Comparable<Edge> {
	
	int vertex, value;
	Edge(int vertex, int value) {
		this.vertex = vertex;
		this.value = value;
	}
	
	public int compareTo(Edge e) {
		if (this.value > e.value) {
			return 1;
		} else {
			return -1;
		}
	}
}