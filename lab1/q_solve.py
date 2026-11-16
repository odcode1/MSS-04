import math


#  ax2 + bx + c = 0
# solve for real, get exception if not real
# not real if b^2-4ac

#solution of quadratic eq= (-b +- discrimiante)/(2a)

##### B+C)
def q_solve(a,b,c):
    discriminante=(b**2 -4*a*c)
    #print(discriminante)
    if discriminante>=0:
        print("roots are real")
        if discriminante==0:
            print("only one root")
            result_a=-b/(2*a)
            return result_a
        else:
            result_a1= (-b+ math.sqrt(discriminante))/(2*a)
            result_a2= (-b-math.sqrt(discriminante))/(2*a)
            return result_a1,result_a2
    else:
        print("complex roots")
        result_a1=(-b+ cmath.sqrt(discriminante))/(2*a)
        result_a2= (-b-cmath.sqrt(discriminante))/(2*a)
        return result_a1,result_a2

print(q_solve(1,2,1))

