from collections import deque


# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# deque는 collections 모듈에 속해있으며, 단방향 흐름이었던 기존 Queue 자료구조(queue.Queue())와 달리, 앞 뒤(왼쪽, 오른쪽) 방향에서 삽입 삭제를 할 수 있는 자료구조이다. 
# .append() 뒤에서 추가
# .appendleft() 앞에서 추가
# .extend([a, b, c]) 뒤에서 객체를 순환하며 값들을 차례로 추가 
# .extendleft([a, b, c]) 앞에서 객체를 순환하며 값들을 차례로 추가 (!! 순차적으로 앞에서 추가되므로 객체의 마지막값이 가장 나중에 들어감 -> [c, b, a, 기존 값 ...])
# .remove() : deque안의 특정 값 삭제 
# .pop() : 오른쪽 값 삭제 후 반환 
# .popleft() : 왼쪽 값 삭제 후 반환
# .rotate() : deque안의 값들을 회전시킴
### print(dq)  # print결과 : deque([1, 2, 3, 4, 5])
### dq.rotate(1)
### print(dq)  # print결과 : deque([5, 1, 2, 3, 4])
### dq.rotate(-1)
### print(dq)  # print결과 : deque([1, 2, 3, 4, 5])
### dq.rotate(-1)
### print(dq)  # print결과 : deque([2, 3, 4, 5, 1])




# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # pop을 하는데 왼쪽에서 부터 하겠다는 뜻 , 5가 나가리됨
queue.append(1)
queue.append(4)
queue.popleft() # 2가 나가리됨

print(queue) # 들어온 순서대로 출력 
queue.reverse() # 
print(queue) # 나중에 들어온 순서대로 출력