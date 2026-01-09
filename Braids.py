def braid_to_pd(word, n):
    '''construct list of planar link diagram crossings from an
       n-strand braid word, a list of integers representing generators'''
    
    p = list(range(1, n+1)) # current arcs in horiz positions
    k = n + 1 # next arc label to be assigned
    pd = [] # output
    
    for x in w:
        i = abs(x) - 1 # generator left strand
        
        if x > 0: # create new pd crossing
            pd.append([p[i+1], p[i], k, k+1])
        else:
            pd.append([p[i], k, k+1, p[i+1]])

        k += 2
        # update current arcs
        p[i], p[i+1] = k, k+1

    # close the braid's pd by replacing all final arcs with initial arcs
    m = {p[j]: j + 1 for j in range(n)} # get reverse hash
    return [[m[u] if u in m else u for u in c] for c in pd]
