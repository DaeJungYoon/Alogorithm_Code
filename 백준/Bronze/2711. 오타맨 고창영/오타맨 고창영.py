T = int(input())  # 첫 번째 줄에서 테스트 케이스의 개수 입력받기
for _ in range(T):  # T번 반복
    idx, word = input().split()  # 각 테스트 케이스에서 오타 위치와 단어 입력받기
    idx = int(idx)  # 오타 위치를 정수로 변환
    new_word = word[:idx-1] + word[idx:] # 인덱스 위치의 문자 제거
    print(new_word)