'''
说明：
Python中可以使用pycrypto库来实现对称加密算法的加密和解密。
以下是一个使用AES算法进行加密和解密的示例代码：
'''

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


# 加密函数
def encrypt(key, text):
    # 将密钥转换为16、24或32字节的二进制格式
    key = key.encode('utf-8')
    key = key + b'\0' * (16 - len(key))
    # 将明文进行补齐
    text = pad(text.encode('utf-8'), AES.block_size)
    # 创建AES加密器
    cipher = AES.new(key, AES.MODE_ECB)
    # 对明文进行加密
    encrypted = cipher.encrypt(text)
    # 将加密后的密文进行Base64编码
    return base64.b64encode(encrypted).decode('utf-8')



# 解密函数
def decrypt(key, ciphertext):
    # 将密钥转换为16、24或32字节的二进制格式
    key = key.encode('utf-8')
    key = key + b'\0' * (16 - len(key))
    # 对密文进行Base64解码
    ciphertext = base64.b64decode(ciphertext)
    # 创建AES解密器
    cipher = AES.new(key, AES.MODE_ECB)
    # 对密文进行解密
    decrypted = cipher.decrypt(ciphertext)
    # 对解密后的明文进行去除补齐符操作
    return unpad(decrypted, AES.block_size).decode('utf-8')



# ##使用加密、解密函数
# # 生成密钥（建议使用更复杂的密钥）
# key = 'my_secret_key'
#
# # 要加密的文本
# text = 'kangsz_lc'
#
# # 加密
# encrypted_text = encrypt(key, text)
# print('加密后的文本：', encrypted_text)

'''
# 生成的加密文本
ciphertext = "+NOU5idbtlX34Sjqe/3TdQ=="

# 解密（请注意，ECB模式不够安全，不建议在生产环境中使用）
decrypted_text = decrypt(key, ciphertext)
print('解密后的文本：', decrypted_text)
'''


'''
在上面的代码中，我们使用了ECB模式进行加密和解密，这是一种基本的加密模式，但不够安全。
在实际应用中，建议使用更加安全的加密模式，如CBC模式。
同时，密钥的长度应该大于等于16字节，否则会导致加密强度不足。
'''
