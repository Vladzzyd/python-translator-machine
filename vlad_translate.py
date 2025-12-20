from deep_translator import GoogleTranslator
import textwrap
from itertools import zip_longest 

BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD      = "\033[1m"

bahasa = {"indonesia":"id",
          "inggris":"en",
          "jepang":"ja",
          "korea":"ko",
          "russia":"ru",
          "deteksi":""}
riwayat_terjemahan ={}
daftar_fungsi = ("translate","riwayat","hapus","quit")
daftar_hapus = ("hapus","reset","quit")
counter_riwayat = 1

def judul(teks):
    print(BRIGHT_MAGENTA+"="*50+RESET)
    print(BOLD+BRIGHT_MAGENTA+teks.center(50)+RESET)
    print(BRIGHT_MAGENTA+"="*50+RESET)

def terjemahan():
    global counter_riwayat
    
    judul("TRANSLATOR")
    print(BRIGHT_WHITE+"bahasa tersedia:"+RESET)
    for i, key in enumerate(bahasa, start=1):
        print(f"{BOLD}{BRIGHT_MAGENTA}[{i}]{RESET} {key}")

    while True:
        asal = input(BRIGHT_BLUE+"\nmasukkan asal bahasa (q to quit): "+RESET).lower().strip()
        if asal == "q":
            print(BRIGHT_GREEN+"kembali ke menu utama..\n"+RESET)
            return
        if not asal:
            print(BRIGHT_RED+"ERROR: asal bahasa tidak boleh kosong!!"+RESET)
        elif asal not in bahasa:
            print(BRIGHT_RED+"ERROR: bahasa belum tersedia!!"+RESET)
        else:
            print(BRIGHT_GREEN+f"asal bahasa adalah {asal}"+RESET)
            break

    while True:

        tujuan = input(BRIGHT_BLUE+"\nmasukkan tujuan bahasa (q to quit): "+RESET).lower().strip()
        if tujuan == "q":
            print(BRIGHT_GREEN+"kembali ke menu utama..\n"+RESET)
            return
        if not tujuan:
            print(BRIGHT_RED+"ERROR: tujuan bahasa tidak boleh kosong!!"+RESET)
        elif tujuan not in bahasa:
            print(BRIGHT_RED+"ERROR: bahasa belum tersedia!!"+RESET)
        elif asal == tujuan:
            print(BRIGHT_RED+"ERROR: asal dan tujuan bahasa tidak boleh sama!!"+RESET)
        else:
            print(BRIGHT_GREEN+f"menerjemahkan bahasa dari {asal} ke {tujuan}..\n"+RESET)
            break

    if asal == "deteksi":
        asal = "deteksi bahasa"
        tl = GoogleTranslator(target=bahasa[tujuan])

    else: 
        tl = GoogleTranslator(source=bahasa[asal], target=bahasa[tujuan])

    while True:
        teks = input(BRIGHT_BLUE+"masukkan teks yang mau diterjemahkan (enter to quit): "+RESET)
        if not teks:
            print()
            return
        hasil = tl.translate(teks)
        print(BRIGHT_GREEN+"hasil terjemahan:"+RESET+hasil)
        riwayat_terjemahan[counter_riwayat] = {
            "asal": asal,
            "tujuan": tujuan,
            "teks": teks,
            "hasil": hasil
        }

        counter_riwayat += 1

def riwayat():
    judul("RIWAYAT TERJEMAHAN")
    print(BRIGHT_WHITE+"menampilkan semua riwayat terjemahan..\n"+RESET)

    if not riwayat_terjemahan:
        print(BRIGHT_YELLOW+"belum ada riwayat terjemahan"+RESET)
        print(BRIGHT_GREEN+"kembali ke menu utama..\n"+RESET)
        return

    for i, data in riwayat_terjemahan.items():
        print(BRIGHT_YELLOW+f"[{str(i).center(3)}] {data['asal']} → {data['tujuan']}"+RESET)

        wrapped_key = textwrap.wrap(data["teks"], 30)
        wrapped_value = textwrap.wrap(data["hasil"], 30)

        print(BRIGHT_GREEN+f"     | {wrapped_key[0].center(30)} | {wrapped_value[0].center(30)}"+RESET)

        for k, v in zip_longest(wrapped_key[1:], wrapped_value[1:], fillvalue=""):
            print(BRIGHT_GREEN+f"     | {k.center(30)} | {v.center(30)}"+RESET)
    print()

def hapus():
    while True:
        judul("MENU HAPUS RIWAYAT")

        if not riwayat_terjemahan:
            print(BRIGHT_YELLOW+"\nriwayat tersimpan kosong"+RESET)
            print(BRIGHT_GREEN+"kembali ke menu utama..\n"+RESET)
            return

        for i, key in enumerate(daftar_hapus, start=1):
            print(f"{BOLD}{BRIGHT_MAGENTA}[{i}]{RESET} {key}")

        while True:
            fungsi = input(BRIGHT_BLUE+"\nmasukkan fungsi yang ingin digunakan: "+RESET).lower().strip()
            if not fungsi:
                print(BRIGHT_RED+"ERROR: fungsi tidak boleh kosong!!"+RESET)
            elif fungsi not in daftar_hapus:
                print(BRIGHT_RED+"ERROR: fungsi tidak valid!!"+RESET)
            else:
                break
        
        if fungsi == "hapus":
            while True:
                indeks = input(BRIGHT_BLUE+"masukkan indeks riwayat yang ingin dihapus (q to quit): "+RESET)
                if indeks == "q":
                    print("kembali ke menu hapus..\n")
                    break
                if not indeks.isdigit():
                    print(BRIGHT_RED+"indeks harus angka!"+RESET)
                    continue

                indeks = int(indeks)
                if indeks not in riwayat_terjemahan:
                    print(BRIGHT_RED+f"ERROR: riwayat dengan indeks {indeks} tidak ditemukan!!\n"+RESET)
                    continue
            
                del riwayat_terjemahan[int(indeks)]
                print(BRIGHT_GREEN+f"berhasil menghapus riwayat dengan indeks {indeks}"+RESET)
        
        elif fungsi == "reset":
            riwayat_terjemahan.clear()
            print(BRIGHT_GREEN+"semua riwayat berhasil dihapus!"+RESET)
            return
        
        elif fungsi == "quit":
            print(BRIGHT_GREEN+"keluar dari menu hapus..\n"+RESET)
            return

while True:
    judul("VLAD TRANSLATOR")
    for i, key in enumerate(daftar_fungsi, start=1):
        print(f"{BOLD}{BRIGHT_MAGENTA}[{i}]{RESET} {key}")

    while True:
        fungsi = input(BRIGHT_BLUE+"\nmasukkan fungsi yang ingin digunakan: "+RESET).lower().strip()
        if not fungsi:
            print(BRIGHT_RED+"ERROR: fungsi tidak boleh  kosong!!"+RESET)
        elif fungsi not in daftar_fungsi:
            print(BRIGHT_RED+"ERROR: fungsi tidak valid!!"+RESET)
        else:
            break
    
    if fungsi == "translate":
        print(BRIGHT_GREEN+"memasuki menu translate..\n"+RESET)
        terjemahan()

    elif fungsi == "riwayat":
        print(BRIGHT_GREEN+"memasuki riwayat terjemahan..\n"+RESET)
        riwayat()

    elif fungsi  == "hapus":
        print(BRIGHT_GREEN+"memasuki menu hapus..\n"+RESET)
        hapus()

    elif fungsi == "quit":
        print(BRIGHT_GREEN+"mematikan mesin.."+RESET)
        break
