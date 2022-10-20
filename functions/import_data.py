import csv


def import_data():
    with open(r'C:\Users\melis\tests-play\data\AUNZ_cities_test.csv', newline='') as f:
        imported_data = list(csv.reader(f))
        return imported_data


if __name__ == '__main__':
    data = import_data()


