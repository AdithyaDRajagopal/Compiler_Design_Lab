def ConvertToDFA(nfa):
	print()
	print("Generating DFA...")
	delta=[]
	S=nfa[1]
	F=[]
	lazySet=[]
	lazySet.append(S)
	tt=nfa[2]
	i=0
	while i<len(lazySet):
		row=[]
		for j in range(len(sigma)):
			reachable=[]
			next=-1
			for k in lazySet[i]:
				states=tt[k][j].split(",")
				for x in states:
					y=int(x)
					if y not in reachable:
						reachable.append(y)
			reachable.sort()
			if reachable not in lazySet:
				lazySet.append(reachable)
				next=len(lazySet)
				row.append(next-1)
			else:
				next=lazySet.index(reachable)
				row.append(next)
		delta.append(row)
		i=i+1
	print()
	print("Start state of DFA : 0")
	print()
	print("STATE",end="\t")
	for i in range(s-1):
		print(sigma[i],end="\t")
	print(sigma[s-1])
	for i in range(len(lazySet)):
		print(i,end="\t")
		for j in range(s-1):
			print(delta[i][j],end="\t")
		print(delta[i][s-1])
	print()
	for x in lazySet:
		for y in x:
			if y in nfa[3]:
				F.append(lazySet.index(x))
				break
	print("Final States of DFA : ",end="")
	F.sort()
	for i in range(len(F)-1):
		print(F[i],end=",")
	print(F[len(F)-1])

global s
global n
global sigma
n=int(input("Enter number of states in the NFA:"))
Q=[i for i in range(n)]
s=int(input("Enter number of input symbols:"))
print("State",end="\t")
x=('a','b','c','d','e','f','g','h','i','j')
sigma=[]
for i in range(s):
	print(x[i],end="\t")
	sigma.append(x[i])
print()
nfa=[]
nfa.append(Q)
delta=[]
for i in range(n):
	print(i,end="\t")
	t=input().split()
	delta.append(t)
m=input("Enter the start states of the NFA:").split(",")
f=input("Enter the final states of the NFA:").split(",")
S=[]
F=[]
for i in range(len(m)):
	S.append(int(m[i]))
for i in range(len(f)):
	F.append(int(f[i]))
nfa.append(S)
nfa.append(delta)
nfa.append(F)
ConvertToDFA(nfa)
