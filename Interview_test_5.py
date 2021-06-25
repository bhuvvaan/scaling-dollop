input_brackets_string = input().split()
left_brackets = {'(':1,'{':2,'[':3}
right_brackets = {')':1,'}':2,']':3}
i = 0
while i<len(input_brackets_string):
    item = input_brackets_string[i]
    if len(item)%2!=0:
            print('NO')
            i+=1
            continue
    j=0
    break_all_loops = False
    while j<len(item):
        if item[j] in right_brackets.keys():
            print('NO')
            break
        if item[j] in left_brackets.keys():
            k=1
            while j<len(item):
                j+=1
                try:
                    if item[j] in left_brackets.keys():
                        k+=1
                        continue
                    else:
                        l=k-1
                        w=j
                        while l>=0:
                            try:
                                if right_brackets[item[j]] == left_brackets[item[w-k+l]]:   
                                    l-=1
                                    j+=1
                                    continue
                                else:
                                    print('NO')
                                    break_all_loops = True
                                    break
                            except:
                                print('NO')
                                break_all_loops = True
                                break
                        if break_all_loops:
                            break
                except:
                    print('NO')
                    break_all_loops = True
                    break
            if break_all_loops:
                break
    else:
        print('YES!')
    i+=1    
