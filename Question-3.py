       list1=[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
          
          def consecutive(list)
            a=0,b=0
            for i in range(len(list)):
               if(list[i]==0):
                 a=0
               else:
                 a++
                 if(a>b):
                  b=a
           print("maximum consecutive 1 is: ",b)
