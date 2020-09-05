# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    from collections import defaultdict
    words = defaultdict(int)
    for word in magazine:
        words[word] += 1

    for word in note:
        if words[word] == 0:
            print('No')
            return
        else:
            words[word] -= 1
    print('Yes')
        
