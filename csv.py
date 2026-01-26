from collections import defaultdict

def read_csv_data(filename):
    data = []
    merged = defaultdict(list)
    with open(filename , "r", encoding="utf-8") as file :
        headers = file.readline().strip ().split (",")
        for line in file:
            values = line.strip().split (",")
            row = dict(zip(headers, values))
            data.append(row)
    for row in data :
        for k, v in row.items():
            merged[k].append(int(v))
    return dict(merged)
if __name__ == '__main__':
    csv_dict = read_csv_data ("datoteka.csv")
    print(csv_dict)