import android

# once we have "droid" object we have whole power to control your android phone. :) 
droid = android.Android()
# This is URI for reading call logs 
query = "content://call_log/calls" 
# Query Android db to get call logs 
call_log_data = droid.queryContent(query) 
# get result from call_log query 
call_log_result = call_log_data.result 
# Just print one record to get idea what each row represent
print( call_log_result[0])