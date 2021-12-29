print(((n:=int(input())+1) and False) or sum([( ((n:=n-1) and False) or (n-x if n>=x else x-n)) for x in sorted(list(map(int,input().split())))[::-1]]))
