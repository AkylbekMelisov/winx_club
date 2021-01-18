def hulk(n):
    hulk_say = ''
    for i in range(1,n+1):
        if i % 2 == 0:
            hulk_say += 'I love it '
        else:
            hulk_say += 'I hate it '
    count_it = hulk_say.count('it')-1
    hulk_say = hulk_say.replace('it','that',count_it)
    print(hulk_say)
hulk(int(input()))