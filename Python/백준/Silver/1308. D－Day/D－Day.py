from datetime import datetime

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
time = (datetime(y2, m2, d2) - datetime(y1, m1, d1)).days

if time >= 365243:
    print("gg")
else :
    print(f"D-{time}")
