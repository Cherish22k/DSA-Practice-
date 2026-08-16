n = int(input("Enter how many numbers: "))

sum = 0

for i in range(n):
    num = float(input("Enter number: "))
    sum = sum + num

average = sum / n

print("Average =", average)
