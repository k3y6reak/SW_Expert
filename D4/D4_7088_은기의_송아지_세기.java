# [아이디어]
# 인덱스가 1부터 시작하므로 하나 더 큰 배열을 생성한다.
# 마찬가지로 등급도 1부터 시작 하므로 하나 더 큰 배열을 생성한다.
# [인덱스][등급]
# 
# 1
# 6 3 -> [7][4] 칸을 만든다는 것.
# 2 -> 1번 인덱스에 [0, 1, 2, 3] 등급의 배열 중에서 [0, 0, 1, 0] 해당 위치에 1증가 시킨다.
# 1 -> 2번 인덱스에 1번 인덱스의 값을 2번 인덱스에 가져온 후에 해당 위치에 1 증가 시킨다. [0, 0, 1, 0] -> [0, 1, 1, 0]
# 1 -> 3번 인덱스에 2번 인덱스의 값을 3번 인덱스에 가져온 후 해당 위치에 1 증가 시킨다. [0, 1, 1, 0] -> [0, 2, 1, 0]
# 3 -> 마찬가지로 [0, 2, 1, 0] -> [0, 2, 1, 1]
# 2
# 1
# 1 6
# 3 3
# 2 4 -> 2번 인덱스부터 4번 인덱스를 가져오라고 한다면 4번 인덱스 값 - (2번 -1 인덱스 값)을 해주면 된다.
# 4번 인덱스 값 [0, 2, 1, 1] - 1번 인덱스 값 [0, 0, 1, 0] = [0, 2, 0, 1]이 된다.



import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		for(int i = 1; i < tc+1; i++)
		{
			int N = sc.nextInt();
			int Q = sc.nextInt();
			int[][] cows = new int[N+1][4];
			
			for(int j = 1; j < N + 1; j++) {
				int tmp = sc.nextInt();
				for(int k= 0; k < 4; k++)
				{					
					cows[j][k] += cows[j-1][k];
				}
				
				cows[j][tmp]++;
			}

			System.out.println("#"+i);
			for(int j = 0; j < Q; j++)
			{
				int start = sc.nextInt();
				int end = sc.nextInt();
				
				for(int k = 1; k < 4; k++)
				{
					System.out.print(cows[end][k] - cows[start-1][k]+" ");
				}
				System.out.println();
			}
			
		}
	}
}
