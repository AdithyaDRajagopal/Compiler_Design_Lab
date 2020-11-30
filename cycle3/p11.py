def printStack():
	global Stack
	for i in Stack:
		print(i,end="")
	print("\t\t",end="")

def reduce():
	global Stack
	global handle
	global prevhandle
	if Stack[-1]=="i":
		Stack.pop()
		Stack.append("E")
		prevhandle=handle[0]
		return True
	if len(Stack)>=3:
		if Stack[-1]=="E" and Stack[-3]=="E":
			op=Stack.pop()
			op=Stack.pop()
			if op=="+":
				prevhandle=handle[1]
			elif op=="*":
				prevhandle=handle[2]
			return True
		elif Stack[-1]==")" and Stack[-2]=="E" and Stack[-3]=="(":
			op=Stack.pop()
			op=Stack.pop(-2)
			prevhandle=handle[3]
			return True
	return False

def Shift_Reduce_Parser(str):
	global Stack
	global handle
	global prevhandle
	T=['+','*','i','(',')','$']
	Stack=['$']
	ip=0
	handle=['i','E+E','E*E','(E)']
	print("STACK\t\tINPUT\t\tACTION")
	print("$\t\t"+str+"\t-")
	while ip<len(str):
		Stack.append(str[ip])
		ip=ip+1
		printStack()
		if ip==len(str):
			print("-\t\tShift")
			break
		print(str[ip:],"\t\tShift")
		while(reduce()):
			printStack()
			print(str[ip:],end="\t\t")
			print("Reduce E -> "+prevhandle)
	if Stack[0]=='$' and Stack[1]=='E' and Stack[2]=='$':
		return True
	return False

global Stack
global handle
global prevhandle
print("The Grammar is:")
print("E -> E+E | E*E | (E) | i")
s=input("Enter the string to be parsed:")
w=s+'$'
if(Shift_Reduce_Parser(w)):
	print("Successfully parsed")
else:
	print("Error in parsing")
