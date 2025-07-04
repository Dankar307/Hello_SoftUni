def sorting_cheeses(**kwargs):
    cheese_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''
    for cheese_name, quantities in cheese_dict:
        result += cheese_name + '\n'

        for quantity in sorted(quantities, reverse=True):
            result += str(quantity) + '\n'
    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)