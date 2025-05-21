def fullpyramid(n):
    for i in range(1,n+1):
        for j in range(1, n+1):
            print("$", end=" ")
        print()
n=5
fullpyramid(n)

def left_and_right_triangle(n):
    for i in range(1, n+1):
        left = "*" * i
        right = "*" * i
        print(left.ljust(n) + right.rjust(n))
left_and_right_triangle(5)