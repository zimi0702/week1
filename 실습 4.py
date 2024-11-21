class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            print("큐가 가득 찼습니다.")

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            removed_item = self.array[self.front]
            self.array[self.front] = None  # 삭제된 요소를 None으로 설정
            return removed_item
        else:
            print("큐가 비어 있습니다.")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front + 1:self.rear + 1])
        else:
            return str(self.array[self.front + 1:self.capacity] +
                       self.array[0:self.rear + 1])


# 테스트 프로그램
if __name__ == "__main__":
    q = CircularQueue(10)
    
    while True:
        command = input("명령어를 입력하세요 (e: enqueue, d: dequeue, q: 종료): ").strip().lower()
        
        if command == 'e':
            item = input("큐에 추가할 요소를 입력하세요: ")
            q.enqueue(item)
            print(f'큐 내용: {q}')
        
        elif command == 'd':
            removed_item = q.dequeue()
            if removed_item is not None:
                print(f'삭제된 요소: {removed_item}')
            print(f'큐 내용: {q}')
        
        elif command == 'q':
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("유효하지 않은 명령어입니다. e, d, q 중에서 선택하세요.")
