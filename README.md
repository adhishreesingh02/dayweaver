# DayWeaver – Daily Routine Optimizer

## About
DayWeaver is a simple Python project that helps in planning daily tasks in a better way. The main idea is to arrange tasks based on energy levels such as High, Medium, and Low so that important work can be done first.

I made this project because I personally find it difficult to manage my daily routine properly. Many times I end up doing random tasks without any proper order. So I thought of creating a small program that can organize tasks in a simple and structured way.

---

## Problem Statement
Students and individuals often struggle with managing their time effectively. Important tasks are sometimes delayed because there is no clear structure or priority in daily planning.

---

## Solution
This project provides a basic solution by taking user inputs and organizing tasks based on priority (energy levels). It then generates a timetable starting from the morning, helping users visualize their day clearly.

---

## How it Works
- The user enters the number of tasks
- Then enters task name and energy level for each task
- Tasks are sorted based on priority:
  - High → first  
  - Medium → next  
  - Low → last  
- A timetable is generated starting from 8:00 AM
- Each task is assigned a duration of 2 hours

---

## Features
- Simple and easy to use  
- Helps in basic time management  
- Automatically sorts tasks  
- Generates a clear timetable  

---

## Technologies Used
- Python  
- datetime module  

---

## Implementation
The project is implemented using basic Python concepts such as lists, loops, and dictionaries. A priority dictionary is used to assign importance to tasks, and sorting is done using a lambda function. The datetime module is used to generate time slots for each task.

---

## Sample Output

Time Task Energy

08:00 AM - 10:00 AM Study High
10:00 AM - 12:00 PM Exercise Medium
12:00 PM - 02:00 PM Relax Low

---

## Applications
- Can be used by students for study planning  
- Useful for daily task management  
- Can be extended into productivity tools  

---

## Limitations
- Fixed duration for all tasks  
- No break scheduling  
- No graphical interface  
- Depends on manual input  

---

## Future Scope
- Add custom task durations  
- Include break times  
- Convert into GUI or web app  
- Add smarter scheduling using AI/ML  

---

## Conclusion
This project is a simple attempt to solve the problem of daily time management. It helped me understand how basic programming logic can be used to organize tasks effectively. Even though it is simple, it can be improved further and developed into a more advanced system.

---

## How to Run
Make sure Python is installed on your system.

Run the following command in terminal:

python dayweaver.py

Then enter the inputs when asked.
