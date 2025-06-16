n,m = map(int,input().split())
set_n = set(input() for x in range(n))
set_m = set(input() for i in range(m))

print("\n".join(set_n.intersection(set_m)))

