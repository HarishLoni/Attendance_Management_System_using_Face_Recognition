# Attendance Management System Using Face Recognition


A Python project that captures and saves student attendance using facial recognition. It connects to a MySQL database to store attendance data and can export the data to CSV files for easy access and management. The application includes functionalities for manual entry, data validation, and user notifications, with a graphical user interface built using Tkinter.





## Features

- Image Capture: Captures images of students for attendance.
- Model Training: Trains a face recognition model using the captured images.
- Automatic Attendance: Marks attendance by recognizing faces in real-time.
- Attendance Records: Saves attendance data in a database and exports it to a CSV file.


## Installation
Prerequisites :
Make sure you have the following installed: Python 3.x pip (Python's package installer) Virtual Environment (optional but recommended)


1]Clone the Repository:
```bash
git clone https://github.com/HarishLoni/Attendance_Management_System_using_Face_Recognition.git  
cd Attendance_Management_System_using_Face_Recognition
```
2]Install Required Dependencies:
```bash
pip install -r requirements.txt
```
3]Set Up the Database:
- Install MySQL and create a database.
- Update the database credentials in the project files (host, user, password, db).
4]Run the Application:
```bash
python main_Run.py
```
5]Using the Application:
Capture images of individuals.
Train the model with the captured data.
Use the "Automatic Attendance" feature to mark and save attendance






## Using the Application

- Capture images of individuals.
- Train the model with the captured data.
- Use the "Automatic Attendance" feature to mark and save attendance.
- Check the attendance records in the StudentDetails folder as CSV files.
- Alternatively, access the records directly from the database.
