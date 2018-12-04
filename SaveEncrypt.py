# -*- coding: UTF-8 -*-
# 存档明文为标准json
# 存档加密方式为用"key"与存档数据逐位异或后再base64编码
# # 本程序将修改过后的json明文(ChangededSave.txt)加密成原始存档格式(EncryptedSave.txt)
import base64

ChangededSave = open("ChangededSave.txt")
EncryptedSave = open("EncryptedSave.txt", "wb+")
str1 = ChangededSave.read()
ChangededSave.close()
DataLenth = len(str1)  # 加密
KeyString = 'key'  # 存档默认的加密字为key
KeyLenth = len(KeyString)
i = 0
str3 = ''
while i < DataLenth:
    str3 += chr(ord(str1[i]) ^ ord(KeyString[i % KeyLenth]))  # 字符串按位异或
    i = i + 1
str2 = base64.b64encode(str3.encode('utf-8'))  # 再base64编码
print(str2)
EncryptedSave.write(str2)
EncryptedSave.close()
