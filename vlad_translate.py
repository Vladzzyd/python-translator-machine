from deep_translator import GoogleTranslator
import textwrap
from itertools import zip_longest

class VladTranslator:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def __init__(self):
        self.bahasa = {
            "indonesia":"id", "inggris":"en", "jepang":"ja", "korea":"ko",
            "russia":"ru", "arab":"ar", "mandarin":"zh-CN", "thai":"th",
            "jerman":"de", "prancis":"fr", "spanyol":"es", "portugis":"pt",
            "italia":"it", "belanda":"nl", "turki":"tr", "hindi":"hi",
            "deteksi":""
        }

        self.menu_utama = ("translate", "riwayat", "hapus", "quit")
        self.menu_hapus = ("hapus", "reset", "quit")

        self.riwayat = {}
        self.counter = 1

    def judul(self, teks):
        print(self.MAGENTA + "="*50 + self.RESET)
        print(self.BOLD + self.MAGENTA + teks.center(50) + self.RESET)
        print(self.MAGENTA + "="*50 + self.RESET)

    def pilih_bahasa(self, prompt, otomatis=True):
        while True:
            pilih = input(prompt).lower().strip()

            if pilih == "q":
                return "q"

            if pilih.isdigit():
                idx = int(pilih) - 1
                if 0 <= idx < len(self.bahasa):
                    key = list(self.bahasa.keys())[idx]
                    if key == "deteksi" and not otomatis:
                        print(self.RED+"deteksi tidak bisa dipilih!"+self.RESET)
                        continue
                    return key
                print(self.RED+"nomor tidak valid!"+self.RESET)

            elif pilih in self.bahasa:
                if pilih == "deteksi" and not otomatis:
                    print(self.RED+"deteksi tidak bisa dipilih!"+self.RESET)
                    continue
                return pilih

            else:
                print(self.RED+"bahasa tidak dikenali!"+self.RESET)

    def translate(self):
        self.judul("TRANSLATOR")

        for i, key in enumerate(self.bahasa, 1):
            print(f"{self.BOLD}{self.MAGENTA}[{i}]{self.RESET} {key}")

        asal = self.pilih_bahasa(self.BLUE+"\nasal bahasa: "+self.RESET)
        if asal == "q":
            return

        while True:
            tujuan = self.pilih_bahasa(self.BLUE+"tujuan bahasa: "+self.RESET, False)
            if tujuan == "q":
                return
            if tujuan != asal:
                break
            print(self.RED+"asal & tujuan tidak boleh sama!"+self.RESET)

        translator = (
            GoogleTranslator(target=self.bahasa[tujuan])
            if asal == "deteksi"
            else GoogleTranslator(source=self.bahasa[asal], target=self.bahasa[tujuan])
        )

        while True:
            teks = input(self.BLUE+"teks (enter = keluar): "+self.RESET)
            if not teks:
                return

            hasil = translator.translate(teks)
            print(self.GREEN+"hasil: "+hasil+self.RESET)

            self.riwayat[self.counter] = {
                "asal": asal,
                "tujuan": tujuan,
                "teks": teks,
                "hasil": hasil
            }
            self.counter += 1

    def tampil_riwayat(self):
        self.judul("RIWAYAT")

        if not self.riwayat:
            print(self.YELLOW+"riwayat kosong"+self.RESET)
            return

        for i, d in self.riwayat.items():
            print(self.YELLOW+f"[{i}] {d['asal']} → {d['tujuan']}"+self.RESET)

            k = textwrap.wrap(d["teks"], 30)
            v = textwrap.wrap(d["hasil"], 30)

            print(self.GREEN+f" | {k[0]:^30} | {v[0]:^30}"+self.RESET)
            for a, b in zip_longest(k[1:], v[1:], fillvalue=""):
                print(self.GREEN+f" | {a:^30} | {b:^30}"+self.RESET)

    def reindex(self):
        self.riwayat = {i+1: v for i, v in enumerate(self.riwayat.values())}
        self.counter = len(self.riwayat) + 1

    def hapus_riwayat(self):
        self.judul("HAPUS RIWAYAT")

        if not self.riwayat:
            print(self.YELLOW+"riwayat kosong"+self.RESET)
            return

        cmd = input(self.BLUE+"hapus / reset / quit: "+self.RESET)
        if cmd == "reset":
            self.riwayat.clear()
            self.counter = 1
            print(self.GREEN+"riwayat direset"+self.RESET)

        elif cmd == "hapus":
            idx = input(self.BLUE+"indeks: "+self.RESET)
            if idx.isdigit() and int(idx) in self.riwayat:
                del self.riwayat[int(idx)]
                self.reindex()
                print(self.GREEN+"riwayat dihapus"+self.RESET)

    def run(self):
        while True:
            self.judul("VLAD TRANSLATOR")
            for i, m in enumerate(self.menu_utama, 1):
                print(f"[{i}] {m}")

            cmd = input(self.BLUE+"pilih menu: "+self.RESET).lower()
            if cmd == "translate":
                self.translate()
            elif cmd == "riwayat":
                self.tampil_riwayat()
            elif cmd == "hapus":
                self.hapus_riwayat()
            elif cmd == "quit":
                print(self.GREEN+"bye bye 👋"+self.RESET)
                break

if __name__ == "__main__":
    VladTranslator().run()
