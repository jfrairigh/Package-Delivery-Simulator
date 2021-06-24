import csv
from Resources.Hashtable import Hashtable
from Model.Package import Package

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
class ImportData:
    def __init__(self):
        self._distance_table = {}
        self._package_table = Hashtable()
        self._initialize_packages()
        self._initialize_distances()

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def _initialize_packages(self):  # Read package information from file
        with open('Resources/WGUPSPackageFile.csv') as package_csvfile:
            read_csv = csv.reader(package_csvfile, delimiter=',')
            for row in read_csv:
                package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 'at the hub')
                self._package_table.insert(package.id, package)

    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def _initialize_distances(self):  # Read distance information from file and store it in a nested dictionary
        with open('Resources/WGUPSDistanceTable.csv') as distance_csvfile:
            read_distance_csv = csv.reader(distance_csvfile, delimiter=',')
            row1 = next(read_distance_csv)
            for i, current_location in enumerate(row1):  # Outer loop traverses column headers and creates inner dict
                temp_inner_dict = {}
                for row in read_distance_csv:  # Inner loop fill inner dict {destination: miles}
                    temp_destination = row[0]
                    temp_distance = float(row[i+1])
                    temp_inner_dict[temp_destination] = temp_distance
                self._distance_table[current_location] = temp_inner_dict
                distance_csvfile.seek(0)
                next(read_distance_csv)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_distance(self, current_location, destination):
        if current_location == destination:  # if the two locations are the same then look up isn't required
            return 0
        table_column = self._distance_table[current_location]
        return table_column[destination]

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_package_table(self):
        return self._package_table
