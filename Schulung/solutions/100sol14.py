def mymean(*args):
    accumulator = 0
    counter = 0
    for a in args:
       accumulator += a
       counter += 1
    print('sum(args): ', sum(args))
    print('len(args): ', len(args))
    print('type(args): ', type(args))
    return accumulator/counter  # in Py3 division defaults to float div
                                # for Py2 cast to float
#%%
print(mymean(1,5.5))
print(mymean(1,5, -3))
