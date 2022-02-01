balls = [1,2,3,4]
weapons = [11,22,3,44]

for ball_idx, ball_val in enumerate(balls):
    print("ball : ", ball_val)
    for w_idx, w_val in enumerate(weapons):
        print("weapon : ", w_val)
        if ball_val == w_val : #충돌 체크
            print("충돌")
            break
    else:
        continue
    print("밖 ")
    break