def solution(priorities, location): #인쇄 순서 계산 함수
    queue = []
    result = []
    i = 0
    
    for p in priorities:
        queue.append((p, i))
        i += 1

    while queue:
        I = 0
        j = queue.pop(0)
        for index in range(len(queue)):
            if j[0] >= queue[index][0]:
                pass
            else:
                I += 1
        if I == 0:
            result.append(j)
        else:
            queue.append(j)
        
    answer = result.index((priorities[location], location)) + 1
    return answer

if __name__ == '__main__': #메인 프로그램
    
    p1 = [2, 1, 3, 2]
    p2 = [1, 1, 9, 2, 3, 4]
    p3 = [1, 1, 2, 1, 1, 1]

    print('인쇄 순서 출력:\n')
    print(p1,'\n', solution(p1, 2))
    print(p2,'\n', solution(p2, 1))
    print(p3,'\n', solution(p3, 0))