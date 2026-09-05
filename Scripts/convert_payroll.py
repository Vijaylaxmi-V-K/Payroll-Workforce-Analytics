import csv

input_file = "Payroll_DB.csv"
output_file = "payroll_insert.sql"

with open(input_file, "r", encoding="utf-8-sig", newline="") as csv_file:
    reader = csv.reader(csv_file)

    next(reader)  # skip header

    with open(output_file, "w", encoding="utf-8") as sql_file:
        for row in reader:
            if len(row) != 14:
                continue

            values = [value.replace("'", "''") for value in row]

            sql = (
                "INSERT INTO payroll "
                "(Payroll_ID, Employee_ID, Month, Basic_Salary, HRA, "
                "Allowances, Overtime_Pay, Bonus, Gross_Salary, PF, Tax, "
                "Other_Deductions, Net_Salary, Payment_Status) "
                "VALUES ('"
                + "', '".join(values)
                + "');\n"
            )

            sql_file.write(sql)

print("Payroll SQL file created successfully.")