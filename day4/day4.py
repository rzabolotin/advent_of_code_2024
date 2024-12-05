
def find_sentences(source, target):
    count = 0
    offset = 0
    while source.find(target, offset) != -1:
        count += 1
        offset = source.find(target, offset) + 1
    return count

def find_sentences_centers(source, target):
    centers = []
    offset = 0
    while source.find(target, offset) != -1:
        offset = source.find(target, offset) + 1
        centers.append(offset)
    return centers


def convert_diagonal_point(offset, x_start, y_start, x_direction, y_direction):
    return x_start + offset * x_direction, y_start + offset * y_direction


def get_diagonal_row(data, x_start, y_start, x_direction = -1, y_direction = 1):
    result = []
    x = x_start
    y = y_start
    while ((x_direction == -1 and x >= 0) or (x_direction == 1 and x < len(data)))\
            and (y_direction == 1 and y < len(data[0]) or (y_direction == -1 and y >= 0)):
        result += [data[x][y]]
        x += x_direction
        y += y_direction

    return "".join(result)


def get_diagonal_data(data, x_start, x_direction, with_starts = False):
    result = []
    y_start = 0
    y_direction = 1
    while (x_direction == 1 and x_start < len(data)) or (x_direction == -1 and x_start >= 0):
        if with_starts:
            result.append({
                'start': (x_start, y_start, -x_direction, y_direction),
                'row': get_diagonal_row(data, x_start, y_start, -x_direction, y_direction)
            })
        else:
            result.append(get_diagonal_row(data, x_start, y_start, -x_direction, y_direction))
        x_start += x_direction
    x_start -= x_direction
    y_start += y_direction
    while y_start < len(data[0]):
        if with_starts:
            result.append({
                'start': (x_start, y_start, -x_direction, y_direction),
                'row': get_diagonal_row(data, x_start, y_start, -x_direction, y_direction)
            })
        else:
            result.append(get_diagonal_row(data, x_start, y_start, -x_direction, y_direction))
        y_start += y_direction

    return result


def main():
    with open("input.txt", "r") as fin:
        data = fin.readlines()
        data = [x.strip() for x in data]

    # Part 1
    count = 0
    # count rows
    for row in data:
        count += find_sentences(row, "XMAS")
        #print(f"Row: {row} - {count}")
    for row in data:
        count += find_sentences(row, "SAMX")
        #print(f"RowR: {row} - {count}")

    transposed_data = list(map(lambda *args: "".join(list(*args)), zip(*data)))
    for column in transposed_data:
        count += find_sentences(column, "XMAS")
        #print(f"Column: {column} - {count}")
    for column in transposed_data:
        count +=find_sentences(column, "SAMX")
        #print(f"ColumnR: {column} - {count}")

    print(f"Count in rows+columns: {count}")

    diagonal_data = get_diagonal_data(data, 0, 1)
    for diagonal in diagonal_data:
        count += find_sentences(diagonal, "XMAS")
        #print(f"Diagonal: {diagonal} - {count}")
    for diagonal in diagonal_data:
        count += find_sentences(diagonal, "SAMX")
        #print(f"DiagonalR: {diagonal} - {count}")

    print(f"Count in rows+columns+right-diagonals: {count}")

    diagonal_data = get_diagonal_data(data, len(data) - 1, -1)
    for diagonal in diagonal_data:
        count += find_sentences(diagonal, "XMAS")
        #print(f"Diagonal: {diagonal} - {count}")
    for diagonal in diagonal_data:
        count += find_sentences(diagonal, "SAMX")
        #print(f"DiagonalR: {diagonal} - {count}")

    print(f"Count in rows+columns+both-diagonals: {count}")

    # Part 2

    diagonal_data = get_diagonal_data(data, 0, 1, with_starts = True)
    centers_1 = set()
    for diagonal in diagonal_data:
        for point in find_sentences_centers(diagonal['row'], "MAS"):
            centers_1.add(convert_diagonal_point(point, diagonal['start'][0], diagonal['start'][1], diagonal['start'][2], diagonal['start'][3]))
        for point in find_sentences_centers(diagonal['row'], "SAM"):
            centers_1.add(convert_diagonal_point(point, diagonal['start'][0], diagonal['start'][1], diagonal['start'][2], diagonal['start'][3]))

    diagonal_data = get_diagonal_data(data, len(data) - 1, -1, with_starts = True)
    centers_2 = set()
    for diagonal in diagonal_data:
        for point in find_sentences_centers(diagonal['row'], "MAS"):
            centers_2.add(convert_diagonal_point(point, diagonal['start'][0], diagonal['start'][1], diagonal['start'][2], diagonal['start'][3]))
        for point in find_sentences_centers(diagonal['row'], "SAM"):
            centers_2.add(convert_diagonal_point(point, diagonal['start'][0], diagonal['start'][1], diagonal['start'][2], diagonal['start'][3]))


    print(f"Count of X-MAX: {len(centers_1.intersection(centers_2))}")






if __name__ == "__main__":
    main()