import math
import cmath

#  ax2 + bx + c = 0
# solve for a,b,c even if they are complex

#solution of quadratic eq= (-b +- discrimiante)/(2a)

#REMEMBER THAT YOU MUST WRITE 1J IF YOU WANT TO USE j, NOT eg 1+j, it's 1+1j
##### D
def q_solve(a,b,c):
    discriminante=b**2-4*a*c
    solution_a= (-b+cmath.sqrt(discriminante))/(2*a)
    solution_b= (-b-cmath.sqrt(discriminante))/(2*a)
    return solution_a,solution_b


print(q_solve(3+2j,2+3j,1-1j))

