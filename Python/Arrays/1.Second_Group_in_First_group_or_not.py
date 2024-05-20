
#In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

# Enter your code here. Read input from STDIN. Print output to STDOUT
#from collections import defaultdict

n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

for i in B:
    if i not in A:
        print(-1)
    else:
        indices = [index+1 for index, value in enumerate(A) if value == i]
        print(' '.join(map(str, indices)))
