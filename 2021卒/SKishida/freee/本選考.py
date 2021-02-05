free・コーディングテスト・コード

import datetime

A_A1_A7 = {
  "route_name": "A",
  "start_station": "A1",
  "end_station": "A7",
  "dir": "U",
  "time": datetime.time(5, 55),
  "per": 10
}

A_A1_A13 = {
  "route_name": "A",
  "start_station": "A1",
  "end_station": "A13",
  "dir": "U",
  "time": datetime.time(6, 0),
  "per": 10
}

A_A7_A13 = {
  "route_name": "A",
  "start_station": "A7",
  "end_station": "A13",
  "dir": "U",
  "time": datetime.time(6, 10),
  "per": None
}

B_B1_A7 = {
  "route_name": "B",
  "start_station": "B1",
  "end_station": "A7",
  "dir": "U",
  "time": datetime.time(6, 0),
  "per": 6
}

A_A7_A1 = {
  "route_name": "A",
  "start_station": "A7",
  "end_station": "A1",
  "dir": "D",
  "time": datetime.time(6, 6),
  "per": 10
}

A_A13_A1 = {
  "route_name": "A",
  "start_station": "A13",
  "end_station": "A1",
  "dir": "D",
  "time": datetime.time(5, 52),
  "per": 10
}

A_A13_A7 = {
  "route_name": "A",
  "start_station": "A13",
  "end_station": "A7",
  "dir": "D",
  "time": datetime.time(22, 52),
  "per": None
}

B_A7_B1 = {
  "route_name": "B",
  "start_station": "A7",
  "end_station": "B1",
  "dir": "D",
  "time": datetime.time(6, 11),
  "per": 6
}

train_lists = [A_A1_A7, A_A1_A13, A_A7_A13, B_B1_A7, A_A7_A1, A_A13_A1, A_A13_A7, B_A7_B1]
end_time = datetime.time(23, 0)
take_time = {
  "A": [3, 5, 2, 3, 4, 3, 4, 2, 2, 3, 6, 2],
  "B": [4, 3, 3, 2, 3]
}

if __name__ == '__main__':
  line = list(input().split())

  time_table = []

  for train_list in train_lists:
    if train_list["route_name"] == line[0] and train_list["dir"] == line[2] and train_list["per"] != None:
      start_s, start_n = train_list["start_station"][0], int(train_list["start_station"][1])
      curr_s, curr_n   = line[1][0], int(line[1][1])

      take_minutes = 0
      if start_n < curr_n:
        take_minutes = sum(take_time[line[0]][(start_n-1):(curr_n-1)])

      elif start_n > curr_n:
        take_minutes = sum(take_time[line[0]][(curr_n-1):(start_n-1)])


      curr_time = datetime.datetime.combine(datetime.date.today(), train_list["time"]) + datetime.timedelta(minutes=take_minutes)

      while curr_time.hour < int(line[3]):
        curr_time += datetime.timedelta(minutes=train_list["per"])

      while curr_time.hour < int(line[3]) + 1:
        time_table.append(curr_time.minute)
        curr_time += datetime.timedelta(minutes=train_list["per"])

  time_table.sort()
  answer = str(line[3]) + ":"
  if time_table != []:
    for time in time_table:
      if time < 10:
        answer += " 0{}".format(time)
      else:
        answer += " {}".format(time)
    print(answer)
  else:
    print("No train")