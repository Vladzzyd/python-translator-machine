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
          "arab":"ar",
          "mandarin":"zh-CN",
          "thai":"th",
          "jerman":"de",
          "prancis":"fr",
          "spanyol":"es",
          "portugis":"pt",
          "italia":"it",
          "belanda":"nl",
          "turki":"tr",
          "hindi":"hi",
          "deteksi":""}
riwayat_terjemahan ={}
daftar_fungsi = ("translate","riwayat","hapus","quit")
daftar_hapus = ("hapus","reset","quit")
counter_riwayat = 1

def judul(teks):
    print(BRIGHT_MAGENTA+"="*50+RESET)
    print(BOLD+BRIGHT_MAGENTA+teks.center(50)+RESET)
    print(BRIGHT_MAGENTA+"="*50+RESET)

def pilih_bahasa(prompt, otomatis=True):
    while True:
        pilihan = input(prompt).lower().strip()

        if pilihan == "q":
            return "q"
        
        if pilihan.isdigit():
            indeks = int(pilihan) - 1
            if 0 <= indeks < len(bahasa):
                bahasa_pilihan = list(bahasa.keys())[indeks]
                if bahasa_pilihan == "deteksi" and not otomatis:
                    print(BRIGHT_RED+"ERROR: deteksi tidak bisa dipilih disini!!\n"+RESET)
                    continue
                return bahasa_pilihan
            else:
                print(BRIGHT_RED+"nomor tidak valid!!\n"+RESET)
        
        elif pilihan in bahasa:
            if pilihan == "deteksi" and not otomatis:
                print(BRIGHT_RED+"deteksi bahasa tidak bisa dipilih disini!!\n"+RESET)
                continue
            return pilihan
        
        else:
            print(BRIGHT_RED+"bahasa tidak dikenali!!\n"+RESET)

def terjemahan():
    global counter_riwayat
    
    judul("TRANSLATOR")
    print(BRIGHT_WHITE+"bahasa tersedia:"+RESET)
    for i, key in enumerate(bahasa, start=1):
        print(f"{BOLD}{BRIGHT_MAGENTA}[{i}]{RESET} {key}")

    asal = pilih_bahasa(BRIGHT_BLUE+"\nmasukkan asal bahasa (nama / angka, q to quit): "+RESET, otomatis=True)
    if asal == "q":
        print(BRIGHT_GREEN+"kembali ke menu utama..\n"+RESET)
        return

    while True:
        tujuan =  pilih_bahasa(BRIGHT_BLUE+"\nmasukkan tujuan bahasa (nama / angka, q to quit): "+RESET, otomatis=False)
        if tujuan == "q":
            print(BRIGHT_GREEN+"kembali ke menu utama..\n"+RESET)
            return
        if tujuan != asal:
            break
        print(BRIGHT_RED+"ERROR: asal dan tujuan bahasa tidak boleh sama!!\n"+RESET)

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
    global counter_riwayat
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
                reindex_riwayat()
                print(BRIGHT_GREEN+f"berhasil menghapus riwayat dengan indeks {indeks}"+RESET)
        
        elif fungsi == "reset":
            riwayat_terjemahan.clear()
            print(BRIGHT_GREEN+"semua riwayat berhasil dihapus!"+RESET)
            counter_riwayat = 1
            return
        
        elif fungsi == "quit":
            print(BRIGHT_GREEN+"keluar dari menu hapus..\n"+RESET)
            return
        
def reindex_riwayat():
    global riwayat_terjemahan, counter_riwayat

    riwayat_baru = {}
    counter = 1

    for data in riwayat_terjemahan.values():
        riwayat_baru[counter] = data
        counter += 1

    riwayat_terjemahan = riwayat_baru
    counter_riwayat = counter

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
