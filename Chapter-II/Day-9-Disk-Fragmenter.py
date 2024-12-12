input_file = "Inputs/Chapter-II/Day-9-Test-Input.txt"

with open(input_file) as file:
    data = [int(x) for x in file.read().rstrip()]

def files_spaces():
    files = {0: data[0]}
    spaces = {1: (files[0], files[0] + data[1])}
    
    for i in range(2, len(data), 2):
        files[i] = data[i]
        prev = spaces[i-1][1] + files[i]
        if i+1 < len(data):
            spaces[i+1] = (prev, prev + data[i+1])
    return files, spaces

def disk_fragmenter(size_limitation=False):
    files, spaces = files_spaces()
    
    def fill_gap(f_id, x, y, result):
        while x < y and files[f_id]  > 0:
            result += f_id // 2 * x
            files[f_id] -= 1
            x += 1

        if files[f_id]  == 0:
            del files[f_id]

        return x, y, result
    
    def fill_gap_size_limitation(f_id, x, y, result):
        if files[f_id] <= y - x:
            for i in range(x, files[f_id] + x):
                result += f_id // 2 * i
            del files[f_id]
            x += files[f_id] 
        return x, y, result

    result, end = 0, 0
    for id, (x, y) in list(spaces.items()):
        if id-1 in files:
            for i in range(end, end + files[id-1]): 
                result += (id-1) // 2 * i
            del files[id-1]

        for f_id in reversed(list(files.keys())):
            if not size_limitation:
                x, y, result = fill_gap(f_id, x, y, result)
            else:
                x, y, result = fill_gap_size_limitation(f_id, x, y, result)
            if x >= y: break
        end = y
        del spaces[id]
    return result


def part1():
    return disk_fragmenter()

def part2():
    return disk_fragmenter(size_limitation=True)
