#Break Examples:
#example1 break after if
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#example2 break before if
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

#example3 while loop break
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

#Reverse Order Comparison(compares one list to the reverse order of another)
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#, the last index in the second list is len(lst2) - 1, or 5 - 1 = 4. 
# Now in order to get the inverse of the position we are at in the first list, 
# we subtract the index we are at from the end of the second list. So on the first pass,
# we’ll compare the element at position 0 to the element at position 5 - 1 - 0 = 4. 
# On the next pass, we’ll compare the element at position 1 to the element at position 5 - 1 - 1 = 3, and so on.