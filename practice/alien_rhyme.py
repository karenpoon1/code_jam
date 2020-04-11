t = int(input())

for i in range(t):
    n = int(input())
    word_list = [(i,str(input())) for i in range(n)]
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
            while len(a) > 0:
                
    print(word_list)
    


    # ans = 0
    # i = 0
    # while len(word_list) > 0:
    # # for i in range(n):
    #     for j in range(len(word_list)):
    #         pair = 0
    #         if word_list[i] !=  word_list[j] and word_list[j][-1] == word_list[i][-1] and word_list[j][-2] != word_list[i][-2]:
    #             word_list.remove(word_list[j])
    #             if not pair:
    #                 pair = 1
        
    #     word_list.remove(word_list[i])
    #     ans += pair
    #     i += 1
    
