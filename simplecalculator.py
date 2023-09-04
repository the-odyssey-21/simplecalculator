#this program is a simple calculator
#it accepts two numbers from the input and adds them together
while True:
    print("enter a number")
    num = int(input())
    if num > 1000000:
        break
    print("enter another number")
    num2 = int(input())
    sum = num + num2
    sum_str=str(sum)
    print("the sum is:", sum_str)
print("error")

