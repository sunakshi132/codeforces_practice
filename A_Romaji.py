def ber(s):
    vowels = ['a','e','i','o','u']
    if (s[-1] != 'n') & (s[-1] not in vowels) :
        return 'NO'
    for i in xrange(len(s)-1): 
        if (s[i] not in vowels) & (s[i] != "n"):
            if s[i+1] not in vowels:
                return "NO"
        
    return 'YES'
if __name__ == '__main__':
    s = raw_input()
    print ber(s)