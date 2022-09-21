eurorate = 7.43
krate = 0.16
mkrate = 0.5
print('welcome to the bank of veksling')
print('how many kroner would u like to veksle to eur?')
dkk = float(input())
finalveksel = dkk/eurorate
final_kommission = dkk/eurorate*krate
print(finalveksel, ' EUR')
print('commission rate of 2 percent is applied aswell')
print('after kalkulus u get this')
if final_kommission > mkrate:
    print(finalveksel - final_kommission, 'EUR')
else:
    print(finalveksel - mkrate, 'EUR')
