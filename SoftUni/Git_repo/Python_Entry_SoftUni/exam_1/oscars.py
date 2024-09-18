naem = int(input())


statuetki = naem - (naem * 0.3)
ketaring = statuetki - (statuetki * 0.15)
ozvuchavane = ketaring * 0.5
whole_sum = naem + statuetki + ketaring + ozvuchavane
print(f"{whole_sum:.2f}")
