import csv

input_file = "Attendance_DB.csv"
output_file = "attendance_insert.sql"

with open(input_file, "r", encoding="utf-8-sig", newline="") as csv_file:
    reader = csv.reader(csv_file)

    next(reader)

    with open(output_file, "w", encoding="utf-8") as sql_file:
        for row in reader:
            if len(row) != 8:
                continue

            values = [value.replace("'", "''") for value in row]

            sql = (
                "INSERT INTO attendance "
                "(Attendance_ID, Employee_ID, Month, Working_Days, "
                "Present_Days, Leave_Days, Absent_Days, Overtime_Hours) "
                "VALUES ('"
                + "', '".join(values)
                + "');\n"
            )

            sql_file.write(sql)

print("Attendance SQL file created successfully.")