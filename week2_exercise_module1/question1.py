import random
num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
k = 3

def k_large(num_list, k):
    
  result = []
  count = len(num_list) - k + 1
  for i in range(count):
      new_list = num_list[i:k+i]
      result.append(max(new_list))
  return result
print(k_large(num_list, k))

  