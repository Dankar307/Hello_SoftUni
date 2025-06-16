txt = input()
set_of_text = set()
for el in txt:
    set_of_text.add(el)

for ch in sorted(set_of_text):
    print(f"{ch}: {txt.count(ch)} time/s")