def RDP(pr,str,ip):
	global production
	global T
	global N
	if len(pr)>0 and pr[0]=="#":
		return RDP(pr[1:],str,ip)
	if len(pr)==0:
		if str[ip]=='$':
			return True
		return False
	if pr[0] in T:
		if str[ip]==pr[0]:
			return RDP(pr[1:],str,ip+1)
		return False
	if pr[0] in N:
		c=pr[0]
		for i in production[c]:
			if(RDP(i+pr[1:],str,ip)):
				return True
	return False

global production
global T
global N
production={}
n=int(input("Enter the number of productions:"))
print("Enter the productions:\t\t(Use \# for epsilon)")
T=[]
N=[]
s=[]
for _ in range(n):
	pr=input().split(" -> ")
	if pr[0] in production.keys():
		production[pr[0]].append(pr[1])
	else:
		production[pr[0]]=[pr[1]]
	if pr[0] not in N:
		N.append(pr[0])
	if pr[0] not in s:
		s.append(pr[0])
	if pr[1]=='#':
		continue
	for i in pr[1]:
		if i not in s:
			s.append(i)
for i in s:
	if i not in N:
		T.append(i)
print("Set of Terminals : ",end="")
for i in range(len(T)-1):
	print(T[i],end=",")
print(T[-1])
print("Set of Non-terminals : ",end="")
for i in range(len(N)-1):
	print(N[i],end=",")
print(N[-1])
S=N[0]
print("Start Symbol :",S)
str=input("Enter the expression to be parsed : ")
w=str+'$'
if(RDP(S,w,0)):
	print("Valid Expression")
else:
	print("Invalid Expression")
