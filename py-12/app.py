

counter=0
while True:
    prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210 }
    try:
        animals = input('Heyvanlari girin: ').split(', ')
        if not 3<len(animals)<10:
            raise Exception
        print('Umumi qiymet:', sum(map(lambda animal: prices[animal], animals)))
        i=input("Başqa bir heyvan axtarmaq üçün 'Y', çıxmaq üçün 'Q' daxil edin.")
        if i.upper() == "Y":
            continue
        else:
            break
    except KeyError:
        print("Axtardığınız heyvan Zooparkda yoxdur.")
    except Exception:
        print("En az 3 ve en çox 10 heyvan daxil ede bilersiz!")
    else:
        print("Bilinmeyen xeta baş verdi. Zehmet olmazsa yeniden giriş edin.")


    if counter>=10:
        print("Günlük limiti doldurdunuz!")
        break
    counter+=1


