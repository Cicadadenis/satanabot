gg = open('ussers.txt', 'r').readlines()
if len(gg) > 100:
    for x in range(0, len(gg), 100):
        print(gg[x:x+100])
