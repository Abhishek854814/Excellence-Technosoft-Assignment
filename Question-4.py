         #User Table will be:-
          
          CREATE TABLE Users (
          Username   varchar(200) Foreign_key,
          Password   varchar(8)
          );

          #Address Table will be:-

          CREATE TABLE Adresses(
          Username   varchar(200)
          Column_street  varchar(50),
          Pincode        int(6),
          Country        varchar(20),
          Phone          bigint(10)
          );

         #Querry will be:-
          
           SELECT Users.Username,
           Adresses.Username,
            FROM Users
           INNER JOIN Adresses ON
           Users.Username=Addresses.Username;
