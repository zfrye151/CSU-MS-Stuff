#Zachary Frye
#CSC 500
#3/1/2026
#Assignment 6

courses = {"CSC101": {"room": "3004", "instructor": "Haynes", "time": "8:00 AM"}, #create nested dictionaries for all data
           "CSC102": {"room": "4501", "instructor": "Alvarado", "time": "9:00 AM"},
           "CSC103": {"room": "6755", "instructor": "Rich", "time": "10:00 AM"},
           "NET110": {"room": "1244", "instructor": "Burke", "time": "11:00 AM"},
           "COM241": {"room": "1411", "instructor": "Lee", "time": "1:00 PM"}}

course_number = input("Enter a course number: ") #prompt user for course number
if course_number in courses: #check if course number is valid
    details = courses[course_number] #retrieve course details from dictionary
    print("Course: " + course_number) #print course number and details
    print("Room: " + details["room"]) #print room number, instructor, and time
    print("Instructor: " + details["instructor"])
    print("Time: " + details["time"])
else:
    print("Course not found.") #print error message if course number is invalid