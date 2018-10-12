def get_indices_of_item_weights(weights, limit):
  ht = {}
  for weight in weights:
    ht[weight] = weights.index(weight)

  # for i in range(0, len(weights)):
  #   ht[weights[i]] = i
  #   print(weights[i])

  weight_list = []

  for key in ht:
    if (limit - key) in ht:
      weight_list.append(ht[key])

  weight_list.sort(reverse=True)
  indices = tuple(weight_list)
  print(indices)


  return indices

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  get_indices_of_item_weights([9], 9)
  get_indices_of_item_weights([4, 4], 8)
  get_indices_of_item_weights([4, 6, 10, 15, 16], 21)
  get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 7)