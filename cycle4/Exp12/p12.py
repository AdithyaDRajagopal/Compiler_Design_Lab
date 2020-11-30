def printloop(lines):
	for i in lines:
		print(i,end="")

def unroll_for(program,start):
	global variables
	lines=[]
	stack=[]
	i=start+1
	while i<len(program):
		if program[i][0]=="{":
			stack.append("{")
			i=i+1
			continue
		elif program[i][0]=="}":
			stack.pop()
			if len(stack)==0:
				break
		lines.append(program[i])
		if len(stack)==0:
			break
		i=i+1
	retval=i
	line=program[start]
	str=""
	for i in line[3:]:
		str+=i
	loop=str[1:len(str)-2]
	con=loop.split(";")
	init=con[0].split("=")
	init[1]=int(init[1])
	cnd=con[1]
	if "<" in cnd:
		if "=" in cnd:
			condition=cnd.split("<=")
			condition.append("<=")
		else:
			condition=cnd.split("<")
			condition.append("<")
	elif ">" in cnd:
		if "=" in cnd:
			condition=cnd.split(">=")
			condition.append(">=")
		else:
			condition=cnd.split(">")
			condition.append(">")
	condition[1]=int(condition[1])
	val=con[2]
	if "++" in val:
		inc=val.split("++")
		inc.append(1)
	elif "--" in val:
		inc=val.split("--")
		inc.append(-1)
	elif "+=" in val:
		inc=val.split("+=")
		inc[1]=int(inc[1])
	elif "-=" in val:
		inc=val.split("-=")
		inc[1]=-int(inc[1])
	if init[0]==condition[0] and init[0]==inc[0]:
		i=init[1]
		con=condition[2]
		if con=="<":
			while i<condition[1]:
				printloop(lines)
				i+=inc[1]
		elif con=="<=":
			while i<=condition[1]:
				printloop(lines)
				i+=inc[1]
		elif con==">":
			while i>condition[1]:
				printloop(lines)
				i+=inc[1]
		elif con==">=":
			while i>=condition[1]:
				printloop(lines)
				i+=inc[1]
	return retval

def loop_unroll(program):
	global variables
	i=0
	while i<len(program):
		if program[i][0:4]=="for(":
			i=unroll_for(program,i)
		else:
			print(program[i],end="")
		i=i+1

program=[]
print("The program is in the file p12.c.\n")
f=open("p12.c", "r")
for line in f:
	program.append(line)
	if line=="end\n":
		break
f.close()
loop_unroll(program)
