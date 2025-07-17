""" EN BUYUK SAYIYI BUL

list = [2,5,6,55,4,1,99]

def en_buyuk_sayi_bulucu():
    gecici = list[0]
    for sayi in list:
        if sayi > gecici:
            gecici = sayi
    return gecici

print(en_buyuk_sayi_bulucu())  

"""
""" KELİME SAYISI BUL

metin = "Görev: def kelime_sayaci(metin): adında bir fonksiyon yaz. Bu fonksiyon, aldığı bir metin (string) içindeki toplam kelime sayısını döndürmelidir."

def kelime_sayaci(metin):
    kelimeler = metin.split()
    return (len(kelimeler))

sonuc = kelime_sayaci(metin)


print("Verilen metindeki kelime sayisi:",sonuc)

"""
""" POLINDROM KELİME 

def is_polindrome(kelime):
    kontrol = kelime
    kontrol = kontrol.lower()
    if kontrol == kontrol[::-1]:
        return True
    else:
        return False
    
print(is_polindrome("Yapay"))    

"""
""" CIFT SAYILARI FILTRELEME

def cift_sayilari_bul(sayi_listesi):
    cift_sayilar =  []
    for sayi in sayi_listesi:
        if sayi % 2 == 0:
            cift_sayilar.append(sayi)
    return cift_sayilar

ornek_liste = [5,66,3,24,20,10,55,7,96,3]
sonuc = cift_sayilari_bul(ornek_liste)

print("verilen listedeki cift sayilar:",sonuc)

"""
""" KELIME FREKANS SAYACI

def frekans_hesapla(metin):
    yeni_metin = metin.lower()
    noktalamalar = [".", ",", "?", "!", ":", ";"]

    for isaret in noktalamalar:
        yeni_metin = yeni_metin.replace(isaret, "") 

    kelimeler = yeni_metin.split()

    frekanslar = {}

    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1   
    return frekanslar

metin = "bu bir deneme metnidir, evet sadece bir deneme metnidir"
print("verilen metindeki kelime sayilari su sekildedir:")
print(frekans_hesapla(metin))

"""

