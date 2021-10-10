def ugly(n):
    if n%2==0 or n%3==0 or n%5==0:
        for x in range(7, n):
            if x == 7 and n % 7 == 0: return False
            if n % x == 0:
                if ugly(x):
                    return True
                else:
                    return False
    else: return False
    return True


def ugly_number():
    n = 11
    num = 15
    while n<1500:
        ugly2 = True
        num += 1
        if num%2==0 or num%3==0 or num%5==0:
            for x in range(7, num):
                if x==7 and num%7==0:
                    ugly2 = False
                    break
                if num%x==0:
                    if not ugly(x):
                        ugly2 = False
                        break
            if ugly2:
                n += 1
                print(num)
        if n==1500:
            return f"The 1500'th ugly number is {num}."

# print(ugly_number())  # == 860934420
# 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25


