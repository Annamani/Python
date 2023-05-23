i = 1
while i < 6:
  print(i)
  i += 1

# BReak
j = 1
print("Break")
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1

#   Continue
k = 1
print("Continue")
while k < 10:
  k += 1
  if k == 3:
    continue
  print(k)