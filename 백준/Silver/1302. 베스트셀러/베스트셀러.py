N = int(input())
# 구조화
# 빈 딕셔너리 제작
sales_info = {}
# 반복문을 돌며
for _ in range(N):
    # 책 제목을 입력받고
    book_name = input()

# 1. 조건문을 통한 분기
    # 만약 딕셔너리에 해당 제목이 없다면? => 생성
    if book_name not in sales_info:
        sales_info[book_name] = 1
    # 있다면? => 1 더해주기
    else:
        sales_info[book_name] = sales_info[book_name] + 1

# 딕셔너리 정렬
sorted_sales_info = sorted(sales_info.items(), key=lambda x: (-x[1], x[0]))
print(sorted_sales_info[0][0])