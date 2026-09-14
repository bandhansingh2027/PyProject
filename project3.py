import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [
["Engineering Chemistry", 81],
["Engineering Mathematics-I", 64],
["Fundamentals of Electrical Engineering", 81],
["Programming for Problem Solving", 64],
["Environment and Ecology", 78],
["Engineering Chemistry Lab", 96],
["Basic Electrical Engineering Lab", 95],
["Programming for Problem Solving Lab", 96],
["Engineering Graphics & Design Lab", 95],

["Engineering Physics", 64],
["Engineering Mathematics-II", 60],
["Fundamentals of Electronics Engineering", 72],
["Fundamentals of Mechanical Engineering", 72],
["Soft Skills", 73],
["Engineering Physics Lab", 96],
["Basic Electronics Engineering Lab", 95],
["English Language Lab", 97],
["Workshop Practice Lab", 97],

["Material Science", 55],
["Technical Communication", 79],
["Data Structure", 78],
["Computer Organization and Architecture", 68],
["Discrete Structures & Theory of Logic", 63],
["Cyber Security", 60],
["Data Structure Lab", 98],
["Computer Organization and Architecture Lab", 98],
["Web Designing Workshop", 98],
["Internship Assessment / Mini Project", 51],

["Mathematics-IV", 70],
["Universal Human Value and Professional Ethics", 61],
["Operating System", 76],
["Theory of Automata and Formal Languages", 72],
["Object Oriented Programming with Java", 81],
["Python Programming", 75],
["Operating System Lab", 98],
["Object Oriented Programming with Java Lab", 98],
["Cyber Security Workshop", 98],
["Sports and Yoga-II", 99],

["Database Management System", 77],
["Web Technology", 81],
["Design and Analysis of Algorithm", 63],
["Object Oriented System Design with C++", 69],
["Application of Soft Computing", 82],
["Database Management System Lab", 98],
["Web Technology Lab", 97],
["Design and Analysis of Algorithm Lab", 98],
["Mini Project / Internship Assessment", 95],

["Software Engineering", 92],
["Data Analytics", 79],
["Computer Networks", 77],
["Blockchain Architecture Design", 82],
["Idea to Business Model", 70],
["Software Engineering Lab", 98],
["Data Analytics Lab", 97],
["Computer Networks Lab", 98]
]

df = pd.DataFrame(data, columns=["Subject", "Marks"])

semesters = (
    ["Semester 1"] * 9 +
    ["Semester 2"] * 9 +
    ["Semester 3"] * 10 +
    ["Semester 4"] * 10 +
    ["Semester 5"] * 9 +
    ["Semester 6"] * 8
)

df["Semester"] = semesters


# dataset containing your marks from Semester 1 to Semester 6 using Pandas.

print(df)


# semesters are present in  dataset

print(df["Semester"].nunique())


# subjects  studied in total?

print(df["Subject"].nunique())


#  Findr highest marks.

print(df["Marks"].max())


#  Find  lowest marks.

print(df["Marks"].min())


#  Which semester has the highest total marks?

semester_total = df.groupby("Semester")["Marks"].sum()
print(semester_total.idxmax(), semester_total.max())


#  Which semester has the lowest total marks?

print(semester_total.idxmin(), semester_total.min())


#  Display the first five records.

print(df.head())


#  Find  average marks for each semester.

semester_average = df.groupby("Semester")["Marks"].mean()
print(semester_average)


#  Create a line graph of semester-wise average marks.

plt.figure(figsize=(8,5))
plt.plot(semester_average.index, semester_average.values, marker="o")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Semester-wise Average Marks")
plt.show()


#  Create a bar graph of subject-wise average marks.

subject_average = df.groupby("Subject")["Marks"].mean()

plt.figure(figsize=(12,6))
plt.bar(subject_average.index, subject_average.values)
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")
plt.xticks(rotation=90)
plt.show()


# . Identify  highest-performing subject.

print(subject_average.idxmax(), subject_average.max())


#  Identify  lowest-performing subject.

print(subject_average.idxmin(), subject_average.min())


#  Identify your best and worst semester.

print(semester_average.idxmax(), semester_average.max())
print(semester_average.idxmin(), semester_average.min())


#  Calculate the improvement between Semester 1 and Semester 6.

improvement = semester_average["Semester 6"] - semester_average["Semester 1"]
print(improvement)


#  Calculate mean, median, maximum, minimum and standard deviation using NumPy.

print(np.mean(df["Marks"]))
print(np.median(df["Marks"]))
print(np.max(df["Marks"]))
print(np.min(df["Marks"]))
print(np.std(df["Marks"]))



# Q18. Set an academic target of 75% and show it on your graph using axhline().

plt.figure(figsize=(8,5))
plt.plot(semester_average.index, semester_average.values, marker="o")
plt.axhline(y=75, linestyle="--")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Performance with Academic Target")
plt.show()


# Q19. Compare your performance with the class average
# Q20. Create a 2×2 Matplotlib dashboard


#Write 5 observations based on your visualizations.

print("1. Semester 6 has the highest average performance.")
print("2. Semester 3 has the lowest average performance.")
print("3. Practical and laboratory subjects generally have higher marks.")
print("4. Semester-wise performance improves in the later semesters.")
print("5. Some subjects are below the academic target of 75%.")