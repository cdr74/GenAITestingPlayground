# This python program is used to sort the data in the file and write the sorted data to a new file.
# The data consist of an address book in a csv format with the following fields: name, surname, phone number, email
# The data can be sorted by name or surname in ascending or descending order.
# The main function will check for input errors and call the appropriate function to sort the data.

## COPILOT OUTPUT :

import csv
import operator
import sys


# This function will sort the data by name in ascending order
def sort_name_asc(data):
    data.sort(key=operator.itemgetter(0, 1))
    return data


# This function will sort the data by name in descending order
def sort_name_desc(data):
    data.sort(key=operator.itemgetter(0, 1), reverse=True)
    return data


# INPUT: "Generate unit test" for the above selected method
import unittest


class TestSortNameAsc(unittest.TestCase):
    def test_sort_name_asc(self):
        self.assertEqual(
            sort_name_asc([(3, "b"), (1, "a"), (2, "c")]),
            [(1, "a"), (2, "c"), (3, "b")],
        )
        self.assertEqual(
            sort_name_asc([(3, "b", "z"), (1, "a", "y"), (2, "c", "x")]),
            [(1, "a", "y"), (2, "c", "x"), (3, "b", "z")],
        )
        self.assertEqual(sort_name_asc([]), [])


# This function will sort the data by surname in ascending order
def sort_surname_asc(data):
    data.sort(key=operator.itemgetter(1, 0))
    return data


# This function will sort the data by surname in descending order
def sort_surname_desc(data):
    data.sort(key=operator.itemgetter(1, 0), reverse=True)
    return data


# This function will write the sorted data to a new file
def write_file(data):
    with open("sorted.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    return


# This function will check for input errors and call the appropriate function to sort the data
def main():
    if len(sys.argv) != 3:
        print("Usage: python sort.py <filename> <sort order>")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        sort_order = sys.argv[2]
        if sort_order not in ["name-asc", "name-desc", "surname-asc", "surname-desc"]:
            print("Usage: python sort.py <filename> <sort order>")
            sys.exit(1)
        else:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                data = list(reader)
            if sort_order == "name-asc":
                data = sort_name_asc(data)
            elif sort_order == "name-desc":
                data = sort_name_desc(data)
            elif sort_order == "surname-asc":
                data = sort_surname_asc(data)
            elif sort_order == "surname-desc":
                data = sort_surname_desc(data)
            write_file(data)
            print("Sorted data written to sorted.csv")
    return


if __name__ == "__main__":
    # main()
    unittest.main()
