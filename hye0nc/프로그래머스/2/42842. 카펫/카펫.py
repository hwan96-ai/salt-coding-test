def solution(brown, yellow):
    for y_height in range(1, yellow + 1):

        if yellow % y_height == 0:
            y_width = yellow // y_height 
         
            width = y_width + 2
            height = y_height + 2
          
            if (width * height) - yellow == brown:
              
                if width >= height:
                    return [width, height]