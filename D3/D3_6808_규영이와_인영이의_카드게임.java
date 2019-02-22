import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Solution {
	static int win = 0;
	public static void swap(int[] in, int i, int k)
	{
		int tmp = in[i];
		in[i] = in[k];
		in[k] = tmp;
	}
	
	public static void perm(int[] in, int n, int[] gyu)
	{
		if(n == in.length)
		{
			int gyu_sum = 0;
			int in_sum = 0;
			for(int i = 0; i < in.length; i++)
			{
				if(in[i] < gyu[i])
				{
					gyu_sum += (in[i] + gyu[i]);
				}
				else
				{
					in_sum += (in[i] + gyu[i]);
				}
			}
			
			if(gyu_sum > in_sum)
			{
				win++;
			}
		}
		
		for(int i = n; i < in.length; i++)
		{
			swap(in, i, n);
			perm(in, n+1, gyu);
			swap(in, i, n);
		}
		
		return;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int testCase = sc.nextInt();

		for (int i = 0; i < testCase; i++) {
			boolean[] check = new boolean[19];
			int[] gyu = new int[9];
			int[] in = new int[9];

			for (int j = 0; j < 9; j++) {
				int num = sc.nextInt();
				check[num] = true;
				gyu[j] = num; // 규형이의 카드를 받는다.
			}
			int k = 0;
			for (int j = 1; j <= 18; j++) {
				
				if(check[j] != true)
				{
					in[k++] = j;
				}
			}
			
			perm(in, 0, gyu);
			System.out.println("#" + (i+1) + " " + win + " " + (362880-win));
			win = 0;
			
		}
	}
}


