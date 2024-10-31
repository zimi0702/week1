import re
import os
from collections import Counter

class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e

    def replace(self, pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e

    def __str__(self):
        return str(self.array[0:self.size])

    def make_dictionary(self):
        all_text = ' '.join(self.getEntry(i) for i in range(self.size))
        words = re.findall(r'\b\w+\b', all_text)
        word_count = Counter(words)

        print("입력된 내용 :", all_text)
        for word, count in word_count.items():
            print(f"{word} : {count}")

        # 현재 파일이 저장될 경로 설정
        output_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dic.txt')
        with open(output_file_path, 'w') as file:
            for word, count in word_count.items():
                file.write(f"{word} : {count}\n")

# 메인 코드
list = ArrayList(1000)
while True:
    print("현재 작업 디렉토리:", os.getcwd())  # 현재 작업 디렉토리 출력
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료, m-사전생성 => ")

    if command == 'i':
        pos = int(input("  입력행 번호: ")) - 1
        str = input("  입력행 내용: ")
        list.insert(pos, str)

    elif command == 'd':
        pos = int(input("  삭제행 번호: ")) - 1
        list.delete(pos)

    elif command == 'r':
        pos = int(input("  변경행 번호: ")) - 1
        str = input("  변경행 내용: ")
        list.replace(pos, str)

    elif command == 'p':
        print('Line Editor')
        for line in range(list.size):
            print('[%2d] ' % line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q':
        exit()

    elif command == 'l':
        filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.txt')
        with open(filename, "r") as infile:
            lines = infile.readlines()
            for line in lines:
                list.insert(list.size, line.rstrip('\n'))

    elif command == 's':
        filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.txt')
        with open(filename, "w") as outfile:
            for i in range(list.size):
                outfile.write(list.getEntry(i) + '\n')

    elif command == 'm':
        list.make_dictionary()

    else:
        print("잘못된 명령어입니다.")
