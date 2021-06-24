# Package-Delivery-Simulator
### Reason for creating:
I created this application for Data Structures and Algorithms II at Western Governors University (WGU).

### Requirements and Purpose of Project:
The application is a Python console program, which simulates the delivery of forty packages using two drivers and their respective trucks. 
It decides which packages should be loaded onto what truck, updates the status of each package, and creates a route, which allows packages to be delivered in less
than 140 miles. It also adheres to the constraints of each package, which are written in the notes field of "Resources/WGUPSPackageFile.csv". 

### How to run the application:
* Ensure you have Python 3.6 or higher
* Download the provided files. You may exclude the Documents folder.
* Open your Command Line (Terminal) and Navigate to the WGU UPS folder.
* Type "python main.py"

#### The application will ask you for user input before starting the simulation.

Input Needed: 

1. "Enter the time that you would like to be updated on delivery statuses (hour:minute):"
* The time you enter should be in military time. (ex: 14:00)
* The time you enter is part of the simulation and does not represent actual time. The first truck will start at 8:00 and the simulation will stop at the indicated time.

2. "Would you also like to know the total distance traveled by all trucks up to that time? (Yes or No):"
 * Acceptable answers include: Yes, No, y, n, Y, or N
 
 ### Document Folder:
 
 The Document folder includes the instructions given by WGU, and a document describing how the application fulfills the requirements.
