p = 17
q = 23
e = 5
n = p*q
phi = (p-1)*(q-1)

# Hàm tính UCLN theo Euclid
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
# Hàm tìm nghịch đảo modular (d sao cho d*e ≡ 1 mod phi_n)
def ngdao(e, phi):
    for d in range(1,phi):
        if (d*e) % phi == 1: return d
    return None

# Kiểm tra gcd(e, phi_n)
if gcd(e, phi) != 1:    raise ValueError("e và phi(n) không nguyên tố cùng nhau!")

d = ngdao(e, phi) 
P = input("\nNhập thông điệp cần mã hóa (ví dụ: TenCuaBan): ")

print(f"p = {p}, q = {q}, n = {n}, phi = {phi}, e = {e}, d = {d}")
P_number = [ord(ch) for ch in P] # Chuyển từng ký tự thành số (theo mã ASCII)
C = [pow(m, e, n) for m in P_number] # C = pow(m,e,n) = (M^e) mod n

print(f"\nThông điệp dạng số (mã ASCII): \n \t{P_number}")
print(f"Bản mã: \n \t{C}")

# Giải mã để kiểm tra: M = (C^d) mod n
M_decrypted = [pow(c, d, n) for c in C]
P_decrypted = ''.join([chr(m) for m in M_decrypted])
print("Giải mã:", P_decrypted)
