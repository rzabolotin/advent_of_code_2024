from collections import Counter

def main():
    with open("input.txt", "r") as fin:
        data = fin.readlines()

    # Part 1
    # parsing input data
    pairs = [[int(j) for j in x.strip().split()] for x in data]
    list1, list2 = zip(*pairs)

    list1 = sorted(list1)
    list2 = sorted(list2)

    # Distances
    distances = [abs(x-y) for x, y in zip(list1, list2)]
    result = sum(distances)

    print("Total distance: ", result)

    # Part 2
    right_similarity = Counter(list2)
    similarity = sum([x * right_similarity.get(x, 0) for x in list1])
    print("Similarity: ", similarity)




if __name__ == "__main__":
    main()