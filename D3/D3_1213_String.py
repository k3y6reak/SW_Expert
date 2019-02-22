import re

def main():
    for t in range(10):
        tc = input()
        pattern = input()
        line = input()
        regex = re.compile(pattern)
        match = regex.findall(line)
        print("#" + str(tc), len(match))

if __name__ == '__main__':
    main()


