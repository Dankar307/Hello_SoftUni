N = int(input())
longest_intersection = []
for _ in range(N):
    first_range, second_range = list(input().split("-"))
    first_start,first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")

    set_a = set(int(x) for x in range(int(first_start),int(first_end)+1))
    set_b = set(int(x) for x in range(int(second_start),int(second_end)+1))
    curr_intersection = set_a.intersection(set_b)
    if len(curr_intersection) > len(longest_intersection):
        longest_intersection = list(curr_intersection)
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")