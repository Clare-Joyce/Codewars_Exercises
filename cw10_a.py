def find(n):
    # Code here
    sum = 0
    for i in range(1, n):
        if i%3 == 0 or i %5 == 0:
            sum = sum + i
        else:
            pass
    if n%3 == 0 or n %5 == 0:
        sum = sum + n
    else:
        pass
  
    return sum