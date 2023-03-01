# define a function that takes a number(n)
# return a dictonary that returns cube from 1 to n

def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i]=i**3
    return cubes

print(cube_finder(10))
