n = int(input('please give n: '))

if n <= 0:
    print('not a positive value:', n)
else: # comment to illustrate git use
    result = 1
    while n > 1:
        result *= n
        n -= 1

    print(result) # another small change