        import sqlite3
         connection = sqlite3.connect("myTable.db)
         crsr = connection.cursor()
                                      
         #User Table will be:-
          
         sql_command = """CREATE TABLE Users (
          Username   varchar(200) Foreign_key,
          Password   varchar(8)
          );"""
          crsr.execute(sql_command)                          

          #Address Table will be:-

          sql_command = """CREATE TABLE Adresses(
          Username   varchar(200)
          Column_street  varchar(50),
          Pincode        int(6),
          Country        varchar(20),
          Phone          bigint(10)
          );"""
          crsr.execute(sql_command) 
           connection.commit()                           
                            
         #Querry will be:-
                                      
          crsr.execute("SELECT Users.Username,Adresses.Username,FROM Users INNER JOIN Adresses ON Users.Username=Addresses.Username;")
            ans = crsr.fetchball()
             print(ans)                         
            
           
           
           
