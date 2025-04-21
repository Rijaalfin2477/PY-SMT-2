#ALFIN ALFRIZA - FTI - 241552018155635


def bilprim(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

angka = int(input("Masukkan sebuah angka: "))
if bilprim(angka):
    print(f"{angka} merupakan bilangan prima.")
else:
    print(f"{angka} merupakan bilangan prima.")
