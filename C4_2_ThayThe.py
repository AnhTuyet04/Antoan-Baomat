def mhThayThe(plaintext, k):
    ciphertext = ""
    for i in  plaintext:
        if i.isalpha():  # Chỉ mã hóa nếu ký tự là chữ cái (A-Z hoặc a-z).
            base = ord('A') if i.isupper() else ord('a')
            p = ord(i) - base   # chuyển sang 0..25
            c = (p + k) % 26    # đảm bảo kết quả quay vòng trong 26 chữ cái.
            ciphertext += chr(c + base)
        else:
            ciphertext += i  # ký tự khác giữ nguyên
    return ciphertext

if __name__ == "__main__": 
    plaintext = input("Nhập văn bản gốc cần mã hóa (ví dụ: TenCuaBan): ")
    k = int(input("Nhập secret key cho việc mã hóa (ví dụ: STT): "))
    ciphertext = mhThayThe(plaintext, k)
    
    print(f'''
    Plaintext - dữ liệu ban đầu: {plaintext}
    Key: {k}
    Ciphertext - kết quả sau khi được mã hóa: {ciphertext}\n''')

# ord(ch): chuyển ký tự → mã ASCII (số nguyên)
# chr(num): chuyển mã ASCII (số nguyên) → ký tự
