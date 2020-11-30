def epsilon_closure(l,k):
	t=[]
	t.append(k)
	if l[k][s]=="-":
		return t
	for i in t:
		if l[i][s]=="-":
			continue
		x=l[i][s].split(",")
		for a in x:
			if a not in t:
				t.append(int(a))
	return t

def ConvertToNFA(enfa):
	print()
	print("Generating NFA ...")
	Q=enfa[0]
	S=enfa[1]
	delta=[]
	F=enfa[3]
	tt=enfa[2]
	for i in Q:
		l=epsilon_closure(tt,i)
		trans=[]
		for j in range(len(sigma)):
			f=[]
			for k in l:
				if(tt[k][j]=="-"):
					continue
				elif(len(tt[k][j])==1):
					x=tt[k][j]
					if x not in f:
						f.append(int(x))
				else:
					x=tt[k][j].split(",")
					for q in x:
						if q not in f:
							f.append(int(q))
			c=[]
			for k in f:
				x=epsilon_closure(tt,k)
				for w in x:
					if w not in c:
						c.append(w)
			trans.append(c)
		delta.append(trans)
	print()
	print("Start states of NFA : ",end="")
	for i in range(len(S)-1):
		print(S[i],end=",")
	print(S[len(S)-1])
	print()
	print("STATE",end="\t")
	for i in range(len(sigma)-1):
		print(sigma[i],end="\t")
	print(sigma[len(sigma)-1])
	for i in range(n):
		print(i,end="\t")
		for j in range(s-1):
			for z in range(len(delta[i][j])-1):
				print(delta[i][j][z],end=",")
			print(delta[i][j][len(delta[i][j])-1],end="\t")
		for z in range(len(delta[i][s-1])-1):
			print(delta[i][s-1][z],end=",")
		print(delta[i][s-1][len(delta[i][s-1])-1])
	print()
	for i in S:
		l=epsilon_closure(tt,i)
		for j in l:
			if j in F:
				F.append(i)
				break
	print("Final states of NFA : ",end="")
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
print("epsilon")
enfa=[]
enfa.append(Q)
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
enfa.append(S)
enfa.append(delta)
enfa.append(F)
ConvertToNFA(enfa)
