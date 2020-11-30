def epsilon_closure(enfa):
	eclosure=[]
	for k in range(n):
		t=[]
		t.append(k)
		if enfa[k][s]=="-":
			eclosure.append(t)
			continue
		for i in t:
			if enfa[i][s]=="-":
				continue
			x=enfa[i][s].split(",")
			for a in x:
				if a not in t:
					t.append(int(a))
		eclosure.append(t)
	print()
	print("State\tEpsilon-Closure\t")
	for i in range(len(eclosure)):
		print(i,"\t",eclosure[i])

global s
global n
n=int(input("Enter number of states in the NFA:"))
s=int(input("Enter number of input symbols:"))
print("State",end="\t")
x=('a','b','c','d','e','f','g','h','i','j')
for i in range(s):
	print(x[i],end="\t")
print("epsilon")
enfa=[]
for i in range(n):
	print(i,end="\t")
	t=input().split()
	enfa.append(t)
epsilon_closure(enfa)
