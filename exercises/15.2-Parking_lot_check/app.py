parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(park_state):
  state = {"total_slots":0, "avaliable_slots":0, "occupied_slots":0}
  for i in park_state:
    for j in i:
        if j > 0:
          state["total_slots"]+=1
        if j >= 2:
          state["avaliable_slots"]+=1
        elif j == 1:
          state["occupied_slots"]+=1
  return state

print(get_parking_lot(parking_state))