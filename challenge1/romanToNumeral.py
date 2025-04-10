def conversion(roman):
    total = 0

    for var in roman:
        if var == 'M':
            total += 1000
        elif var == 'D':
            total += 500
        elif var == 'C':
            total += 100
        elif var == 'L':
            total += 50
        elif var == 'X':
            total += 10
        elif var == 'V':
            total += 5
        elif var == 'I':
            total += 1

    print(total)

conversion("IX")