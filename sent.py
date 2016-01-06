import csv, re

filename = 'Ratings_Warriner_et_al.csv'

ratings_array = []

with open(filename, 'rb') as myfile:
  reader = csv.reader(myfile)
  for row in reader:
    ratings_array.append(row)

print(len(ratings_array))
print(ratings_array[13915])

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

def dict_compare(str1, str2):
  if str1.is_empty():

def dict_lookup_aux(str, first, last):
  #if low > high: # termination case  
    #return -1  
  #middle = (low + high) / 2 # gets the middle of the array  
  #if array[middle] == key:  # if the middle is our key  
    #return middle  
  #elif key < array[middle]: # our key might be in the left sub-array  
    #return binarySearch(array, key, low, middle-1)  
  #else:                     # our key might be in the right sub-array  
    #return binarySearch(array, key, middle+1, high) 
  return 0

# binary search for index 1 to len(ratings_array); returns 0 if not found
def dict_lookup(str):
  return dict_lookup_aux(str, 1, 13916)

def sent(twt):
  result = [0,0,0]
  bagofwords = re.sub("[^\w]", " ",  twt).split()
  for word in bagofwords:
    index = dict_lookup(word)
    result[0] = result[0] + ratings_array[index][1]
    result[1] = result[1] + ratings_array[index][4]
    result[2] = result[2] + ratings_array[index][7]
  for i in xrange(0,3):
    result[i] = result[i]/float(len(bagofwords))
  return result