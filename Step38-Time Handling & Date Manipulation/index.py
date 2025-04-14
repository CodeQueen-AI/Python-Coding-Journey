#Current Date & Time
from datetime import datetime
now = datetime.now() 
print(now)         

#Set a Specific Date & Time
from datetime import datetime
custom_date = datetime(2023, 5, 17, 12, 30, 45)
print(custom_date)  

#Convert Date to String Format
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  

#Convert String to Date (Parsing)
from datetime import datetime
date_string = "2025-03-22 14:35:10"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date) 

#Find Days Difference (Date Subtraction)
from datetime import datetime
now = datetime.now()
print(now.date()) 
print(now.time())  
