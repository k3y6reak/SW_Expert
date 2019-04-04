


class Atomic:
    def __init__(self, x, y, go, power):
        self.x = x
        self.y = y
        self.go = go
        self.power = power


#     상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def boom(map_, atomics, boom_chk, n):
    all_power = 0

    # 가장 끝 점에서부터 반대편 끝 점까지 이동하면 원자는 밖으로 나갈 수 있음.
    # 1초부터 4000초까지 맵에 있으며, 4001초면 밖으로 나감.
    for time in range(1, 4002):
        # 해당 원자들을 방향대로 이동시키자.
        for i in range(n):
            if atomics[i].power == 0: # 해당 원자의 파워가 0이면 버림.
                continue

            x = atomics[i].x
            y = atomics[i].y
            go = atomics[i].go

            nx = x + dx[go]
            ny = y + dy[go]

            if nx < 0 or ny < 0 or nx >= 4001 or ny >= 4001:
                # 이동하는 원자의 방향이 범위 밖이라면.
                # 해당 원자를 소멸시킨다.
                map_[x][y] -= 1
                atomics[i].power = 0
                continue

            # 범위 내이면. 다음 위치로 이동한다.
            # 이동하면 원래 자리 -1 후 다음 자리 +1을 해준다.
            # 원자가 이동하면서 겹치면 해당 자리는 1을 초과하게 된다.
            map_[x][y] -= 1
            atomics[i].x = nx
            atomics[i].y = ny
            map_[nx][ny] += 1

            if map_[nx][ny] > 1:
                boom_chk[nx][ny] = True

        for i in range(n):
            # 원자의 파워가 0이면 버림.
            if atomics[i].power == 0:
                continue

            x = atomics[i].x
            y = atomics[i].y

            # 해당 위치가 폭발지점이고, 원자의 개수가 0개가 아니면.
            # 원자의 개수를 감소, 파워를 더하고, 0으로 변경 해야함.
            if boom_chk[x][y] and map_[x][y] > 1:
                map_[x][y] -= 1
                all_power += atomics[i].power
                atomics[i].power = 0
            # 폭발지점에서 원자가 모두 감소되었으면, chk를 False로 변경
            elif boom_chk[x][y] and map_[x][y] == 1:
                map_[x][y] -= 1
                all_power += atomics[i].power
                atomics[i].power = 0
                boom_chk[x][y] = False

        # 돌면서 원자들을 모두 확인해 파워가 0이면 리턴
        cnt = 0
        for i in range(n):
            if atomics[i].power == 0:
                cnt += 1

        if cnt == n:
            return all_power


def main():
    for t in range(1, int(input()) + 1):
        n = int(input())
        atomics = []

        # 맵의 범위가 -1000 ~ 1000 이므로 0부터 시작하도록 +1000을 한다.
        # 또한 0.5초에서 충돌이 일어날 수 있으므로 맵을 2배 키워 1칸 단위로 충돌이 일어날 수 있도록 한다.
        # 맵의 범위는 0 ~ 4000칸까지 이므로 칸은 4001칸으로 잡는다.
        map_ = [[0]*4001 for _ in range(4001)]
        boom_chk = [[False]*4001 for _ in range(4001)]

        for i in range(n):
            line = list(map(int, input().split()))
            atomics.append(Atomic((line[0]+1000)*2, (line[1]+1000)*2, line[2], line[3]))
            map_[atomics[i].x][atomics[i].y] += 1 # 해당 위치에 원자를 넣는다.

        print("#%d %d" %(t, boom(map_, atomics, boom_chk, n)))


if __name__ == '__main__':
    main()










======================================

import java.util.Scanner;

public class Solution {
	public static class Atomic
	{
		int x;
		int y;
		int go;
		int power;
		
		public Atomic(int x, int y, int go, int power) {
			super();
			this.x = x;
			this.y = y;
			this.go = go;
			this.power = power;
		}
		
	}
	
	//			     상, 하, 좌, 우
	static int[] dx = {0, 0, -1, 1};
	static int[] dy = {1, -1, 0, 0};
	
	public static int boom(int[][] map, Atomic[] atomics, boolean[][] boom_chk, int N)
	{
		int all_power = 0;
		// 가장 끝 점에서부터 반대편 끝 점까지 이동하면 원자는 밖으로 나갈 수 있음.
	    // 1초부터 4000초까지 맵에 있으며, 4001초면 밖으로 나감.
		for(int time = 1; time < 4002; time++)
		{
			// 해당 원자들을 방향대로 이동시키자.
			for(int i = 0; i < N; i++)
			{
				// 해당 원자의 파워가 0이면 버림.
				if(atomics[i].power == 0)
				{
					continue;
				}
				
				int x = atomics[i].x;
				int y = atomics[i].y;
				int go = atomics[i].go;
				
				int nx = x + dx[go];
				int ny = y + dy[go];
				
				
				// 이동하는 원자의 방향이 범위 밖이라면.
                // 해당 원자를 소멸시킨다.
				if(nx < 0 || ny < 0 || nx >= 4001 || ny >= 4001)
				{
					map[x][y] -= 1;
					atomics[i].power = 0;
					continue;
				}
				
				// 범위 내이면. 다음 위치로 이동한다.
	            // 이동하면 원래 자리 -1 후 다음 자리 +1을 해준다.
	            // 원자가 이동하면서 겹치면 해당 자리는 1을 초과하게 된다.
				
				map[x][y] -= 1;
			    atomics[i].x = nx;
			    atomics[i].y = ny;
			    map[nx][ny] += 1;
				
	            if(map[nx][ny] > 1)
	            {	            	
	            	boom_chk[nx][ny] = true;
	            }
			}
			
			for(int i = 0; i < N; i++)
			{
				// 원자의 파워가 0이면 버림.
	            if(atomics[i].power == 0)
	            {
	            	continue;
	            }

	            int x = atomics[i].x;
	            int y = atomics[i].y;

	            
	            // 해당 위치가 폭발지점이고, 원자의 개수가 0개가 아니면.
	            // 원자의 개수를 감소, 파워를 더하고, 0으로 변경 해야함.
	            if(boom_chk[x][y] && map[x][y] > 1)
	            {
	            	map[x][y] -= 1;
	    	        all_power += atomics[i].power;
	    	        atomics[i].power = 0;
	            }
	                
	            // 폭발지점에서 원자가 모두 감소되었으면, chk를 False로 변경
	            else if(boom_chk[x][y] && map[x][y] == 1)
	            {
	            	map[x][y] -= 1;
	    	        all_power += atomics[i].power;
	    	        atomics[i].power = 0;
	    	        boom_chk[x][y] = false;
	            }
	                
			}
			
			// 돌면서 원자들을 모두 확인해 파워가 0이면 리턴
	        int cnt = 0;
	        for(int i = 0; i < N; i++)
	        {
	        	if(atomics[i].power == 0)
	        	{
	        		cnt += 1;
	        	}
	                
	        }
	            

	        if(cnt == N)
	        {
	        	return all_power;
	        }
	            
	        
		}
		return 0;
	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		
		for(int t = 1; t <= tc; t++)
		{
			int N = sc.nextInt();
			Atomic[] atomics = new Atomic[N];
			
			// 맵의 범위가 -1000 ~ 1000 이므로 0부터 시작하도록 +1000을 한다.
	        // 또한 0.5초에서 충돌이 일어날 수 있으므로 맵을 2배 키워 1칸 단위로 충돌이 일어날 수 있도록 한다.
	        // 맵의 범위는 0 ~ 4000칸까지 이므로 칸은 4001칸으로 잡는다.
			
			int[][] map = new int[4001][4001];
			boolean[][] boom_chk = new boolean[4001][4001];
			
			for(int i = 0; i < N; i++)
			{
				int x = (sc.nextInt()+1000)*2;
				int y = (sc.nextInt()+1000)*2;
				int go = sc.nextInt();
				int power = sc.nextInt();
				
				atomics[i] = new Atomic(x, y, go, power);
			}
			
			System.out.println("#"+t+" "+boom(map, atomics, boom_chk, N));
		}
		
	}

}

