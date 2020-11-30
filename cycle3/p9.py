def FIRST(X):
	global production
	global T
	global N
	first=[]
	if X in T:
		first.append(X)
	if X in N:
		if '#' in production[X]:
			first.append('#')
		for pr in production[X]:
			for p in pr:
				f=FIRST(p)
				for i in f:
					if i not in first:
						first.append(i)
				if '#' not in f:
					break
			flag=0
			for p in pr:
				if '#' not in FIRST(p):
					flag=1
					break
			if flag==0:
				if '#' not in first:
					first.append('#')
	return first

def FOLLOW():
	global production
	global follow
	global first
	global N
	for X in N:
		for pr in production[X]:
			if pr[-1] in N and '$' not in follow[pr[-1]]:
				follow[pr[-1]].append('$')
			for i in range(len(pr)-1):
				if pr[i] in N:
					f=first[pr[i+1]]
					for x in f:
						if (x not in follow[pr[i]]
						and x!='#'):
							follow[pr[i]].append(x)
	for X in N:
		for pr in production[X]:
			for p in pr:
				if ((p==pr[-1]
				or '#' in first[pr[pr.index(p)+1]])
				and p in N):
					f=follow[X]
					for x in f:
						if x not in follow[p]:
							follow[p].append(x)

global production
global T
global N
global follow
global first
production={}
n=int(input("Enter the number of productions:"))
print("Enter the productions:\t\t(Use \# for epsilon)")
T=[]
N=[]
s=[]
first={}
follow={}
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
for i in s:
	first[i]=FIRST(i)
	if i in N:
		follow[i]=[]
follow[N[0]].append('$')
print("Set of Terminals : ",end="")
for i in range(len(T)-1):
	print(T[i],end=",")
print(T[-1])
print("Set of Non-Terminals : ",end="")
for i in range(len(N)-1):
	print(N[i],end=",")
print(N[-1])
print("FIRST")
for i in s:
	print("\t",i,end=" : ")
	for f in first[i]:
		print(f,end=" ")
	print()
print("FOLLOW")
FOLLOW()
for i in follow.keys():
	print("\t",i,end=" : ")
	for f in follow[i]:
		print(f,end=" ")
	print()
