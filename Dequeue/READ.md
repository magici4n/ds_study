## Dequeue(Double ended queue)
____________________________________________________

- 왼쪽과 오른쪽에서 모두 삽입과 삭제가 가능한 큐
- 두가지 버전의 push와 pop 연산을 구현해야함.
- 오른쪽 push = append, 왼쪽 push = appendleft
- 오른쪽 pop = pop, 왼쪽 pop = popleft
- 나머지 다른 연산들은 Stack,Queue와 비슷하게 구현.
- Python에서는 collections라는 모듈에 deque란 클래스로 dequeu가 구현되어 있음.

#### 모듈 collections에서 Dequeue 사용
<pre>
<code>

from collections import deque
>>>d = deque('ghi')          # make a new deque with three items
>>>d.append('j')             # add a new entry to the right side
>>>d.appendleft('f')         # add a new entry to the left side
>>>d
deque(['f','g','h','i','j'])
>>>d.pop()                  # return and remove the rightmost item
'j'
>>>d.popleft()               # return and remove the leftmost item
'f'
>>>list(d)                   # list the contents of the deque
['g','h','i']
>>>print(d[0],d[-1])        # peek at leftmost, rightmost items

</code>
</pre>

#### 덱 연산 시간
- append(x) - O(1) 
- appendleft(x) - O(n)  / 블록구조 + 원형 연결리스트 기반시 O(1)
- pop() - O(1)
- popleft() - O(n)  / 블록구조 + 원형 연결리스트 기반시 O(1)
- peek() - O(1) / 앞 또는 뒤 요소 확인
- isEmpty() - O(1)
- len() - O(1)

#### dequeue.py에서 연산들 참고

#### 결론
- 양쪽 앞/뒤 에서 삽입과 삭제가 모두 가능하기 때문에 큐보다 유연하다는 장점.
- 스택처럼, 큐처럼 둘다 가능
- 그러나 똑같이 중간 요소 접근은 느림(O(n)) 따라서 인덱스 접근 시 비효율적
- 회문 검사,슬라이딩 윈도우, 양방향 탐색 등이 적합 상황
- 자주 중간 요소를 접근하거나 정렬이 필요한 경우는 비적합 상황

#### Dequeue 사용예시
1. Palinodrome 검사 코드
2. Sliding Window Minimum

#### 백준 덱 예제
- 초급 - 덱 기본 구조
1. 10866 - baekjoon_10866.py 참고
2. 28279 - baekjoon_28279.py 참고
3. 2346  -

- 중급 - 덱 회전 및 조건 처리
1. 1021 - 
2. 5430 -
3. 3190 -

- 도전 과제 - 응용
1. 11003 -
2. 2812  -
3. 17413 -
4. 1697  -
