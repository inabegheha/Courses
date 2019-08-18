#NABEGHEHA.COM

def second_smallest(numbers):
  if (len(numbers)<2):
    return ("kamtar az 2 nemishe hesab kard")
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return ("bayad bishtar az 2 ta bashe")
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x) #inja add mikonim k adad tekrari be list ezafe nashe
  uniq_items.sort()    
  return  uniq_items[1]   

print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2,2]))
print(second_smallest([2]))


# Sample Output:

# -2
# 0
# 0
# None
# None