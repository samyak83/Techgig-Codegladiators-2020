def main():
    t = int(input())
    while t>0:
        count = 0
        n = int(input())
        power_gteam = list(map(int,input().split()))
        power_oteam = list(map(int,input().split()))
        power_gteam.sort(reverse=True)
        power_oteam.sort(reverse=True)
        p=0
        for i in range(n):
            for j in range(p,n):
                if power_gteam[i] > power_oteam[j]:
                    p=j+1
                    count+=1
                    break
        print(count)
        t-=1


