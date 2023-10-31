num = input("Enter number: ")
lt = []
num = int(num)
lt2 = []
for i in range(num):
    num2 = input("Enter Number into: ")
    num2 = int(num2)
    for j in range(num2):
        n = input("Enter the Name: ")
        lt2.append(n)
    lt.append(lt2)
    lt2 = []
print(lt)


