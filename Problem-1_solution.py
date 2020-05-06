def main():
    number = int(input())
    quality = list(map(int,input().split()))
    quantity = list(map(int,input().split()))
    l = []
    for i in range (0,len(quantity)):
        data = quantity[i]//quality[i]
        l.append(data)
    print(min(l))

main()
