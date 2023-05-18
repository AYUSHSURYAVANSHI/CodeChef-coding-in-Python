#Solution as follows

c = 0

#Note that print(c) is coming after c = c + 1
#How does this change the condition of the while loop?
while c < 15 :
  c = c + 1
  if c == 11 :
   continue
  print(c)
 
