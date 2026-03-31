from datetime import datetime, timedelta

print("DayWeaver - Daily Planner")

p = {"High": 0, "Medium": 1, "Low": 2}
t = []

try:
    n = int(input("No. of tasks: "))
except:
    n = 2
i = 0
while i < n:
    print("\nTask", i+1)
    a = input("Name: ")
    b = input("Energy (High/Medium/Low): ")

    b = b.capitalize()
    if b not in p:
        b = "Medium"
    t.append([a, b])
    i += 1

# sorting of data in list 
t.sort(key=lambda x: p[x[1]])
time = datetime.strptime("08:00 AM", "%I:%M %p")

print("\nTime\t\t\tTask\tEnergy")
print("-----------------------------------")

for x in t:
    start = time
    end = time + timedelta(hours=2)

    s = start.strftime("%I:%M %p")
    e = end.strftime("%I:%M %p")
    print(s + " - " + e, "\t", x[0], "\t", x[1])
    time = end
print("\nDone")