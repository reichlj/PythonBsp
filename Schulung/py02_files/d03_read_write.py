with open('yellow_snow.txt') as fh:
    for line in fh:
        print(line.rstrip())
        
with open('yellow_snow.txt') as fobj_in:
    with open('yellow_snow2.txt','w') as fobj_out:
        counter = 0
        for line in fobj_in:
            fobj_out.write(str(counter) + ': ' + line)
            counter += 1
        
