# Get and format current date and time as YYYY-MM-DD HH:MM:SS.
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", current_time)
