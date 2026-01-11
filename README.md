# Student Management System

A desktop application built with PyQt6 for managing student records. This application provides a user-friendly graphical interface to add, view, edit, delete, and search student information stored in an SQLite database.

## Features

- **Add Students**: Register new students with name, course, and mobile number
- **View Students**: Display all student records in a table format with ID, Name, Course, and Mobile columns
- **Edit Students**: Update existing student information by clicking on a record
- **Delete Students**: Remove student records from the database with confirmation dialog
- **Search Students**: Find students by name with highlighting in the table
- **Modern GUI**: Clean interface with menu bar, toolbar, and status bar
- **SQLite Database**: Lightweight, file-based database for data persistence

## Requirements

- Python 3.x
- PyQt6 library
- SQLite3 (included with Python by default)

## Installation

1. Clone or download this repository

2. Install PyQt6:

```bash
pip install PyQt6
```

## Database Setup

The application uses an SQLite database file (`database.db`). The database should have a `students` table with the following schema:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    mobile TEXT NOT NULL
)
```

If the database file doesn't exist or the table is missing, you may need to create it. You can initialize it by running a simple Python script:

```python
import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course TEXT NOT NULL,
        mobile TEXT NOT NULL
    )
""")

connection.commit()
connection.close()
```

## Usage

Run the application:

```bash
python main.py
```

### Application Interface

#### Main Window

The main window displays a table with all student records. The table shows:
- **ID**: Unique identifier for each student
- **Name**: Student's full name
- **Course**: Course name (Biology, Math, Astronomy, or Physics)
- **Mobile**: Contact mobile number

#### Menu Bar

- **File Menu**:
  - **Add Student**: Opens a dialog to register a new student

- **Edit Menu**:
  - **Search**: Opens a search dialog to find students by name

- **Help Menu**:
  - **About**: Displays information about the application

#### Toolbar

Quick access buttons for:
- Add Student (with icon)
- Search (with icon)

#### Status Bar

When you click on a table row, the status bar displays:
- **Edit Record**: Button to modify the selected student's information
- **Delete Record**: Button to remove the selected student from the database

### Adding a Student

1. Click "Add Student" from the File menu or toolbar
2. Fill in the form:
   - **Name**: Enter the student's name
   - **Course**: Select from dropdown (Biology, Math, Astronomy, Physics)
   - **Mobile**: Enter the mobile number
3. Click "Register" to save

### Editing a Student

1. Click on any row in the student table
2. Click "Edit Record" in the status bar
3. Modify the information in the dialog
4. Click "Update" to save changes

### Deleting a Student

1. Click on the student record you want to delete
2. Click "Delete Record" in the status bar
3. Confirm deletion in the dialog
4. The record will be removed and a success message will be displayed

### Searching for a Student

1. Click "Search" from the Edit menu or toolbar
2. Enter the student's name
3. Click "Search"
4. Matching records will be highlighted in the table

## File Structure

```
Student_Management_System/
├── main.py                    # Main application file with GUI and database operations
├── example.py                 # Example PyQt6 application (Age Calculator)
├── database.db                # SQLite database file (created automatically)
├── icons/                     # Application icons
│   └── icons/
│       ├── add.png            # Add icon for toolbar/menu
│       └── search.png         # Search icon for toolbar/menu
└── README.md                  # This file
```

## How It Works

### DatabaseConnection Class

Provides a simple interface to connect to the SQLite database:

```python
connection = DatabaseConnection().connect()
```

### MainWindow Class

The main application window that includes:
- Table widget for displaying student data
- Menu bar with File, Edit, and Help menus
- Toolbar with quick action buttons
- Status bar for contextual actions (Edit/Delete buttons)

### Dialog Classes

- **InsertDialog**: Form for adding new students
- **EditDialog**: Form for updating existing student records
- **DeleteDialog**: Confirmation dialog for deleting records
- **SearchDialog**: Input dialog for searching students by name
- **AboutDialog**: Information dialog about the application

### Data Operations

- **Load Data**: Retrieves all students from the database and populates the table
- **Insert**: Adds a new student record to the database
- **Update**: Modifies an existing student record
- **Delete**: Removes a student record from the database
- **Search**: Queries the database and highlights matching records in the table

## Available Courses

The application supports the following courses:
- Biology
- Math
- Astronomy
- Physics

To add more courses, modify the `courses` list in the `InsertDialog` and `EditDialog` classes.

## Customization

### Adding More Courses

Edit the `courses` list in both `InsertDialog` and `EditDialog` classes:

```python
courses = ["Biology", "Math", "Astronomy", "Physics", "Chemistry", "Computer Science"]
```

### Changing Database File

Modify the `DatabaseConnection` class initialization:

```python
def __init__(self, database_file="your_database.db"):
    self.database_file = database_file
```

### Modifying Table Columns

To add or remove columns:
1. Update the database schema (add/remove columns)
2. Modify `setColumnCount()` and `setHorizontalHeaderLabels()` in `MainWindow`
3. Update all SQL queries to include new columns
4. Modify dialog classes to include new fields

## Troubleshooting

- **Import Error for PyQt6**: Make sure PyQt6 is installed: `pip install PyQt6`
- **Database Errors**: Ensure `database.db` exists and has the correct schema
- **Icons Not Showing**: Verify that the `icons/icons/` directory contains `add.png` and `search.png`
- **Application Crashes on Startup**: Check that the database file is accessible and not corrupted
- **Search Not Working**: Ensure student names match exactly (case-sensitive search)

## Notes

- The search function is case-sensitive and requires exact name matches
- The database file (`database.db`) is created in the same directory as the script
- Icons are expected in the `icons/icons/` directory relative to the script location
- The application uses SQLite, so no separate database server is required

## License

This project is open source and available for personal and educational use.
