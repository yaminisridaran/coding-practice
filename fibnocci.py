def fib(n):
   a, b = 0,1
   while a <= n:
       yield a
       a, b = b, a+b

def main():
    g = fib(5)
    for i in g :
        print("value", i)


if __name__ == "__main__":
    main()
