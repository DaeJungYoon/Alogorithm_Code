import sys
input = sys.stdin.readline

member_info = set()

for _ in range(int(input())):
    name, status =input().split()

    if status == "enter":
        member_info.add(name)

    elif status == "leave":
        member_info.discard(name)

working_member = sorted(member_info, reverse=True)

for member in working_member:
    print(member)