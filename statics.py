#statics 
def getmode(numlist) :
    num_set = set(numlist)
    num_dick = dict()
    for f in num_set :
        num_dick[f] = numlist.count(f)
    # print(num_dick)

    max_num = max(num_dick.values())
    modes = []
    for k, v in num_dick.items() :
        if v == max_num :
            # print('최빈값', k, v )
            modes.append(k)
    return modes

def getavg(numlist) :
    return sum(numlist) / len(numlist)


