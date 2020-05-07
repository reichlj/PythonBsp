with open('bundeslaender.txt',encoding='ISO-8859-1') as fh:
    fh.readline()
    max_size = 15000
    small_states = []
    for line in fh:
        state, size_of_state, *rem =  line.split()
        size_of_state = float(size_of_state)
        if size_of_state < max_size:
            small_states.append(state)
    
print(small_states)
