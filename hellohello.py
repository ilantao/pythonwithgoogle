import sys

def hello(name):
    
    if name == 'Alice':
        name = name + '???'
        print 'Alert: Alice Mode'
    else:
        doesnotexist()
    name = name + '!!!'
    print 'hello', name

def main():
    hello(sys.argv[1])

if __name__ == '__main__':
    main() 