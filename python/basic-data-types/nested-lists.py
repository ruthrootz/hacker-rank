if __name__ == '__main__':

    records = []
    second_lowest_score = 1000
    lowest_score = 999
    result_names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowest_score:
            second_lowest_score = lowest_score
            lowest_score = score
        if score < second_lowest_score and score > lowest_score:
            second_lowest_score = score
        records.append([name, score])

    for record in records:
        if record[1] == second_lowest_score:
            result_names.append(record[0])

    result_names.sort()
    for name in result_names:
        print(name)
