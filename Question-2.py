        dict1={'1':70,'2':20,'3':50,'4':60}
          def greatervalue(dict)               #greatervalue is function for highest value
            highest = max(dict, key=dict.get)
            hvalue = max(dict.values())
            print("{",highest,":",hvalue"}")
             
           print(greatervalue(dict1))
