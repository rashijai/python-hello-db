import telnetlib 
  
tn = telnetlib.Telnet("database-1-instance-1.c6ralslvhwx7.us-east-1.rds.amazonaws.com", 3306) 
output = tn.read_all() 
print (output)
tn.close()

