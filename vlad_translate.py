from deep_translator import GoogleTranslator
bahasa = {"indonesia":"id",
          "inggris":"en",
          "jepang":"ja",
          "korea":"ko",
          "russia":"ru"}

def judul(teks):
    print("="*50)
    print(teks.center(50))
    print("="*50)

def terjemahan(asal,tujuan):
    judul("TRANSLATOR MACHINE")
    tl = GoogleTranslator(source=asal, target=tujuan)

    while True:
        teks = input("masukkan teks yang mau diterjemahkan (enter to quit): ")
        if not teks:
            return
        print("hasil terjemahan:", tl.translate(teks))

while True:
    judul("VLAD TRANSLATOR")
    print("bahasa tersedia:")
    for i, key in enumerate(bahasa, start=1):
        print(f"[{i}] {key}")

    while True:
        asal = input("\nmasukkan asal bahasa (q to quit): ").lower().strip()
        if asal == "q":
            print()
            break
        if not asal:
            print("ERROR: asal bahasa tidak boleh kosong!!")
        elif asal not in bahasa:
            print("ERROR: bahasa belum tersedia!!")
        else:
            break
    
    if asal == "q":
        break

    while True:
        tujuan = input("masukkan tujuan bahasa (q to quit): ").lower().strip()
        if tujuan == "q":
            print()
            break
        if not tujuan:
            print("ERROR: tujuan bahasa tidak boleh kosong!!\n")
        elif tujuan not in bahasa:
            print("ERROR: bahasa belum tersedia!!\n")
        elif asal == tujuan:
            print("ERROR: asal dan tujuan bahasa tidak boleh sama!!\n")
        else:
            break

    if tujuan == "q":
        break

    print("\nmemasuki mesin translate..")
    print(f"Menerjemahkan {asal.upper()} ➜ {tujuan.upper()}\n")
    terjemahan(bahasa[asal],bahasa[tujuan])