import random

son = random.randint(1, 100)
urinish = 0

while True:
    taxmin = int(input("1-100 oralig‘ida son taxmin qiling: "))
    urinish += 1
    
    if taxmin == son:
        print(f"Tabriklayman! {urinish} urinishda topdingiz!")
        break
    elif taxmin < son:
        print("Kattaroq son kiriting!")
    else:
        print("Kichikroq son kiriting!")
