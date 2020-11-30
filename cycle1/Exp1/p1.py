def isSpecialSymbol(token):
	symbol=("~","!","@","#","$","&",
	"(","&",")","[","]","{","}",":",
	"?",".","|",",","%","+","-","*",
	"/","\"","\\","=","<",">")
	for i in token:
		if i in symbol:
			return True
	return False

def isOperator(token):
	op=("+","-","*","/","%","^","<",">",":=","&","|","!")
	if token in op:
		return True
	return False

def isKeyword(token):
	keywords=("prog","begin","end","read","write",
	"integer","string","character","float",
	"if","else","then","endif","while","do","endwhile")
	if token in keywords:
		return True
	return False

def isIdentifier(token):
	id=("1","2","3","4","5","6","7","8","9","0","_")
	if token[0] not in id:
		if(not isSpecialSymbol(token)):
			return True
	return False

def isLiteral(token):
	num=("1","2","3","4","5","6","7","8","9","0")
	count=0
	for i in token:
		if i not in num:
			if i!="." and count==0:
				return False
			count=1
	return True

def isSymbol(token):
	if token==",":
		return True
	return False

def mixed(token):
	op=("+","-","*","/","%","^","<",">",":=","&","|","!",",")
	s=[]
	for o in op:
		if o in token:
			t=token.split(o)
			if token[0]==o:
				s.append(o)
			for id in t:
				s.append(id)
				s.append(o)
			if(token[len(token)-1]!=o):
				s.pop()
	scan(s)

def scan(program):
	for line in program:
		token=line.split()
		for i in range(len(token)):
			if token[i][len(token[i])-1]==';':
				token[i]=token[i][:-1]
			if(isKeyword(token[i])):
				print("Keyword : "+token[i])
			elif(isIdentifier(token[i])):
				print("Identifier : "+token[i])
			elif(isLiteral(token[i])):
				print("Literal : "+token[i])
			elif(isOperator(token[i])):
				print("Operator : "+token[i])
			elif(isSymbol(token[i])):
				print("Symbol : "+token[i])
			else:
				mixed(token[i])

program=[]
print("The program is in the file p1.txt.\n")
f=open("p1.txt", "r")
for line in f:
	program.append(line)
	if line=="end\n":
		break
f.close()
scan(program)
