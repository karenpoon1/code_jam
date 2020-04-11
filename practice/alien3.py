from collections import defaultdict


def words_to_rymes(words):
    suffix_dict = defaultdict(int)
    for word in words:
        for i in range(len(word)):
            suff = word[i:]
            suffix_dict[suff] += 1
    print(suffix_dict)
    res = 0
    keys = sorted(suffix_dict.keys(), key=lambda x: len(x), reverse=True)
    print(keys)
    for key in keys:
        if suffix_dict[key] > 1:
            for i in range(len(key)):
                new_key = key[i:]
                suffix_dict[new_key] -= 2
            res += 2
    return res


def main():
    num_tests = input()
    for i in range(int(num_tests)):
        num_words = int(input())
        words = []
        for _ in range(num_words):
            words.append(input())
        n_rhymes = words_to_rymes(words)
        output = "Case #{}: {}".format(i + 1, n_rhymes)
        print(output)

main()
