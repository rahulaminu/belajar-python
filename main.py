# Import library
import random

welcome_message = "WELCOME TO THE GAME!"
treasure_position = random.randint(1, 4)

print("****************************")
print(f"*** {welcome_message} ***")
print("****************************")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4
goa = goa_kosong.copy()

goa[treasure_position - 1] = "[0]"

nama_user = input("Masukkan nama kamu: ")
print(f'''Halo {nama_user}, Coba perhatikan goa di bawah ini!
{goa_kosong}
''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa yang ada harta karun? [1 / 2 / 3 / 4]: "))

confirm_user = input(f"Apakah kamu yakin bahwa harta karun ada di goa nomor {pilihan_user}? [y / n]: ") 

if confirm_user == "y":
    if pilihan_user == treasure_position:
        print(f"{goa} \nSelamat {nama_user}, Kamu berhasil menemukan harta karun! \ndi goa nomor {pilihan_user} adalah goa yang tepat!")
    else:
        print(f"{goa} \nMaaf, harta karun tidak berada di goa ini. \nHarta karun ada di goa nomor {treasure_position}")
elif confirm_user == "n":
    print("Oke, silahkan coba lagi lain waktu!")
    exit()
else:
    print("Input tidak valid!")
    exit()