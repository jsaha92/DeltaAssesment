Please Read DeltaSubmissionDocumentation.docx for detailed insight as to how the code was created.

Please refer to DeltaAssessment.ipynotebook to refer to my testing process via Google Colab, as was mentioned in the .docx file

The assumed technologies for the customer using the scripts are having a UNIX terminal, Python, and SQL Database functionality

Code Files contained:

1. Task1.sql (SQL script to get latest flightkey information)
2. Task2.py (python function to get latest flightkey information)

For the SQL code provided in the task1.sql file, there are few changes that need to be made to have it work properly:

1. Navigate to line 15 (From Clause)
2. Change table being used into your own postgres table and schema combination (e.g. schemaname.tablename)
3. Run query and await results

For the Python function to be called few steps need to be done as well

1. Open a terminal
2. Navigate to the directory where Task2.py is located
3. Start a Python terminal
4. Import the function
4a. ex: from Task2 import get_latest_flight_status
5. Define the file path for the Excel file
5a. ex: file_path = "/content/..../*.xlsx"
6. Call the function with the file_path parameter and store as a variable
6a. ex: latest_status = get_latest_flight_status(file_path)
7. Use/print result as desired
7a. ex: print(latest_status)

User Tips to remember:

1. You can change file_path to point to any Excel file they want.
2. No need to modify Task2.py; just import the function and call it.
3. The script is now reusable and doesn’t execute anything automatically.