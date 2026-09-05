import csv

input_file = "Employees_NoHeader.csv"
output_file = "employees_insert.sql"

with open(input_file, "r", encoding="utf-8-sig", newline="") as csv_file:
    reader = csv.reader(csv_file)

    with open(output_file, "w", encoding="utf-8") as sql_file:
        for row in reader:
            if len(row) != 8:
                continue

            values = [value.replace("'", "''") for value in row]

            sql = f"""INSERT INTO employees
(Employee_ID, Employee_Name, Gender, Department_ID, Designation, Location, Joining_Date, Employment_Type)
VALUES ('{values[0]}', '{values[1]}', '{values[2]}', '{values[3]}', '{values[4]}', '{values[5]}', '{values[6]}', '{values[7]}');
"""

            sql_file.write(sql)

print("SQL file created successfully.")