
lt = [12, 23, 34, 45, 56, 67, 78, 89, 90, 26]
lt2 = []
lt3 = []
lt4 = []
#num2 = input("Enter Number into: ")
#num2 = int(num2)
#for j in range(num2):
#    n = input("Enter the Number: ")
#    n = int(n)
#    lt.append(n)
print(lt)
k = input("Enter the number of k you want: ")
k = int(k)
for i in range(0,len(lt),k):
    lt1 = lt[i:i + k]
    total = sum(lt[i:i+k])
    mean = total/ len(lt[i:i+k])
    lt2.append(lt1)
    lt3.append(mean)
print(lt2)
print(lt3)

