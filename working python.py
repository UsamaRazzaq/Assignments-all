A = [10, 20, 30, 40, 50]
x = 30
size = len(A)
for i in range (0, size) :
        for j in range (i, size):
            if (A[i] + A[j] == x) :
                print(x)
