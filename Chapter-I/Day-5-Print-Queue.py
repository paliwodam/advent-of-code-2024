from collections import defaultdict
input_file = "Chapter-I/Inputs/Day-5-Test-Input.txt"

# with open(input_file) as file:
#     data = file.read()
#     rules, updates = data.split("\n\n")
#     rules, updates = rules.split(), updates.split()

#     before = defaultdict(list)
#     after = defaultdict(list)

#     for rule in rules:
#         x, y = rule.split("|")
#         before[y].append(x)
#         after[x].append(y)

#     result = 0
#     for update in updates:
#         update = update.split(",")
#         pages = set(update)

#         valid = True
#         printed = []
#         for page in update:
#             for before_page in before[page]:
#                 if before_page in pages and not before_page in printed:
#                     valid = False
#                     break
#             printed.append(page)
#         if valid: 
#             result += int(update[len(update) // 2])
#     print(result)


    
with open(input_file) as file:
    data = file.read()
    rules, updates = data.split("\n\n")
    rules, updates = rules.split(), updates.split()

    before = defaultdict(list)

    for rule in rules:
        x, y = rule.split("|")
        before[y].append(x)

    result = 0
    for update in updates:
        update = update.split(",")
        update_pages = set(update)

        stack = []
        for page in update:
            print(page, ": [", end="")
            for before_page in before[page]:
                if before_page in update_pages:
                    print(before_page, end= ", ")
            print("]")

    #     valid = True
    #     printed = []
    #     for page in update:
    #         for before_page in before[page]:
    #             if before_page in pages and not before_page in printed:
    #                 valid = False
    #                 break
    #         printed.append(page)
    #     if valid: 
    #         result += int(update[len(update) // 2])
    # print(result)