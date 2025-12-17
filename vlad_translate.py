from deep_translator import GoogleTranslator
import textwrap
from itertools import zip_longest 

bahasa = {"indonesia":"id",
          "inggris":"en",
          "jepang":"ja",
          "korea":"ko",
          "russia":"ru"}
riwayat_terjemahan ={}
daftar_fungsi = ("translate","riwayat","quit")
counter_riwayat = 1

def judul(teks):
    print("="*50)
    print(teks.center(50))
    print("="*50)

def terjemahan():
    global counter_riwayat
    
    judul("TRANSLATOR")
    print("bahasa tersedia:")
    for i, key in enumerate(bahasa, start=1):
        print(f"[{i}] {key}")

    while True:
        asal = input("\nmasukkan asal bahasa (q to quit): ").lower().strip()
        if asal == "q":
            print("kembali ke menu utama..\n")
            return
        if not asal:
            print("ERROR: asal bahasa tidak boleh kosong!!")
        elif asal not in bahasa:
            print("ERROR: bahasa belum tersedia!!")
        else:
            print(f"asal bahasa adalah {asal}")
            break

    while True:

        tujuan = input("\nmasukkan tujuan bahasa (q to quit): ").lower().strip()
        if tujuan == "q":
            print("kembali ke menu utama..\n")
            return
        if not tujuan:
            print("ERROR: tujuan bahasa tidak boleh kosong!!")
        elif tujuan not in bahasa:
            print("ERROR: bahasa belum tersedia!!")
        elif asal == tujuan:
            print("ERROR: asal dan tujuan bahasa tidak boleh sama!!")
        else:
            print(f"menerjemahkan bahasa dari {asal} ke {tujuan}..\n")
            break

    tl = GoogleTranslator(source=bahasa[asal], target=bahasa[tujuan])

    while True:
        teks = input("masukkan teks yang mau diterjemahkan (enter to quit): ")
        if not teks:
            print()
            return
        hasil = tl.translate(teks)
        print("hasil terjemahan:",hasil)
        riwayat_terjemahan[counter_riwayat] = {
            "asal": asal,
            "tujuan": tujuan,
            "teks": teks,
            "hasil": hasil
        }

        counter_riwayat += 1


def riwayat():
    judul("RIWAYAT TERJEMAHAN")
    print("menampilkan semua riwayat terjemahan..\n")

    if not riwayat_terjemahan:
        print("belum ada riwayat terjemahan")
        print("kembali ke menu utama..\n")
        return

    for i, data in riwayat_terjemahan.items():
        print(f"[{str(i).center(3)}] {data['asal']} → {data['tujuan']}")

        wrapped_key = textwrap.wrap(data["teks"], 30)
        wrapped_value = textwrap.wrap(data["hasil"], 30)

        print(f"     | {wrapped_key[0].center(30)} | {wrapped_value[0].center(30)}")

        for k, v in zip_longest(wrapped_key[1:], wrapped_value[1:], fillvalue=""):
            print(f"     | {k.center(30)} | {v.center(30)}")


while True:
    judul("VLAD TRANSLATOR")
    for i, key in enumerate(daftar_fungsi, start=1):
        print(f"[{i}] {key}")

    while True:
        fungsi = input("\nmasukkan fungsi yang ingin digunakan: ").lower().strip()
        if not fungsi:
            print("ERROR: fungsi tidak boleh  kosong!!")
        elif fungsi not in daftar_fungsi:
            print("ERROR: fungsi tidak valid!!")
        else:
            break
    
    if fungsi == "translate":
        print("memasuki menu translate..\n")
        terjemahan()

    elif fungsi == "riwayat":
        print("memasuki riwayat terjemahan..\n")
        riwayat()

    elif fungsi == "quit":
        print("mematikan mesin..")
        break
