import csv
import os
class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
    def __iter__(self):
        self.file = open(file=self.file_path)
        return self
    def __next__(self):
        line  = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

# def TxtToCsv(text):
    import httpx
    import csv
    import os

    # url = 'https://jsonplaceholder.typicode.com/users'
    # response = httpx.get(url=url)
    # data = response.json()
    # # print(data)
    # # os.mkdir('users')
    # os.chdir('users')


if __name__ == '__main__':
    with open("Price.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(('name', 'price', 'desctiption'))
        f.close()
    for file in os.listdir("descriptions"):
        ls = list()
        for line in FileReader(f"descriptions/{file}"):
            ls.append(line)
        with open("Price.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow((f"{ls[0]}",f"{ls[1]}",f"{ls[2]}"))
            f.close()
