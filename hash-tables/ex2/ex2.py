def reconstruct_trip(tickets):
  #print(tickets)
  ht = {}
  recon_list = []
  for ticket in tickets:
    ht[ticket[0]] = ticket[1]

  recon_list.append(ht[None])

  for i in range(1, len(ht)-1):
    try:
      recon_list.append(ht[recon_list[i-1]])
    except:
      recon_list = []
      print(recon_list)
      return recon_list
  print(recon_list)
  return recon_list



if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  short_set = [
      (None, 'PDX'),
      ('PDX', 'DCA'),
      ('DCA', None)
    ]

  long_set = [
      ('PIT', 'ORD'),
      ('XNA', 'CID'),
      ('SFO', 'BHM'),
      ('FLG', 'XNA'),
      (None, 'LAX'), 
      ('LAX', 'SFO'),
      ('CID', 'SLC'),
      ('ORD', None),
      ('SLC', 'PIT'),
      ('BHM', 'FLG'),
    ]

  incorrect_set = [
      ('LHD', 'DAB'),
      (None, 'HVN'),
      ('MSO', 'SFO'),
      ('RDU', 'ABQ'),
      ('ACY', None),
    ]

  reconstruct_trip(short_set)
  reconstruct_trip(long_set)
  reconstruct_trip(incorrect_set)
