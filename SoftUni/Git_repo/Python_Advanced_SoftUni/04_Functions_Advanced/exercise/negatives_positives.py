def negatices_positives(*args):
    positives = [el for el in args if el > 0]
    negatives = [el for el in args if el < 0]
    sum_positives = sum(positives)
    sum_negatives = sum(negatives)
    if sum_positives > abs(sum_negatives):
        return f"{sum_negatives}\n{sum_positives}\nThe positives are stronger than the negatives"
    else:
        return f"{sum_negatives}\n{sum_positives}\nThe negatives are stronger than the positives"
nums = [int(el) for el in input().split()]
print(negatices_positives(*nums))