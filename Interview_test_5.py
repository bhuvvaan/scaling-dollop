bracket_string = input().split()
left_brackets = {'(':1,'{':2,'[':3}
right_brackets = {')':1,'}':2,']':3}
m = 0
while m < len(bracket_string):
    item = bracket_string[m]
    i = 0
    outer_loop_breaker = False
    left = []
    count = 0
    while i < len(item):
        if i == 0 and item[0] in right_brackets.keys():
            print('NO')
            break
        if len(item)%2 != 0:
            print('NO')
            break
        if item[i] in left_brackets.keys():
            left.append(item[i])
            count += 1 
            try:
                if item[i+1] in right_brackets.keys():
                    if right_brackets[item[i+1]] == left_brackets[item[i]]:
                        for k in range(count):
                            if right_brackets[item[i-k+count]] != left_brackets[left[k]]:    
                                print('NO')
                                outer_loop_breaker = True
                                break
                        else:
                            i = i+count
                            left = []
                            count = 0
                        if outer_loop_breaker:
                            break
                    else:
                        print('NO')
                        break
                else:
                    i += 1
                    continue
            except IndexError:
                print('NO')
                break
        i += 1
    else:
        print('YES')
    m += 1
