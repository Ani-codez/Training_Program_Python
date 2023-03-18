adults=int(input())
child=int(input())
totalRate=(adults*37550.0+child*(1/3)*37550.0)*1.07*0.90
#tax
#totalRate*=(1.07)
#discount
#totalRate*=(0.9)
print(totalRate)
