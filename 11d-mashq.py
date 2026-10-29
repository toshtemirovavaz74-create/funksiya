def davlatlar():
    davlatlar = ["O'zbekiston", "AQSH", "Rossiya", "Xitoy","Yaponiya", "Turkiya", "Germaniya"]

    print("1. Davlatlar ro'yxati:", davlatlar)

    print("2. Ro'yxat uzunligi:", len(davlatlar))

    print("3. Alifbo bo'yicha:", sorted(davlatlar))

    print("4. Teskari alifbo:", sorted(davlatlar, reverse=True))

    print("5. Asl ro'yxat:", davlatlar)

    teskari = davlatlar.copy()
    teskari.reverse()
    print("6. Teskari ro'yxat:", teskari)

    alfavit = davlatlar.copy()
    alfavit.sort()
    print("7. sort() alifbo:", alfavit)

    alfavit.sort(reverse=True)
    print("   sort() teskari:", alfavit)

    juft_sonlar = list(range(120, 1201, 2))
    print("8. Juft sonlar:", juft_sonlar)

    print("9. Yig'indi:", sum(juft_sonlar))

    print("10. Ayirma:", max(juft_sonlar) - min(juft_sonlar))

    print("11. Elementlar soni:", len(juft_sonlar))

    print("12. Boshidan 20 ta:", juft_sonlar[:20])

    orta = len(juft_sonlar) // 2
    print("    O'rtasidan 20 ta:", juft_sonlar[orta-10:orta+10])

    print("    Oxiridan 20 ta:", juft_sonlar[-20:])

def taomlar():
    taomlar = ["Osh", "Manti", "Somsa", "Sho'rva", "Lag'mon"]
    print("\n13. Taomlar:", taomlar)

    nonushta = taomlar.copy()
    print("14. Nonushta:", nonushta)

    nonushta.clear()
    nonushta.extend(["Tuxum", "Non", "Sut", "Pishloq", "Asal"])

    nonushta.append("Sariyog'")
    nonushta.append("Bo'tqa")

    print("15. Yangilangan nonushta:", nonushta)
    print("16. Barcha taomlar:", taomlar)
    print("    Nonushta taomlari:", nonushta)
