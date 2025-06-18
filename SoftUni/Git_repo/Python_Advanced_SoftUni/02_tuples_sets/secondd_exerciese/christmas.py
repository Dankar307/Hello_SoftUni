from collections import deque
material_boxes = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
gifts = {150:"Doll",250:"Wooden train",300:"Teddy bear",400:"Bicycle"}
presents = {}

while material_boxes and magic:
    total_magic = magic[0] * material_boxes[-1]
    if total_magic in gifts:
        current_present = gifts[total_magic]
        
        
        if current_present not in presents:
            presents[current_present] = 0
        presents[current_present] += 1
        magic.popleft()
        material_boxes.pop()
        
    elif total_magic < 0:
        material_boxes.append(magic.popleft() + material_boxes.pop())
        
    elif total_magic > 0:
        magic.popleft()
        material_boxes[-1] += 15
    else:
        
        if material_boxes[-1] == 0:
            material_boxes.pop()
                
        if magic[0] == 0:
            magic.popleft()
  
   
        
        
if ("Doll" in presents and "Wooden train" in presents) or ("Teddy bear" in presents and "Bicycle" in presents ):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if material_boxes:
    print(f"Materials left: {', '.join(str(x) for x in material_boxes)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in sorted(presents.items()):
    print(f"{key}: {value}")
       
            
        