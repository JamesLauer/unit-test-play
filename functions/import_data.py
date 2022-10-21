import csv
import pathlib

path = pathlib.Path().parent.absolute()


def import_data():
    with open(f'{path}/data/AUNZ_cities_test.csv', newline='') as f:
        imported_data = list(csv.reader(f))
        return imported_data


if __name__ == '__main__':
    data = import_data()


