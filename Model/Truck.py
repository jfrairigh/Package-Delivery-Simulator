import math


# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Truck:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self, packages, initialized_info, start_time, snapshot_time, truck_number, has_return_to_hub=False):
        self._HUB = 'HUB'
        self._packages = packages
        self._current_location = self._HUB
        self._distance_traveled = 0.0
        self._initialized_info = initialized_info
        self._mph = 18.0
        self._current_time = start_time
        self._snapshot_time = snapshot_time
        self._truck_number = truck_number
        self._has_return_to_hub = has_return_to_hub

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def load_start_truck(self):  # Nearest Neighbor Algorithm sorts list based on next closest location
        current_location = 'HUB'
        for sort_partition in range(len(self._packages)):  # sort_partition represents the first unsorted package.id in the list
            i = 0  # i keeps track of the number of positions away from the sort_partition
            temp_min_miles = math.inf  # initializes and resets min distance
            nominated_package = self._initialized_info.get_package_table().look_up(self._packages[sort_partition])
            nominated_index = -1
            while (i + sort_partition) < len(self._packages):  # iterates from sort_partition to the end of the list
                package = self._initialized_info.get_package_table().look_up(self._packages[i + sort_partition])
                distance = self._initialized_info.get_distance(current_location, package.address)
                if distance < temp_min_miles:  # check to see if the new distance is less than the current minimum distance (in miles)
                    temp_min_miles = distance
                    nominated_package = package
                    nominated_index = i + sort_partition
                i += 1

            status = 'on truck ' + str(self._truck_number) + ' at ' + str(self._current_time)
            sort_partition_package = self._initialized_info.get_package_table().look_up(self._packages[sort_partition])
            if sort_partition_package.deadline != 'EOD' and nominated_package.deadline == 'EOD':  # ensure urgent package gets delivered before non-urgent packages
                self._packages[sort_partition] = sort_partition_package  # replace key at sort_partition with corresponding package object
                current_location = sort_partition_package.address  # current_location is changed to reflect chosen packages address
                sort_partition_package.set_delivery_status(status) #  update status of chosen package
            else:
                self._packages[nominated_index] = self._packages[sort_partition]  # swap step 1 of 2
                self._packages[sort_partition] = nominated_package  # swap step 2 of 2.  When package is chosen the package object itself is stored in the list rather than its key.
                current_location = nominated_package.address  # new location has been chosen so current_location is updated
                self._packages[sort_partition].set_delivery_status(status) # delivery status is updated
        self._deliver_packages()

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def _deliver_packages(self):
        for package in self._packages:
            status = 'en route at ' + str(self._current_time)
            package.set_delivery_status(status)
            distance = self._log_miles(package.address)
            self._track_time(distance)

            if str(self._current_time) <= str(self._snapshot_time):  # check current time vs. snapshot time
                status = 'delivered by truck ' + str(self._truck_number) + ' at ' + str(self._current_time)
                package.set_delivery_status(status)
                self._current_location = package.address  # update current location
            else:
                break  # if package will not be delivered before snapshot time then stop delivering packages

        if self._has_return_to_hub:  # return truck to hub if it needs to get another load of packages
            distance = self._log_miles(self._HUB)
            self._track_time(distance)

    def _log_miles(self, address):
        distance = self._initialized_info.get_distance(self._current_location, address)
        self._distance_traveled += distance
        return distance

    def _track_time(self, distance):
        time_passed = distance / self._mph  # converts miles traveled into time passed
        hours_passed = int(time_passed)
        minutes_passed = int(time_passed * 60) % 60
        second_passed = int((time_passed * 60) * 60) % 60
        self._current_time.increase_hour(hours_passed)
        self._current_time.increase_minute(minutes_passed)
        self._current_time.increase_second(second_passed)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    @property
    def distance_traveled(self):
        return self._distance_traveled

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    @property
    def packages(self):
        return self._packages
