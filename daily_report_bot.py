import pyautogui
import openpyxl
from openpyxl.styles import Font
from datetime import datetime
import time
import os
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Create folder on Desktop
report_folder = os.path.join(desktop_path, "Daily_Reports")
os.makedirs(report_folder, exist_ok=True)
current_datetime = datetime.now()

current_date = current_datetime.strftime("%Y-%m-%d")
current_time = current_datetime.strftime("%H:%M:%S")
excel_filename = f"daily_status_report_{current_date}.xlsx"
screenshot_filename = f"daily_status_report_{current_date}.png"

excel_path = os.path.join(report_folder, excel_filename)
screenshot_path = os.path.join(report_folder, screenshot_filename)
print("Creating Excel report...")

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Daily Status Report"

# Headers
headers = [
    "Employee Name",
    "Task",
    "Status",
    "Date",
    "Time"
]

# Add headers
for col_num, header in enumerate(headers, start=1):
    cell = ws.cell(row=1, column=col_num)
    cell.value = header
    cell.font = Font(bold=True)

# Report data
report_data = [
    ["Mohammed", "Server Monitoring", "Completed", current_date, current_time],
    ["Syed Rizwan", "Database Backup", "Completed", current_date, current_time],
    ["Keerthi Kumar", "Ticket Resolution", "In Progress", current_date, current_time],
]

# Insert rows
for row in report_data:
    ws.append(row)

# Column widths
ws.column_dimensions["A"].width = 22
ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 18
ws.column_dimensions["D"].width = 15
ws.column_dimensions["E"].width = 15

# Save workbook
wb.save(excel_path)

print(f"Excel file saved at:\n{excel_path}")
print("Opening Excel file...")

os.startfile(excel_path) # Wait for Excel to fully open
time.sleep(8)
print("Capturing screenshot...")

screenshot = pyautogui.screenshot()
screenshot.save(screenshot_path)

print(f"Screenshot saved at:\n{screenshot_path}")
print("\nDaily report automation completed successfully!")
