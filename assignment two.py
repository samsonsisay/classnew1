# houses = ["A", "E", "C", "G", "F", "B", "D"]


# def second_corner():
#     end = len(houses) - 1
#     return houses[end]
#
#
# def neighbor_a():
#     second = 1
#     return houses[second]
#
#
# def middle():
#     half = len(houses) // 2
#     return houses[half]
#
#
# def b_and_g():
#     b = houses.find("B")  # 5
#     g = houses.find("G")
#     if b < g:
#         mid = b + 1
#     else:
#         mid = g + 1
#     return houses[mid]
#
#
# def b_and_e():
#     b = houses.find("B")  # 5
#     e = houses.find("E")  # 1
#     if b < e:
#         mid = e - b - 1
#     else:
#         mid = b - e - 1
#     return mid


for _ in range(3):
    answer = input("who lives in the second corner?\nA)E  B)C  C)A  D)F  E)G  F)B  G)D\t ")
    if answer == "G" or answer == "g":
        print("CORRECT")
        break
    else:
        print("WRONG")
else:
    print("Good Bye")
    exit()

for _ in range(3):
    answer = input("Who lives in the middle?\nA)E  B)C  C)A  D)F  E)G  F)B  G)D\t ")
    if answer == "E" or answer == "e":
        print("CORRECT")
        break
    else:
        print("WRONG")
else:
    print("Good Bye")
    exit()

for _ in range(3):
    answer = input("Who lives between B and G?\nA)E  B)C  C)A  D)F  E)G  F)B  G)D\t ")
    if answer == "D" or answer == "d":
        print("CORRECT")
        break
    else:
        print("WRONG")
else:
    print("Good Bye")
    exit()

for _ in range(3):
    answer = input("Who is the neighbor of A?\nA)E  B)C  C)A  D)F  E)G  F)B  G)D\t ")
    if answer == "A" or answer == "a":
        print("CORRECT")
        break
    else:
        print("WRONG")
else:
    print("Good Bye")
    exit()


for _ in range(3):
    answer = input("How many houses are there between B and E?\nA)2  B)1  C)3  D)4\t ")
    if answer == "C" or answer == "c":
        print("CORRECT")
        break
    else:
        print("WRONG")
else:
    print("Good Bye")
    exit()

