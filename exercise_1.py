# Enter Two Integers - If divisable by 2 or 3 return their multiplication, 
# else return sum

a, b = input('Enter two integers:').split()

#string to be used after divisibility is calculated
endString = 'Divisble by 2 or 3({0}, {1}) => {2}'

#Convert input to integer type
num1 = int(a)
num2= int(b)

#Sum & Mult of input
sumNum = num1 + num2
multNum = num1 * num2

#if not divisible by 3 or 2 return false
if(sumNum % 3) == 0 or (sumNum % 2) == 0:
    print(endString.format(num1, num2, multNum))
else:
    print(endString.format(num1, num2, sumNum))
