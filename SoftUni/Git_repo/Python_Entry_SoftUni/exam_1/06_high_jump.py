wanted_height = int(input())
bar_height = wanted_height - 30
fails_count = 0
is_successful = False
jump_count = 0
while bar_height <= wanted_height:
    jump_try = int(input())
    jump_count += 1
    if jump_try > bar_height:
        fails_count = 0
        bar_height += 5
    else:
        fails_count += 1
        if fails_count == 3:
            is_successful = False
            break
else:
    is_successful = True
if is_successful:
    print(f"Tihomir succeeded, he jumped over {wanted_height}cm after {jump_count} jumps.")
else:
    print(f'Tihomir failed at {bar_height}cm after {jump_count} jumps.')
