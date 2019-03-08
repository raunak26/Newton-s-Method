# newton.py
# Raunak Anand
# Newton's method
# to find roots of equation, created by user inputs
#

def newton(a,b,c): # defining Newton's method
    d = 10**(-10)
    x = 6
    n = 2
    while abs(n - x) > d:
        n, x = x - (x**3 + a*x**2 + b*x + c)/(3*x**2 + 2*a*x + b), n
    value = [n, abs(n-x)] # "n" is the approximate solution
    return value          # abs(n-x) is the error
    
def main():
    # looping the function 
    while True:

        try: # user input should be an integer

            a = int(input("Enter the integer coefficient of x^2: ")) 
            b = int(input("Enter the integer coefficient of x: "))  
            c = int(input("Enter the integer constant term: ")) 

            newt = newton(a,b,c) # alloting variable "newt" to calling of the function
            
            # if coefficient -ve/+ve then the equation should be printed that way
            nums = [a,b,c]
            for i in range(len(nums)):
                if nums[i] > 0: # if coefficient +ve, print plus sign
                    nums[i] = "+"+str(nums[i])
                else: # if coefficient -ve, print user input as it is 
                    nums[i] = str(nums[i])

            a = nums[0]
            b = nums[1]
            c = nums[2]

            # if coefficient is 0 then the variable should not be printed
            # creating different conditions that will print different statements
            if int(a) == 0 and int(b) != 0 and int(c) != 0:
                print("The approximate solution of x^3",b,"x",c,": ",float(newt[0]), sep='')
            if int(b) == 0 and int(a) != 0 and int(c) != 0:
                print("The approximate solution of x^3",a,"x^2",c,": ",float(newt[0]), sep='')
            if int(c) == 0 and int(a) != 0 and int(c) != 0:
                print("The approximate solution of x^3",a,"x^2",b,"x",": ",float(newt[0]), sep='')
            if int(a) == 0 and int(b) == 0 and int(c) != 0:
                print("The approximate solution of x^3",c,": ",float(newt[0]), sep='')
            if int(a) == 0 and int(c) == 0 and int(b) != 0:
                print("The approximate solution of x^3",b,"x",": ",float(newt[0]), sep='')
            if int(b) == 0 and int(c) == 0 and int(a) != 0:
                print("The approximate solution of x^3",a,"x^2",": ",float(newt[0]), sep='')
            if int(a) == 0 and int(b) == 0 and int(c) == 0:
                print("The approximate solution of x^3: ",float(newt[0]), sep='')
            if int(a) != 0 and int(b) != 0 and int(c) != 0:
                print("The approximate solution of x^3",a,"x^2",b,"x",c,": ",float(newt[0]), sep='')

            print("The error is",float(newt[1]))
            
        except ValueError as msg: # user did not enter an integer
            print(msg, "--please enter an integer!")

        except EOFError: # if user wants to quit then help them
            break
main()
