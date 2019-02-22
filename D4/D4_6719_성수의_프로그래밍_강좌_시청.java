import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test_case = sc.nextInt();
		
		for(int i = 1; i <= test_case; i++)
		{
			int N = sc.nextInt();
			int K = sc.nextInt();
			int[] arr = new int[N];
			for(int j = 0; j < N; j++)
			{
				arr[j] = sc.nextInt();
			}
			Arrays.sort(arr);
			
			int[] arr2 = new int[K];
			int q = 0;
			for(int j = arr.length-1; j >= arr.length-K; j--)
			{
				arr2[q] = arr[j];
				q++;
			}
			
			float sum = 0;
			for(int j = arr2.length-1; j >= 0; j--)
			{
				float tmp = arr2[j] + sum;
				sum = tmp/2;
			}
			
			System.out.println("#"+i+" " + sum);
		}
	}
}


