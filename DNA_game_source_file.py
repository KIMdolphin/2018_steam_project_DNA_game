print('□□□□■■■■■□□■■□□□■□□□■■□□□□□')
print('□□□□■□□□□■□■□■□□■□□■□□■□□□□')
print('□□□□■□□□□■□■□■□□■□■□□□□■□□□')
print('□□□□■□□□□■□■□□■□■□■■■■■■□□□')
print('□□□□■□□□□■□■□□□■■□■□□□□■□□□')
print('□□□□■■■■■□□■□□□□■□■□□□□■□□□')
print('□□□□□□□□□□□□□□□□□□□□□□□□□□□')
print('□■■■■□□□□■■□□□■■■■■■□■■■■■■')
print('■□□□□■□□■□□■□□■□■■□■□■□□□□□')
print('■□□□□□□■□□□□■□■□■■□■□■■■■■■')
print('■□■■■■□■■■■■■□■□■■□■□■□□□□□')
print('■□□□□■□■□□□□■□■□■■□■□■□□□□□')
print('□■■■■□□■□□□□■□■□■■□■□■■■■■■')
print('='*17)
print('DNA 게임에 오신 것을 환영합니다!')
user = input('전사 게임을 하시려면 1, 복제 게임을 하시려면 2, 번역 게임을 체험하시려면 3를 눌러주세요.')
n=0
#복제복제복제 
def bockjae(n):    
    print('='*17)
    import random

    b = []
    c = []
    d = []
    e = []
    s=0

    for i in range(n):
        dnalist4 = ['A','T','G','C','A','T','G','C','A','T','G','C','A','T','G','C'] #염기서열을 생성합니다 
        a = random.sample(dnalist4, 4)
        b = a + b

    print('                                                  ',''.join(b))

    dnadic = ['A','T', 'C', 'G']


    for j in range(len(b)): #문제의 답을 만듭니다. 그리고는 c리스트에 추가합니다 
        if b[j] == dnadic[0]:
            c.append('T')
        elif b[j] == dnadic[1]:
            c.append('A')
        elif b[j] == dnadic[2]:
            c.append('G')
        elif b[j] == dnadic[3]:
            c.append('C')
        
    for o in range(4):
        if o<3:
            useranswer = input('이 배열과 상보적인 염기를 입력하세요 :')
            useranswerlist = list(useranswer) #사용자의 답을 입력받습니다.
            print('='*50)
    
            count = 0


    
            for k in range(len(useranswerlist)):
                if len(useranswerlist) == len(c):
                    if useranswerlist[k] == c[k]:
                        count = count + 1 #정답이 맞으면 count를 하나씩 추가합니다. 이 count 수가 리스트 개수의 수와 동일하다면 계속 더해줍니다!
                    if count == len(useranswerlist):
                            print('모두 정답입니다. 당신의 복제는 안전합니다.')
                            replayRNA = input('다시 이 게임을 하려면 0을 입력해주세요.')
                            outf = open('score.txt.', 'a')
                            outf.write('='*50)
                            outf.write('\n')
                            outf.write('문제 :')
                            outf.write(''.join(b))
                            outf.write('\n')
                            outf.write('당신은 ')
                            outf.write(str(o))
                            outf.write('번 시도하여 복제 문제를 풀었습니다. (3번 시도는 실패)\n')
                            outf.write('='*25)
                            outf.close()
                            if replayRNA == '0':
                                junsa(n)
                    elif useranswerlist[k] != c[k]:
                        dnadic2 = ['A','T', 'C', 'G']
                        dnadic2.remove(c[k])
                        withoutdict = dict(zip(dnadic2,range(3)))
                        if useranswerlist[k] in withoutdict:
                            d.append(k)
                        else:
                            e.append(k)
                else :
                    print('염기의 수가 맞지 않아요. ')
                    break


            da = []
            gcon = 0
        
            for g in range(len(d)+1):
                if len(d) !=0 and gcon < len(d):
                    g1 = int(d[g])+1
                    da.append(str(g1))
                    gcon = gcon + 1 
                elif len(d) ==0:
                    break
                else:
                    print('상보적인 염기 오류 : ',', '.join(da),'번째')

                
    
            ea = []
            ncon = 0
                
            for u in range(len(e)+1):
                if len(e) !=0 and ncon < len(e):
                    n1 = int(e[u])+1
                    ea.append(str(n1))
                    ncon = ncon +1
                elif len(e) ==0:
                    break
                else :
                    print('염기 이외 입력 :', ', '.join(ea),'번째')

            print('='*50)
            o = o+1
            print('                                                  ',''.join(b))

        else:
            print('                                             답: ',''.join(c))
            print('주어진 기회가 모두 끝났습니다.')
            print('당신의 DNA가 이상해졌습니다. ')
            outf = open('score.txt.', 'a')
            outf.write('='*50)
            outf.write('\n')
            outf.write('문제 :')
            outf.write(''.join(b))
            outf.write('\n')
            outf.write('당신은 ')
            outf.write(str(o))
            outf.write('번 시도하여 복제 문제를 풀었습니다. (3번 시도는 실패)\n')
            outf.write('='*25)
            outf.close()
            replayRNA = input('다시 이 게임을 하려면 0을 입력해주세요.')
            if replayRNA == '0':
                bockjae(n)
            else :
                print('게임 종료')

    
def junsa(n):
    
    print('='*17)
    import random

    b = []
    c = []
    d = []
    e = []
    s=0

    for i in range(n):
        dnalist4 = ['A','T','G','C','A','T','G','C','A','T','G','C','A','T','G','C'] #염기서열을 생성합니다 
        a = random.sample(dnalist4, 4)
        b = a + b

    print('                                                  ',''.join(b))

    dnadic = ['A','T', 'C', 'G']


    for j in range(len(b)): #문제의 답을 만듭니다. 그리고는 c리스트에 추가합니다 
        if b[j] == dnadic[0]:
            c.append('U')
        elif b[j] == dnadic[1]:
            c.append('A')
        elif b[j] == dnadic[2]:
            c.append('G')
        elif b[j] == dnadic[3]:
            c.append('C')
        
    for o in range(4):
        if o<3:
            useranswer = input('이 배열과 상보적인 염기를 입력하세요 :')
            useranswerlist = list(useranswer) #사용자의 답을 입력받습니다.
            print('='*50)
    
            count = 0


    
            for k in range(len(useranswerlist)):
                if len(useranswerlist) == len(c):
                    if useranswerlist[k] == c[k]:
                        count = count + 1 #정답이 맞으면 count를 하나씩 추가합니다. 이 count 수가 리스트 개수의 수와 동일하다면 계속 더해줍니다!
                    if count == len(useranswerlist):
                            print('모두 정답입니다. 당신의 전사는 안전합니다.')
                            outf = open('score.txt.', 'a')
                            outf.write('='*50)
                            outf.write('\n')
                            outf.write('문제 :')
                            outf.write(''.join(b))
                            outf.write('\n')
                            outf.write('당신은 ')
                            outf.write(str(o))
                            outf.write('번 시도하여 전사 문제를 풀었습니다. (3번 시도는 실패)\n')
                            outf.write('='*25)
                            outf.close()
                            replayRNA = input('다시 이 게임을 하려면 0을 입력해주세요.')
                            if replayRNA == '0':
                                junsa(n)
                    elif useranswerlist[k] != c[k]:
                        dnadic2 = ['A','U', 'C', 'G']
                        dnadic2.remove(c[k])
                        withoutdict = dict(zip(dnadic2,range(3)))
                        if useranswerlist[k] in withoutdict:
                            d.append(k)
                        else:
                            e.append(k)
                else :
                    print('염기의 수가 맞지 않아요. ')
                    break


            da = []
            gcon = 0
        
            for g in range(len(d)+1):
                if len(d) !=0 and gcon < len(d):
                    g1 = int(d[g])+1
                    da.append(str(g1))
                    gcon = gcon + 1 
                elif len(d) ==0:
                    break
                else:
                    print('상보적인 염기 오류 : ',', '.join(da),'번째')

                
    
            ea = []
            ncon = 0
                
            for w in range(len(e)+1):
                if len(e) !=0 and ncon < len(e):
                    n1 = int(e[w])+1
                    ea.append(str(n1))
                    ncon = ncon +1
                elif len(e) ==0:
                    break
                else :
                    print('염기 이외 입력 :', ', '.join(ea),'번째')

            print('='*50)
            o = o+1
            print('                                                  ',''.join(b))


        else:
            print('                                             답: ',''.join(c))
            print('주어진 기회가 모두 끝났습니다.')
            print('당신의 전사과정이 이상해졌습니다. ')
            outf = open('score.txt.', 'a')
            outf.write('='*50)
            outf.write('\n')
            outf.write('문제 :')
            outf.write(''.join(b))
            outf.write('\n')
            outf.write('당신은 ')
            outf.write(str(o))
            outf.write('번 시도하여 전사 문제를 풀었습니다. (3번 시도는 실패)\n')
            outf.write('='*25)
            outf.close()
            replayRNA = input('다시 이 게임을 하려면 0을 입력해주세요.')
            if replayRNA == '0':
                bockjae(n)
            else :
                print('게임 종료')


def bunyuck(n):
    aa = []
    aminoanswer = []
    z=0
    for p in range(n):
        if z ==0:
            aa.append('AUG')
            z+=1
        elif n-1>z>0:
            import random
            mRNA = ['A','U','G','C','A','U','G','C','A','U','G','C'] #염기서열을 생성합니다 
            a = random.sample(mRNA, 3)
            aa.append(''.join(a))
            z+=1
        elif n-1==z:
            import random
            finish = ['UAG', 'UAA', 'UGA']
            a = random.sample(finish, 1)
            aa.append(a[0])
            z+=1

    amino = {'UU':['페닐알라닌', '류신'], 'UC':['세린'], 'UA':['타이로신'], 'UG':['시스테인', '트립토판'], 'CU':['류신'], 'CC':['프롤린'], 'CA':['히스티딘', '글루타민'], 'CG':['아르지닌'], 'AU':['아이소류신'],'AC':['트레오닌'], 'AA':['아스파라진', '라이신'], 'AG':['세린' ,'아르지닌'], 'GU':['발린'], 'GC':['알라닌'], 'GA':['아스파트산', '글루탐산'], 'GG':['글라이신']}
    for y in range(n):
        if aa[y] == 'AUG':
            aminoanswer.append('메싸이오닌')
        elif aa[y] == 'UGG':
            aminoanswer.append('트립토판')
        elif aa[y] == 'UGA':
            aminoanswer.append('종결코돈')
        elif aa[y] ==  'UAG':
            aminoanswer.append('종결코돈')
        elif aa[y] == 'UAA':
            aminoanswer.append('종결코돈')
        elif len(amino.get(aa[y][0:2]))==2:
            if aa[y][2]=='C':
                aminoanswer.append(''.join(amino.get(aa[y][0:2])[0]))
            elif aa[y][2]=='U':
                aminoanswer.append(''.join(amino.get(aa[y][0:2])[0]))
            elif aa[y][2]== 'A':
                aminoanswer.append(''.join(amino.get(aa[y][0:2])[1]))
            elif aa[y][2]== 'G':
                aminoanswer.append(''.join(amino.get(aa[y][0:2])[1]))
        elif len(amino.get(aa[y][0:2]))==1:
            if aa[y] !=  'UAG' and 'UAA':
                    aminoanswer.append(''.join(amino.get(aa[y][0:2])))
                
    print('<','                      ', ''.join(aa),'>')   

    for o in range(4):
        if o<3:
            useranswer = input('이 염기서열에 대한 알맞는 아미노산을 한 칸씩 띄어서 입력하세요. ex)페닐알라닌 류신')
            useranswerlist = useranswer.split(' ')
            print('='*50)
    
            count = 0
            d = []
            e = []

            for k in range(len(useranswerlist)):
                if len(useranswerlist) == len(aminoanswer):
                    if useranswerlist[k] == aminoanswer[k]:
                         count = count + 1 #정답이 맞으면 count를 하나씩 추가합니다. 이 count 수가 리스트 개수의 수와 동일하다면 계속 더해줍니다!
                    if count == len(useranswerlist):
                         print('모두 정답입니다. 당신의 번역은 안전합니다.')
                         outf = open('score.txt.', 'a')
                         outf.write('='*50)
                         outf.write('\n')
                         outf.write('문제 :')
                         outf.write(''.join(aa))
                         outf.write('\n')
                         outf.write('당신은 ')
                         outf.write(str(o))
                         outf.write('번 시도하여 번역 문제를 풀었습니다. (3번 시도는 실패)\n')
                         outf.write('='*25)
                         outf.close()
                         replay = input('다시 이 게임을 하려면 0을 입력해주세요.')
                         if replay == '0':
                             bunyuck(n)
                         else :
                             print('게임 종료')
                    elif useranswerlist[k] != aminoanswer[k]:
                         aminodic = ['페닐알라닌','류신', '세린', '타이로신','시스테인', '종결코돈', '프롤린', '히스티딘', '글루타민', '아르지닌', '아이소류신', '메싸이오닌', '트레오닌', '아스파라진', '라이신', '발린', '알라닌', '아스파트산', '글루탐산','글라이신']
                         aminodic.remove(aminoanswer[k])
                         withoutdict = dict(zip(aminodic,range(len(aminodic))))
                         if useranswerlist[k] in withoutdict:
                             d.append(k)
                         else:
                             e.append(k)
                else :
                        print('아미노산의 수가 맞지 않아요. ')
                        break

            


            da = []
            gcon = 0
        
            for g in range(len(d)+1):
                if len(d) !=0 and gcon < len(d):
                    g1 = int(d[g])+1
                    da.append(str(g1))
                    gcon = gcon + 1 
                elif len(d) ==0:
                    break
                else:
                    print('아미노산 오류 : ',', '.join(da),'번째')

                
    
            ea = []
            ncon = 0
                
            for w in range(len(e)+1):
                if len(e) !=0 and ncon < len(e):
                    n1 = int(e[w])+1
                    ea.append(str(n1))
                    ncon = ncon +1
                elif len(e) ==0:
                    break
                else :
                    print('아미노산 존재하지 않음 :', ', '.join(ea),'번째')

            print('='*50)
            o = o+1
            print('                                                  ',''.join(aa))

    else:
            print('                                             답: ',' '.join(aminoanswer))
            print('주어진 기회가 모두 끝났습니다.')
            print('당신의 번역과정이 이상해졌습니다. ')
            outf = open('score.txt.', 'a')
            outf.write('='*50)
            outf.write('\n')
            outf.write('문제 :')
            outf.write(''.join(aa))
            outf.write('\n')
            outf.write('당신은 ')
            outf.write(str(o))
            outf.write('번 시도하여 번역 문제를 풀었습니다. (3번 시도는 실패)\n')
            outf.write('='*25)
            outf.close()
            replay = input('다시 이 게임을 하려면 0을 입력해주세요.')
            if replay == '0':
                bunyuck(n)
            else :
                print('게임 종료')



if user == '2':
    n = int(input('1세트 추가당 염기 4개씩 추가됩니다. 몇 세트를 하시겠습니까? :'))
    bockjae(n)
elif user == '1':
    n = int(input('1세트 추가당 염기 4개씩 추가됩니다. 몇 세트를 하시겠습니까? :'))
    junsa(n)
elif user == '3':
    n = int(input('1세트 추가당 코돈 1개씩 추가됩니다. 몇 세트를 하시겠습니까?(기본 2세트 이상) :'))
    bunyuck(n)

