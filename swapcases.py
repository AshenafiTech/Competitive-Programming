def swap_case(s):
    n = []
    for c in s:
        if c.isalpha():
            if c.islower():
                n.append(c.upper())
            else:
                n.append(c.lower())  
        else:
            n.append(c)
            
    return ''.join(n)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)