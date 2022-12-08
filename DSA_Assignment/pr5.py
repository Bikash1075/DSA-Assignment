# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def TowerOfHanoi(n, source, dest, aux):
    if n == 0:
        return
    TowerOfHanoi(n-1, source, aux, dest)
    print("Move disk", n, "from rod", source, "to rod", dest)
    TowerOfHanoi(n-1, aux, dest, source)
 
N = 3
 
TowerOfHanoi(N, 'A', 'C', 'B')
