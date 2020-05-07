try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
    print(i)
except IOError as err:
    (errno,strerror) = err.args
    print('I/O error({0}): {1}'.format(errno,strerror))
except ValueError:
    print('No valid integer in line.')
except Exception as e:
    print('Unexpected error:',e)
    raise    