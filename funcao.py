def soma(x,y):
	return (x+y)

s = soma(5,4)

def mult(x,y):
	return (x*y)

s = soma(5,4)
m = mult(6,3)

def sub(x,y):
	return (x-y)

def div(x,y):
	return (x/y)

s = soma(5,4)
m = mult(6,3)
sub = sub(10,2)
div = div(20,2)

print(s)
print(m)
print(sub)
print(div)

#Chamar de forma recursiva
print(soma(s,m))