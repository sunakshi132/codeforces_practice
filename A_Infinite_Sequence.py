def gen_series(index_):
    num_1 = int((-1 + (1 + (4*2*index_))**0.5)/2)
    sum_1 = num_1*(num_1+1)/2
    num_2 = num_1+1
    sum_2 = num_2*(num_2+1)/2
    if sum_1 == index_:
        ans = num_1
    elif sum_2 >= index_:
        ans = index_ - sum_1
    return ans

if __name__ == '__main__':
    x = int(input())
    print gen_series(index_=x) 