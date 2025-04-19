def cal_minutes(check_time):
    check_hour, check_minute = int(check_time[0:2]), int(check_time[3:5])
    return check_hour*60 + check_minute

def solution(book_time):
    books = []
    
    for checkin_time,checkout_time in book_time:
        checkin_m,checkout_m = cal_minutes(checkin_time),cal_minutes(checkout_time)+10
        books.append([checkin_m,checkout_m])
    books = sorted(books)
    rooms = []
    #예약
    for check_in, check_out in books:
        room_found = False

        # 기존 객실 중 사용 가능한 객실이 있는지 확인
        for i in range(len(rooms)):
            if rooms[i] <= check_in:  # 퇴실 시간이 새 손님의 입실 시간 이전이면
                rooms[i] = check_out  # 해당 객실에 새 손님 배정
                room_found = True
                break

        # 사용 가능한 객실이 없으면 새 객실 추가
        if not room_found:
            rooms.append(check_out)
    return len(rooms)