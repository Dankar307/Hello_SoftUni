protecting_nylon_pricing = 1.5
paint_pricing = 14.50
razreditel_pricing = 5.0
bags = 0.4

nylon_needed = int(input())
paint_needed = int(input())
razreditel_needed = int(input())
hours_work = int(input())

paint_price = (paint_needed + paint_needed * 0.1) * paint_pricing
nylon_price = nylon_needed * protecting_nylon_pricing + (2 * protecting_nylon_pricing)
razreditel_price = razreditel_pricing * razreditel_needed
whole_price = paint_price + nylon_price + razreditel_price + bags
workers_salary = (whole_price * 0.3) * hours_work

final_price = whole_price + workers_salary

print(final_price)
