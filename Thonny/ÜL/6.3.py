def eelarve(külalisi):
    summa = (10 * külalisi) + 55 
    return summa

kutsutud = int(input("Mitu inimest on kutsutud? "))
tuleb = int(input("Mitu inimest on tuleb? "))

print("Maksimaalne eelarve: " , (eelarve(kutsutud)) , " eurot")
print("Minimaalne eelarve: " , (eelarve(tuleb)) , " eurot")