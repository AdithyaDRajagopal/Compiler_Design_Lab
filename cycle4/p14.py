def balanced(exp):
	if '(' not in exp and ')' not in exp:
		return True
	else:
		count=0
		for i in range(len(exp)):
			if exp[i]=='(':
				count+=1
			elif exp[i]==')':
				count-=1
			if count==-1:
				return False
	if count==0:
		return True
	return False

def set(exp):
	list=[]
	br={}
	for i in range(len(exp)):
		if exp[i]=='(':
			list.append(i)
		elif exp[i]==')':
			br[list.pop()]=i
	return br

def bracket(exp):
	global ch
	br=set(exp)
	index=exp.find('(')
	sub=igc(exp[index+1:br[index]])
	exp=exp[:index]+sub+exp[br[index]+1:]
	return exp

def div(exp):
	global ch
	index=exp.find('/')
	print('\t'+ch+' = '+exp[index-1]+' / '+exp[index+1])
	str=exp.replace(exp[index-1]+'/'+exp[index+1],ch)
	ch=chr(ord(ch)-1)
	return str

def mul(exp):
	global ch
	index=exp.find('*')
	print('\t'+ch+' = '+exp[index-1]+' * '+exp[index+1])
	str=exp.replace(exp[index-1]+'*'+exp[index+1],ch)
	ch=chr(ord(ch)-1)
	return str

def add(exp):
	global ch
	index=exp.find('+')
	print('\t'+ch+' = '+exp[index-1]+' + '+exp[index+1])
	str=exp.replace(exp[index-1]+'+'+exp[index+1],ch)
	ch=chr(ord(ch)-1)
	return str

def sub(exp):
	global ch
	index=exp.find('-')
	print('\t'+ch+' = '+exp[index-1]+' - '+exp[index+1])
	str=exp.replace(exp[index-1]+'-'+exp[index+1],ch)
	ch=chr(ord(ch)-1)
	return str

def igc(exp):
	rhs=exp
	while(len(rhs)!=1):
		if '(' in exp:
			exp=bracket(exp)
		elif '/' in exp:
			exp=div(exp)
		elif '*' in exp:
			exp=mul(exp)
		elif '+' in exp:
			exp=add(exp)
		elif '-' in exp:
			exp=sub(exp)
		rhs=exp[exp.find('=')+1:]
	return exp

ch='Z'
exp=input("Enter the expression : ")
if '=' not in exp:
	print("Invalid expression!!!")
elif not balanced(exp):
	print("Parentheses not balanced!!!")
else:
	print()
	print("Intermediate Code:")
	str=exp.split('=')
	exp=igc(str[1])
	print('\t'+str[0]+' = '+exp)
	print()
