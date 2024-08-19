import random

def tas_kagit_makas_ADINIZ_SOYADINIZ():
    
    name = input("İsminiz Nedir ?")

    print(name + " Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
    print("Oyun kuralları: Taş, kağıt, makas seçeneklerinden birini seçin.")
    print("İlk iki turu kazanan oyunun galibi olur.")
    print("Oyundan çıkmak için 'q' tuşuna basın.")
    
    secenekler = ["taş", "kağıt", "makas"]
    oyun_sayisi = 0
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0

    while True:
        tur_sayisi = 0
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0
        
        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            oyuncu_secimi = input("Taş, kağıt veya makas seçin: ").lower()
            if oyuncu_secimi == 'q':
                print("Oyundan çıkılıyor...")
                return
            
            if oyuncu_secimi not in secenekler:
                print("Geçersiz seçenek, tekrar deneyin.")
                continue
            
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
            
            if oyuncu_secimi == bilgisayar_secimi:
                print("Beraberlik!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu kazandınız!")
                oyuncu_galibiyetleri += 1
            else:
                print("Bu turu kaybettiniz!")
                bilgisayar_galibiyetleri += 1
            
            tur_sayisi += 1
            print(f"Skor - Siz: {oyuncu_galibiyetleri}, Bilgisayar: {bilgisayar_galibiyetleri}")
        
        if oyuncu_galibiyetleri == 2:
            print("Tebrikler! Oyunu kazandınız!")
        else:
            print("Üzgünüz, bilgisayar oyunu kazandı.")
        
        tekrar_oyna = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
        if tekrar_oyna != 'e':
            print("Oyun sona erdi.")
            break

tas_kagit_makas_ADINIZ_SOYADINIZ()
