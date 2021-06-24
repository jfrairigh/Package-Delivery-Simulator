# Name: Jessica Rairigh, Student ID: 001198235
import re
import time
from Resources.ImportData import ImportData
from Model.Truck import Truck
from Model.Time import Time

initialized_info = ImportData()  # import data and organize into data structures

packages_remaining = initialized_info.get_package_table().all_keys()

def _is_space_on_truck(packages):
    truck_load_limit = 16
    answer = len(packages) < truck_load_limit
    return answer

# Time Complexity: O(n)
# Space Complexity: O(n)
def get_ready_packages(start_time):
    ready_packages = []
    regex = re.compile('^(?:[01]?\d|2[0-3])(?::[0-5]\d){1,2}$')  # pattern will help find time in package.notes
    for key in packages_remaining:  # check to see if delayed package can be sent yet
        package = initialized_info.get_package_table().look_up(key)
        if 'Delayed' not in package.notes:  # if package is not delayed add it to the list
            ready_packages.append(key)
        else:
            for word in package.notes.split():  # otherwise check to see if start time is greater than time of delay
                if regex.match(word):
                    t = time.strptime(word, '%H:%M')
                    delayed_until = Time(t.tm_hour, t.tm_min)
                    if str(delayed_until) < str(start_time):
                        ready_packages.append(key)
    return ready_packages


# Time Complexity: O(n)
# Space Complexity: O(n)
def get_urgent_packages(delayed_packages_filtered):
    packages = []
    for key in delayed_packages_filtered:  # check for urgent packages
        package = initialized_info.get_package_table().look_up(key)
        if 'EOD' not in package.deadline and _is_space_on_truck(packages):
            packages.append(key)
    return packages


# Time Complexity: O(1)
# Space Complexity: O(1)
def get_delivered_together_packages(packages):
    for key in packages:  # check for packages that must be delivered together , and add to list if necessary
        package = initialized_info.get_package_table().look_up(key)
        if 'Must be delivered' in package.notes:  # if another package is required put key in package_needed
            note = package.notes
            for word in note.split():
                if word.isdigit() and _is_space_on_truck(packages) and int(word) not in packages:
                    packages.append(int(word))

    return packages


# Time Complexity: O(n)
# Space Complexity: O(n)
def get_matching_address_packages(packages, ready_packages):
    for key in packages:  # check for matching addresses
        if not _is_space_on_truck(packages):
            break
        package = initialized_info.get_package_table().look_up(key)
        for k in ready_packages:
            p = initialized_info.get_package_table().look_up(k)
            if package.address == p.address and _is_space_on_truck(packages) and p.id not in packages:
                packages.append(k)

    return packages


# Time Complexity: O(1)
# Space Complexity: O(n)
def get_top_off_load(packages, ready_packages):
    for key in ready_packages:  # finish filling with remaining packages
        if not _is_space_on_truck(packages):
            break
        elif key not in packages:
            packages.append(key)
    return packages


# Time Complexity: O(n)
# Space Complexity: O(n)
def truck_factory(start_time, end_time, truck_number, return_to_hub=False): # O(n)
    ready_packages = get_ready_packages(start_time)  # get a list of all ready packages
    packages = get_urgent_packages(ready_packages)  # add urgent packages to load
    packages = get_delivered_together_packages(packages)  # add any required package
    packages = get_matching_address_packages(packages, ready_packages)
    packages = get_top_off_load(packages, ready_packages)

    return Truck(packages, initialized_info, start_time, end_time, truck_number, return_to_hub)  # create and return Truck object


# Time Complexity: O(n)
# Space Complexity: O(n)
def determine_remaining_packages(truck_packages, previous_remaining_packages):
    remaining_packages = []
    for key in previous_remaining_packages:
        if key not in truck_packages:
            remaining_packages.append(key)

    return remaining_packages


# User Interface:

print('Enter the time that you would like to be updated on delivery statuses (hour:minute): ')
time_string = input().split(':', 2)
snapshot_time = Time(int(time_string[0]), int(time_string[1]))
print('Would you also like to know the total distance traveled by all trucks up to that time? (Yes or No): ')
should_report_miles = True
if input() == 'No':
    should_report_miles = False

# Start Delivery Simulation:

truck1_number = 1
truck2_number = 2

start_time_truck1 = Time(8, 0, 1)  # truck 1 load 1 start time
start_time_truck2_1 = Time(9, 5, 1)  # truck 2 load 1 start time
start_time_truck2_2 = Time(11, 45, 0)  # truck 2 load 2 start time

start_truck_info = [(start_time_truck1, truck1_number, False), (start_time_truck2_1, truck2_number, True),
                    (start_time_truck2_2, truck2_number, False)]

total_distance = 0
for i, truck in enumerate(start_truck_info):
    if str(truck[0]) < str(snapshot_time):  # load and send trucks depending time requested by user
        truck_load = truck_factory(truck[0], snapshot_time, truck[1], truck[2])
        packages_remaining = determine_remaining_packages(truck_load.packages, packages_remaining)  # after each truck load the list is updated to reflect only the remaining packages
        truck_load.load_start_truck()  # truck is started and packages will be delivered until the snapshot_time
        total_distance += truck_load.distance_traveled

initialized_info.get_package_table().print_all()  # print hashtable at requested time for update

if should_report_miles:  # report miles if requested
    print('total distance: ', total_distance)
