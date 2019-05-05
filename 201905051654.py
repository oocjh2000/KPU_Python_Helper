import random
def avr(n,m,numbers):
    loop = 0
    for i in range(n-m):
        print(sum(numbers[loop:loop+m])//m)
        loop+=1

def main():
    n = int(input())
    m = int(input())
    numbers = []
    if m > n:
        print("ERROR")
        return
    for i in range(n):
        numbers.append(random.randint(0,100))
    avr(n,m,numbers)

if __name__ == "__main__":
    main()
