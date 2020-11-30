def MinimizeDFA(dfa):
	print()
	print("Generating minimized DFA...")
	print()
	m=[[0 for _ in range(n)] for _ in range(n)]
	eq=[[] for _ in range(n)]
	flag=1
	f=dfa[3]
	tt=dfa[2]
	for i in range(n):
		if i not in f:
			for j in f:
				m[i][j]=1
				m[j][i]=1
	while flag!=0:
		flag=0
		for i in range(n):
			for j in range(i+1,n):
				if m[i][j]==0:
					for u in range(s):
						if m[tt[i][u]][tt[j][u]]==1:
							m[i][j]=1
							m[j][i]=1
							flag=1
	for i in range(n):
		for j in range(n):
			if m[i][j]==0:
				eq[i].append(j)
	delta=[]
	for i in eq:
		if i not in delta:
			delta.append(i)
	eq=delta
	delta=[]
	for state in eq:
		trans=[]
		for j in range(s):
			t=tt[state[0]][j]
			for loc in eq:
				if t in loc:
					trans.append(loc[0])
		delta.append(trans)
	print("Start State of minimized DFA : 0")
	print()
	print("State",end="\t")
	for i in range(s-1):
		print(sigma[i],end="\t")
	print(sigma[s-1])
	for i in range(len(delta)):
		print(i,end="\t")
		for j in range(s-1):
			print(delta[i][j],end="\t")
		print(delta[i][s-1])
	print()
	f=[]
	for state in eq:
		if state[0] in dfa[3]:
			f.append(state[0])
	print("Final States of minimized DFA : ",end="")
	for i in range(len(f)-1):
		print(f[i],end=",")
	print(f[len(f)-1])

global s
global n
global sigma
n=int(input("Enter number of states in the DFA:"))
Q=[i for i in range(n)]
s=int(input("Enter number of input symbols:"))
print("State",end="\t")
x=('a','b','c','d','e','f','g','h','i','j')
sigma=[]
for i in range(s):
	print(x[i],end="\t")
	sigma.append(x[i])
print()
dfa=[]
dfa.append(Q)
delta=[]
for i in range(n):
	print(i,end="\t")
	t=input().split()
	row=[]
	for k in t:
		row.append(int(k))
	delta.append(row)
S=int(input("Enter the start state of the DFA:"))
f=input("Enter the final states of the DFA:").split(",")
F=[]
for i in range(len(f)):
	F.append(int(f[i]))
dfa.append(S)
dfa.append(delta)
dfa.append(F)
MinimizeDFA(dfa)
