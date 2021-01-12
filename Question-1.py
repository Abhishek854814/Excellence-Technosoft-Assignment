list1 = [5,10,25,18]
   def sumfunction(list, size):          #sum function for sum of list
      if(size==0):
          return 0
      else:
          return list[size-1]+sum(list, size-1)

    result = sumfunction(list, len(list1))
    print("Sum of given list is: ", total) 

