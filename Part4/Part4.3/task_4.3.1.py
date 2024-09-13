zoom_speed, flash_speed = int(input()), int(input())
if zoom_speed > flash_speed:
    print('NO')
elif zoom_speed < flash_speed:
    print('YES')
else:
    print("Don't know")
