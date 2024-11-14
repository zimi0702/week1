import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    heap = []
    for char, freq in char_freq.items():
        heapq.heappush(heap, Node(char, freq))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_codes(node, prefix='', codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def encode(input_string, codebook):
    return ''.join(codebook[char] for char in input_string)

def calculate_compression_ratio(original, encoded):
    original_size = len(original) * 8  # Assuming each character is 8 bits
    encoded_size = len(encoded)
    return (original_size - encoded_size) / original_size * 100

# 메인 프로그램
if __name__ == "__main__":
    # 코딩 대상 문자와 빈도수
    characters = ['k', 'o', 'r', 'e', 'a', 't', 'c', 'h']
    frequencies = [10, 5, 2, 15, 18, 4, 7, 11]
    
    char_freq = dict(zip(characters, frequencies))
    
    # 허프만 트리 생성
    huffman_tree = build_huffman_tree(char_freq)
    codebook = build_codes(huffman_tree)
    
    # 사용자 입력 받기
    while True:
        input_string = input("Please a word: ").strip()
        
        # 유효한 문자 체크
        if all(char in char_freq for char in input_string):
            break
        else:
            print("illegal character")
    
    # 인코딩 및 결과 출력
    encoded_result = encode(input_string, codebook)
    compression_ratio = calculate_compression_ratio(input_string, encoded_result)
    
    print(f'결과 비트 열: {encoded_result}')
    print(f'압축률: {compression_ratio:.2f}%')
