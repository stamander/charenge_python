qs = [
  "What yor name?"
  "What is favorite color?"
  "What is quest?"
]

n = 0
while True:
  print("Type q to quit")
  a = input(qs[n])
  if a == "q":
    break
  n = (n+1)%3
