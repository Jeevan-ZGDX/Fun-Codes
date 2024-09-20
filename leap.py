def is_leap(year):
    leap = False
    
    # Write your logic here
    # If we can divide they year by 4, it's probably a leap year
    if year%4 == 0:
        leap = True

    # But every 100 years we skip a leap year
    if year%100 == 0:
        # when true it also means the year is divisible by 100
        # so we can skip checking those conditions
        leap = False

    # Unless the year is also divisible by 400
    if year%400 == 0:
        # when true it also means the year is divisible by 100 and by 4
        # so we can skip checking those conditions
        leap = True
    return leap

year = int(input())
print(is_leap(year))
