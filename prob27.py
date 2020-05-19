#I hate being alive
import time
dataset = []
loopbreak = time.time() + 1
vowels = 'IAEOU'
try:
    while loopbreak > time.time():
        dataset.append(input())
        loopbreak = time.time() + 1
except EOFError:
    for i in range(0, len(dataset)):
        num = dataset[i]
        num = int(num[0])
        string = dataset[i]
        string2 = ''
        for k in range(2, len(string)):
            char = string[k]
            string2 = string2 + char
        if num == 0:
            break
        
        elif num == 2:
            word1, word2 = string2.split()
            word2_2 = ''
            for d in range(1, len(word1)):
                char = word1[d]
                word2_2 = word2_2 + char
            if word1 == word2:
                print(string2, ' COPY')
                continue
                #copy
            elif word2 == 'SHM' + word1 or word2 == 'SHM' + word2_2:
                print(string2, ' SHM')
                continue
                #SHM
            else:
                word1_1 = ''
                word2_1 = ''
                for t in range(0, len(word1)):
                    char = word1[t]
                    if char in vowels:
                        word1_1 = word1_1 + char
                for t in range(0, len(word2)):
                    char = word2[t]
                    if char in vowels:
                        word2_1 = word2_1 + char
                if word1_1 == word2_1:
                    print(string2, ' RHYMING')
                    continue
                elif word1_1 == 'I':
                    print(string2, ' PROGRESSIVE')
                    continue
                elif word1_1 == 'A':
                    if word2_1 == 'I':
                        print(string2, ' ABLAUT')
                        continue
                    else:
                        print(string2, ' PROGRESSIVE')
                        continue
                elif word1_1 == 'E':
                    if word2_1 == 'I' or word2_1 == 'A':
                        print(string2, ' ABLAUT')
                        continue
                    else:
                        print(string2, ' PROGRESSIVE')
                        continue
                elif word1_1 == 'O':
                    if word2_1 == 'I' or word2_1 == 'A' or word2_1 == 'E':
                        print(string2, ' ABLAUT')
                        continue
                    else:
                        print(string2, ' PROGRESSIVE')
                        continue
                elif word1_1 == 'U':
                    print(string2, ' ABLAUT')
                    continue
                    
                elif len(word1_1) == 2:
                    let1 = word1_1[0]
                    let12 = word1_1[1]
                    
                    let2 = word2_1[0]
                    let22 = word2_1[1]
                    if let1 == let2:
                        if let12 == 'I':
                            print(string2, ' PROGRESSIVE')
                            continue
                        elif let12 == 'A':
                            if let22 == 'I':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let12 == 'E':
                            if let22 == 'I' or let22 == 'A':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let12 == 'O':
                            if let22 == 'I' or let22 == 'A' or let22 == 'E':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let12 == 'U':
                            print(string2, ' ABLAUT')
                            continue
                        
                    if let12 == let22:
                        if let1 == 'I':
                            print(string2, ' PROGRESSIVE')
                            continue
                        elif let1 == 'A':
                            if let2 == 'I':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let1 == 'E':
                            if let2 == 'I' or let2 == 'A':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let1 == 'O':
                            if let2 == 'I' or let2 == 'A' or let2 == 'E':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let1 == 'U':
                            print(string2, ' ABLAUT')
                            continue
                    
        elif num == 3:
            word1, word2, word3 = string2.split()
            if word1 == word2 and word2 == word3:
                print(string2, ' COPY')
                #copy
            else:
                word1_1 = ''
                word2_1 = ''
                word3_1 = ''
                for t in range(0, len(word1)):
                    char = word1[t]
                    if char in vowels:
                        word1_1 = word1_1 + char
                for t in range(0, len(word2)):
                    char = word2[t]
                    if char in vowels:
                        word2_1 = word2_1 + char
                for t in range(0, len(word3)):
                    char = word3[t]
                    if char in vowels:
                        word3_1 = word3_1 + char
                if word1_1 == word2_1 and  word2_1 == word3_1:
                    print(string2, ' RHYMING')
                elif word1_1 == 'I':
                    print(string2, ' PROGRESSIVE')
                    continue
                elif word1_1 == 'A':
                    if word2_1 == 'I':
                        print(string2, ' ABLAUT')
                        continue
                    else:
                        print(string2, ' PROGRESSIVE')
                        continue
                elif word1_1 == 'E':
                    if word2_1 == 'I' or word2_1 == 'A':
                        print(string2, ' ABLAUT')
                        continue
                    else:
                        print(string2, ' PROGRESSIVE')
                        continue
                elif word1_1 == 'O':
                    if word2_1 == 'I' or word2_1 == 'A' or word2_1 == 'E':
                        print(string2, ' ABLAUT')
                        continue
                    else:
                        print(string2, ' PROGRESSIVE')
                        continue
                elif word1_1 == 'U':
                    print(string2, ' ABLAUT')
                    continue
                    
                elif len(word1_1) == 2:
                    let1 = word1_1[0]
                    let12 = word1_1[1]
                    
                    let2 = word2_1[0]
                    let22 = word2_1[1]
                    if let1 == let2:
                        if let12 == 'I':
                            print(string2, ' PROGRESSIVE')
                            continue
                        elif let12 == 'A':
                            if let22 == 'I':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let12 == 'E':
                            if let22 == 'I' or let22 == 'A':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let12 == 'O':
                            if let22 == 'I' or let22 == 'A' or let22 == 'E':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let12 == 'U':
                            print(string2, ' ABLAUT')
                            continue
                
        elif num == 4:
            word1, word2, word3, word4 = string2.split()
            if word1 == word2 and word2 == word3 and word3 == word4:
                print(string2, ' COPY')
                #copy
            else:
                word1_1 = ''
                word2_1 = ''
                word3_1 = ''
                word4_1 = ''
                for t in range(0, len(word1)):
                    char = word1[t]
                    if char in vowels:
                        word1_1 = word1_1 + char
                for t in range(0, len(word2)):
                    char = word2[t]
                    if char in vowels:
                        word2_1 = word2_1 + char
                for t in range(0, len(word3)):
                    char = word3[t]
                    if char in vowels:
                        word3_1 = word3_1 + char
                for t in range(0, len(word4)):
                    char = word4[t]
                    if char in vowels:
                        word4_1 = word4_1 + char
                if word1_1 == word2_1 and word2_1 == word3_1 and word3_1 == word4_1:
                    print(string2, ' RHYMING')
                elif word1_1 == 'I':
                    print(string2, ' PROGRESSIVE')
                    continue
                elif word1_1 == 'A':
                    if word2_1 == 'I':
                        print(string2, ' ABLAUT')
                        continue
                    else:
                        print(string2, ' PROGRESSIVE')
                        continue
                elif word1_1 == 'E':
                    if word2_1 == 'I' or word2_1 == 'A':
                        print(string2, ' ABLAUT')
                        continue
                    else:
                        print(string2, ' PROGRESSIVE')
                        continue
                elif word1_1 == 'O':
                    if word2_1 == 'I' or word2_1 == 'A' or word2_1 == 'E':
                        print(string2, ' ABLAUT')
                        continue
                    else:
                        print(string2, ' PROGRESSIVE')
                        continue
                elif word1_1 == 'U':
                    print(string2, ' ABLAUT')
                    continue
                    
                elif len(word1_1) == 2:
                    let1 = word1_1[0]
                    let12 = word1_1[1]
                    
                    let2 = word2_1[0]
                    let22 = word2_1[1]
                    if let1 == let2:
                        if let12 == 'I':
                            print(string2, ' PROGRESSIVE')
                            continue
                        elif let12 == 'A':
                            if let22 == 'I':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let12 == 'E':
                            if let22 == 'I' or let22 == 'A':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let12 == 'O':
                            if let22 == 'I' or let22 == 'A' or let22 == 'E':
                                print(string2, ' ABLAUT')
                                continue
                            else:
                                print(string2, ' PROGRESSIVE')
                                continue
                        elif let12 == 'U':
                            print(string2, ' ABLAUT')
                            continue