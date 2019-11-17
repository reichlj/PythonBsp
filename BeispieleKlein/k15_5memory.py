memory = {0: 0, 1: 1}


def fibm(n):
    # if n not in memory:
    #     a = memory[n-2] + memory[n-1]
    #     memory[n] = a
    #     return a
    # else:
    #     return memory[n]
    #
    if n not in memory:
        memory[n] = fibm(n-2) + fibm(n-1)
    return memory[n]
