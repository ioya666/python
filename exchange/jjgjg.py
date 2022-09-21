eurorate = 7.43
print('welcome to the bank of veksling')
print('how many kroner would u like to veksle to eur?')
dkk = float(input())
print(dkk/eurorate, ' EUR')
print('commission rate of 2 percent is applied aswell')
if dkk/eurorate*0.02 > 0.5:
    print(dkk/eurorate*0.02, 'EUR')
else:
    print(0.5, 'EUR')
