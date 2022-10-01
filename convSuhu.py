print("\n APLIKASI KONVERSI SUHU \n")

# Fungsi aplikasi
def startApp():
    cek = int(input("Masukan nomor untuk memilih jenis suhu: \n 1. Celcius\n 2. Reamur\n 3. Kelvin\n 4. Fahrenheit\n 5. Keluar\n\n"))
    if cek == 1:
        Celcius()
    elif cek == 2:
        Reamur()
    elif cek == 3:
        Kelvin()
    elif cek == 4:
        Fahrenheit()
    elif cek == 5:
        exit()
    else:
        print("Maaf pilihan anda di luar nalar\n")

# Konversi dari celcius
def Celcius():
    c = float(input("\nMasukan suhu dalam Celcius: "))
    print("Suhu Celcius: " + str(c))
    
    # Reamur
    r = 4/5 * c
    print("Suhu Reamur: " + str(r))

    # Kelvin
    k = c + 273
    print("Suhu Kelvin: " + str(k))

    #Fahrenheit
    f = 9/5 * c + 32
    print("Suhu Fahrenheit: " + str(f) + "\n")

    # Untuk menjalankan kembali aplikasi
    startApp()

# Konversi dari reamur
def Reamur():
    r = float(input("\nMasukan suhu dalam Reamur: "))
    print("Suhu Reamur: " + str(r))

    # Celcius
    c = 5/4 * r
    print("Suhu Celcius: " + str(c))

    # Kelvin
    k = c + 273
    print("Suhu Kelvin: " + str(k))

    #Fahrenheit
    f = 9/4 * r + 32
    print("Suhu Fahrenheit: " + str(f) + "\n")

    # Untuk menjalankan kembali aplikasi
    startApp()

# Konversi dari kelvin
def Kelvin():
    k = float(input("\nMasukan suhu dalam Kelvin: "))
    print("Suhu Kelvin: " + str(k))

    # Celcius
    c = k - 273
    print("Suhu Celcius: " + str(c))
    
    # Reamur
    r = 4/5 * c
    print("Suhu Reamur: " + str(r))

    #Fahrenheit
    f = 9/5 * c + 32
    print("Suhu Fahrenheit: " + str(f) + "\n")
    
    # Untuk menjalankan kembali aplikasi
    startApp()

# Konversi dari fahrenheit
def Fahrenheit():
    f = float(input("\nMasukan suhu dalam Fahrenheit: "))
    print("Suhu Fahrenheit: " + str(f))
    
    #Celcius
    c = 5/9 * (f - 32)
    print("Suhu Celcius: " + str(c))

    # Reamur
    r = 4/9 * (f - 32)
    print("Suhu Reamur: " + str(r))

    # Kelvin
    k = c + 273
    print("Suhu Kelvin: " + str(k) + "\n")

    # Untuk menjalankan kembali aplikasi
    startApp()

# fungsi exit
def exit():
    print("Terimakasih!")

# Mulai aplikasi
startApp()

