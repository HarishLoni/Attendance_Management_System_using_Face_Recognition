# Attendance Management System Using Face Recognition
A Python project that captures and saves student attendance using facial recognition. It connects to a MySQL database to store attendance data and can export the data to CSV files for easy access and management. The application includes functionalities for manual entry, data validation, and user notifications, with a graphical user interface built using Tkinter.

# Features
Image Capture: Captures images of students for attendance.
Model Training: Trains a face recognition model using the captured images.
Automatic Attendance: Marks attendance by recognizing faces in real-time.
Attendance Records: Saves attendance data in a database and exports it to a CSV file.

# How to Run This Project
Clone the Repository:
git clone https://github.com/HarishLoni/Attendance_Management_System_using_Face_Recognition.git
cd Attendance_Management_System_using_Face_Recognition

Install Required Dependencies: Ensure you have Python installed. Then, run:
pip install -r requirements.txt

Set Up the Database:
Install MySQL and create a database.
Update database credentials in the project files (host, user, password, db). Ensure the database tables include the headers: ENROLLMENT, NAME, DATE, TIME.

Run the Application:
python main_Run.py

Using the Application:
Capture images of individuals.
Train the model with the captured data.
Use the "Automatic Attendance" feature to mark and save attendance.

Attendance Records: Check the attendance records in the StudentDetails folder as CSV files or access them directly from the database.

