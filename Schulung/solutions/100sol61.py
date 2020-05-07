%%file my_script_args.py
#run this in a terminal, 
import sys
def usage():
    print('''usage: python my_script_args.py --version|-n ##
            where ## is a positive integer
    ''')
if len(sys.argv) == 1:
    usage()
    exit(1)
if len(sys.argv) == 2:
    if sys.argv[1] == '--version':
        print('0.1')
        exit(0)
    else:
        usage()
        exit(1)
if len(sys.argv) == 3: 
    if sys.argv[1] == '-n':
        n=0
        try:
            n=int(sys.argv[2])
        except:
            usage()
            exit(1)
        for i in range(1,n+1):
            print(i)
        exit(0)
    else:
        usage()
        exit(1)
if len(sys.argv) > 3:
    print('3 arguments detected')
    usage()
    exit(1)

#print( sys.argv)
