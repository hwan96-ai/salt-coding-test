def solution(n, w, num):
    row = (num - 1) // w   #1층이면 0나옴
    idx_in_row = (num - 1) % w
    col = w - 1 - idx_in_row if row % 2 == 1 else idx_in_row
    
    count = 1  # 상자빼는거 이미 1회
    total_rows = (n + w - 1) // w
    
    for r in range(row + 1, total_rows):  # row + 1부터 시작 (num 위의 층)
        boxes_in_row = min(w, n - (r * w))
        if boxes_in_row <= 0: # 박스가 없으면 안빼도됨
            continue
            
        if r % 2 == 0:  # 홀수 층 
            if col < boxes_in_row:
                count += 1
        else:  # 짝수 층
            if w - 1 - col < boxes_in_row:
                count += 1
    
    return count