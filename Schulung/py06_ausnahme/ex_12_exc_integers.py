try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
    print(i)
except (IOError,ValueError):
    print('An I/O error or a ValueError has occurred')
except:
    print('An unexpected error occurred')
    raise    