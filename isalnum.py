s=input()
if s.isalpha() or s.isdigit():
  print("No")
elif any(i.isalpha() for i in s):
  if any(i.isdigit() for i in s):
    print("Yes")
  else:
    print("No")    
else:
   #print result
  print("No")
