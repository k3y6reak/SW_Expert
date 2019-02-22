
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution {
	static int[] parents;
	static int[] rank;
	
	static void makeSet(int x) {
        parents[x] = x;
    }
    static int findSet(int x) {
        if( parents[x] == x )
            return x;
         
        parents[x] = findSet(parents[x]);
        return parents[x];
    }
    static void union(int x, int y) {
        int px = findSet(x);
        int py = findSet(y);
         
        if( rank[px] > rank[py] ) {
            parents[py] = px;
        }
        else {
            parents[px] = py;
            if( rank[px] == rank[py] )
                rank[py]++;
        }
    }
    
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st, st2;

		int tc = Integer.parseInt(br.readLine());
		for (int t = 0; t < tc; t++) {
			int land_num = Integer.parseInt(br.readLine());
			long[][] land_dot = new long[land_num][2];

			st = new StringTokenizer(br.readLine(), " ");
			st2 = new StringTokenizer(br.readLine(), " ");
			double e = Double.parseDouble(br.readLine());

			for (int l = 0; l < land_num; l++) {
				land_dot[l][0] = Integer.parseInt(st.nextToken());
				land_dot[l][1] = Integer.parseInt(st2.nextToken());
			}
			int tmp = (land_num - 1) * land_num / 2;
			double[][] adj = new double[tmp][3];

			int k = 0;
			for (int i = 0; i < land_num-1; i++) {
				for (int j = i + 1; j < land_num; j++) {
					long a = land_dot[j][0] - land_dot[i][0];
					long b = land_dot[j][1] - land_dot[i][1];
					double c = Math.sqrt(a * a + b * b);
					adj[k][0] = (int)i;
					adj[k][1] = (int)j;
					adj[k][2] = c;
					k++;
				}
			}

			
			Arrays.sort(adj, new Comparator<double[]>() {
				@Override
				public int compare(double[] o1, double[] o2) {
					return Double.compare(o1[2], o2[2]);
				}
				
			});
			
			parents = new int[land_num];
			rank = new int[land_num];
			
			for(int i = 0; i < land_num; i++)
			{
				makeSet(i);
			}
			
			double sum_len = 0;
			int j = 0;
			for(int i = 0; i < adj.length; i++)
			{
				if(j == land_num - 1)
				{
					break;
				}
				if(findSet((int) adj[i][0]) != findSet((int)adj[i][1]))
				{
					sum_len += adj[i][2]*adj[i][2];
					union((int)adj[i][0], (int)adj[i][1]);
					j+=1;
				}
			}
			System.out.println("#" + (t+1) + " " + Math.round(e*sum_len));

		}
	}
}


