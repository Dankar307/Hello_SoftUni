def fill_the_box(height,length,width,*args) :
    box_size = height * length * width
    cubes = 0
    for command in args:
        if command == "Finish":
            if cubes >= box_size:
                return f"No more free space! You have {abs(cubes - box_size)} more cubes."
            else:
                return f"There is free space in the box. You could put {abs(cubes - box_size)} more cubes."

        else:
            cubes += command
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))