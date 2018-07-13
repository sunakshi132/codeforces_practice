def rectangle(s):
    rec_1 = max(s[0])

    for rec in xrange(1,len(s)):
        if rec_1 >= max(s[rec]):
            rec_1 = max(s[rec])
        elif rec_1 >= min(s[rec]):
            rec_1 = min(s[rec])
        else:
            return "NO"
    return "YES"

    
if __name__ == '__main__':
    recs = []
    s = input()
    for i in xrange(s):
        x = tuple(map(int,raw_input().split()))
        recs.append(x)
    print rectangle(recs)