import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)

#simulasi serangan MITM
#eve memiliki private key sendiri
e1 = random.randint(1, p-1)  # secret Eve untuk Alice
e2 = random.randint(1, p-1)  # secret Eve untuk Bob

#public key Eve yang akan disisipkan
E1 = pow(g, e1, p) # public key Eve untuk Alice
E2 = pow(g, e2, p) # public key Eve untuk Bob

print("\nEve mengganti public key!")
print("Public key Alice yang diterima Bob :", E1)
print("Public key Bob yang diterima Alice  :", E2)

#alice dan bob menghitung shared secret dengan public key palsu dari eve
shared_secret_A_eve = pow(E2, a, p)  # Alice menghitung
shared_secret_B_eve = pow(E1, b, p)  # Bob menghitung

#Eve dapat menghitung shared secret dengan private keynya sendiri
shared_secret_eve_A = pow(A, e1, p)  # shared secret antara Eve dan Alice
shared_secret_eve_B = pow(B, e2, p)  # shared secret antara Eve dan Bob

#Hasil akhir
print("\n=== Kunci yang dihasilkan ===")
print("kunci alice :", shared_secret_A_eve)
print("kunci bob   :", shared_secret_B_eve)

print("\n=== kunci yang eve tau ===")
print("kunci eve dengan alice :", shared_secret_eve_A)
print("kunci eve dengan bob   :", shared_secret_eve_B)