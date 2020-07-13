# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
def fun_find_int_roots(a, b, c):
	d=(b*b)-(4*a*c)
	if d==0:
		root1=-(b/2*a)
		root2=-(b/2*a)
	else:
		root1= (-b-math.sqrt(d))/2*a
		root2=(-b+math.sqrt(d))/2*a
		print(int(root1),int(root2))
	return int(root1),int(root2)
fun_find_int_roots(a,b,c)


