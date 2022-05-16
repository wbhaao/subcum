
fibodata = [0] * 100
def fibo(n):
    fibodata[0] = 0;
    fibodata[1] = 1;
    i=2
    while i<=n:
        fibodata[i] = fibodata[i - 1] + fibodata[i - 2];
        i += 1
    return fibodata[n];
print(fibo(6))