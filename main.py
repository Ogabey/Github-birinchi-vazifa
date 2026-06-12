from employee_service import (
    get_all_xodimlar,
    get_one_employee,
    get_high_salary_xodimlar,
    employee_statistics,
    top_employee
)

print("BARCHA XODIMLAR ")

xodimlar = get_all_xodimlar()
for emp in xodimlar:
    print(
        f"| {emp['ism'].ljust(15)} "
        f"| {str(emp['maosh']).ljust(10)} "
        f"| {emp['bolim'].ljust(10)} |"
    )

print()

print("BIRTA XODIM ")
print(get_one_employee(1))

print()

print(" YUQORI MAOSHLI XODIMLAR")
print(get_high_salary_xodimlar(2500000))

print()

print(" STATISTIKA ")

stats = employee_statistics()

print(
    f"""
Jami xodimlar: {stats['total_xodimlar']}
O'rtacha maosh: {stats['average_salary']}
Eng katta maosh: {stats['max_salary']}
"""
)

print()

print(" ENG KO'P MAOSH OLUVCHI ")
print(top_employee())