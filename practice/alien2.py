t = int(input())

for i in range(t):
    n = int(input())
    word_list = [str(input()) for i in range(n)]
    last_word = [i[-1] for i in word_list]
    if len(last_word) == len(set(last_word)):
        # no repeat accent
        ans = 0
        continue
    else:
        diff_last = list(set(last_word))
        b = []
        for last_letter in diff_last:
            a = [i for i in word_list if i[-1] == last_letter]
            j = 2
        while j<4:
            c = [i[-j:] for i in a]
            d = {i:c.count(i) for i in set(c)}
            e = []
            f = []
            for key, value in d:
                if value == 1:
                    e.append(key)
                if value == 2 or value == 3:
                    ans += 2
                    f.append(key)
                if len(e) > 1:
                    ans += 2
            print(d)
            if len(c) == len(set(c)):
                continue
                # else:
            j+=1


    # last_set = set(last_word)
