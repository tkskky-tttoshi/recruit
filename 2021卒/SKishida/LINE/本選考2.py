# LINE コーディングテスト（本選考）
# コーディング問題文2.docxの解答

import datetime

def process_time_log():
    travel_log = list(input().split())
    distance = float(travel_log[1])
    time = travel_log[0].split(":")
    sec_mil_time = time.pop(-1).split(".")
    time.append(sec_mil_time[0])
    time.append(sec_mil_time[1])
    time_log = list(map(int, time))
    return time_log, distance

if __name__ == '__main__':
    fare = 410
    pre_time_log, pre_dis = process_time_log()
    total_dis = 0
    low_speed_time = 0
    low_speed_fare = 0
    try:
        while True:
            now_time_log, now_dis = process_time_log()

            sub_hour = now_time_log[0] - pre_time_log[0]
            sub_min = now_time_log[1] - pre_time_log[1]
            sub_sec = now_time_log[2] - pre_time_log[2]
            sub_mil_sec = now_time_log[3] - pre_time_log[3]

            if now_dis * 3600 <= (sub_hour * 3600 + sub_min * 60 + sub_sec + sub_mil_sec / 1000 ) * 10000:
                low_speed_time += sub_hour * 3600 + sub_min * 60 + sub_sec + sub_mil_sec / 1000

            low_speed_fare = (low_speed_time // 90) * 80

            total_dis += now_dis

            if total_dis > 1052:
                total_dis -= 1052
                fare += (total_dis // 237) * 80

            pre_time_log, pre_dis = now_time_log, now_dis

    except EOFError:
        print(int(fare + low_speed_fare))
