n,s = map(int, raw_input().split())
ans = s
for i in range(n):
	f,t = map(int, raw_input().split())
	ans = max(ans, t+f)
print ans