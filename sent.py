import csv, re

filename = 'Ratings_Warriner_et_al.csv'

ratings_array = []

with open(filename, 'rb') as myfile:
  reader = csv.reader(myfile)
  for row in reader:
    ratings_array.append(row)

def dict_order(char):
  if char == " ":
    return 0
  if char == "A" or char == "a":
    return 1
  if char == "B" or char == "b":
    return 2
  if char == "C" or char == "c":
    return 3
  if char == "D" or char == "d":
    return 4
  if char == "E" or char == "e":
    return 5
  if char == "F" or char == "f":
    return 6
  if char == "G" or char == "g":
    return 7
  if char == "H" or char == "h":
    return 8
  if char == "I" or char == "i":
    return 9
  if char == "J" or char == "j":
    return 10
  if char == "K" or char == "k":
    return 11
  if char == "L" or char == "l":
    return 12
  if char == "M" or char == "m":
    return 13
  if char == "N" or char == "n":
    return 14
  if char == "O" or char == "o":
    return 15
  if char == "P" or char == "p":
    return 16
  if char == "Q" or char == "q":
    return 17
  if char == "R" or char == "r":
    return 18
  if char == "S" or char == "s":
    return 19
  if char == "T" or char == "t":
    return 20
  if char == "U" or char == "u":
    return 21
  if char == "V" or char == "v":
    return 22
  if char == "W" or char == "w":
    return 23
  if char == "X" or char == "x":
    return 24
  if char == "Y" or char == "y":
    return 25
  if char == "Z" or char == "z":
    return 26

# dict_compare output:
# 1 means str1 < str2;
# 0 means str1 = str2
# -1 means str1 > str2 (in alphabetic dictionary order)
def dict_compare(str1, str2):
  if not str1:
    if not str2:
      return 0
    return 1
  if not str2:
    return -1
  if dict_order(str1[0]) < dict_order(str2[0]):
    return 1
  elif dict_order(str1[0]) > dict_order(str2[0]):
    return -1
  else:
    return dict_compare(str1[1:], str2[1:])

def dict_lookup_aux(str, first, last):
  if last - first <= 1:
    if str == ratings_array[first][1]:
      return first
    elif str == ratings_array[last][1]:
      return last
    else:
      return 0
  mid = (last + first)/2
  if str == ratings_array[mid][1]:
    return mid
  elif dict_compare(str, ratings_array[mid][1]) == 1:
    return dict_lookup_aux(str, first, mid-1)
  else:
    return dict_lookup_aux(str, mid+1, last)

# binary search for index 1 to len(ratings_array); returns 0 if not found
def dict_lookup(str):
  return dict_lookup_aux(str.lower(), 1, 13915)

def sent(twt):
  foundcount = 0
  result = [0,0,0]
  try:
    bagofwords = re.sub("[^\w]", " ",  twt).split()
  except TypeError:
    print twt
    bagofwords = []
  for word in bagofwords:
    index = dict_lookup(word)
    if index > 0:
      foundcount +=1 
      result[0] = result[0] + float(ratings_array[index][2])
      result[1] = result[1] + float(ratings_array[index][5])
      result[2] = result[2] + float(ratings_array[index][8])
  if foundcount > 0:
    for i in xrange(0,3):
      result[i] = result[i]/foundcount
  return result