def braid_to_pd(word, n):
    '''construct list of planar link diagram crossings from an
       n-strand braid word, a list of integers representing generators'''
    
    p = list(range(1, n+1)) # current arcs in horiz positions
    k = n + 1 # next arc label to be assigned
    pd = [] # output
    
    for x in word:
        i = abs(x) - 1 # generator left strand
        
        if x > 0: # create new pd crossing
            pd.append([p[i+1], p[i], k, k+1])
        else:
            pd.append([p[i], k, k+1, p[i+1]])
        # update current arcs
        p[i], p[i+1] = k, k+1
        k += 2

    # close the braid's pd by replacing all final arcs with initial arcs
    m = {p[j]: j + 1 for j in range(n)} # get reverse hash
    return [[m[u] if u in m else u for u in c] for c in pd]



def random_word_1(n, length):
    # generates a random braid word
    if length <= 0:
        return []
    gens = list(range(-n+1,0))+list(range(1,n))
    return [random.choice(gens) for i in range(length)]

def random_word_2(n, length):
    # generates a random braid word without consecutive inverses
    if length <= 0:
        return []
    gens = list(range(-n+1,0))+list(range(1,n))
    word = [random.choice(gens)]
    for i in range(length-1):
        word.append(random.choice([x for x in gens if x != -word[-1]]))
    return word

result = []
for L in range(1,9):
    rt = []
    for i in range(100):
        word = random_word_1(4, L)
        crossings = braid_to_pd(word, 4)
        pd = PlanarDiagram(crossings)
        comps = pd.find_components()
        jp = jones(pd)
        terms = len(sympy.Add.make_args(sympy.expand(jp)))
        rt.append((len(comps),terms,))
    result.append(rt)
    print(L)

print(result)

