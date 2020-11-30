def newline(line,var,val):
	op=('+','-','*','/','%','[',']','=','<','>','(',')')
	start=0
	for _ in range(line.count(var)):
		start=line.find(var,start+1)
		end=start+len(var)
		if line[start-1] in op:
			line=line[:start]+val+line[end:]
	return line

def constant_propagation(program):
	variable={}
	for line in program:
		x=line.split(":=");
		if len(x)==2:
			lhs=x[0]
			rhs=x[1].split(";")
			if '+' in rhs[0]:
				op=rhs[0].split("+")
				if op[0] in variable.keys():
					op[0]=variable[op[0]]
				variable[lhs]=str(int(op[0])+int(op[1]))
			elif '-' in rhs[0]:
				op=rhs[0].split("-")
				if op[0] in variable.keys():
					op[0]=variable[op[0]]
				variable[lhs]=str(int(op[0])-int(op[1]))
			elif '*' in rhs[0]:
				op=rhs[0].split("*")
				if op[0] in variable.keys():
					op[0]=variable[op[0]]
				variable[lhs]=str(int(op[0])*int(op[1]))
			elif '/' in rhs[0]:
				op=rhs[0].split("/")
				if op[0] in variable.keys():
					op[0]=variable[op[0]]
				variable[lhs]=str(int(op[0])/int(op[1]))
			elif '%' in rhs[0]:
				op=rhs[0].split("%")
				if op[0] in variable.keys():
					op[0]=variable[op[0]]
				variable[lhs]=str(int(op[0])%int(op[1]))
			else:
				variable[lhs]=rhs[0]
		#else:
		for var in variable.keys():
			if var in line:
				val=variable[var]
				line=newline(line,var,val)
		print(line,end="")

program=[]
print("The program is in the file p13.txt.\n")
f=open("p13.txt","r")
for line in f:
	program.append(line)
f.close()
constant_propagation(program)
