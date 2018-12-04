# -*- coding: UTF-8 -*-
# 存档明文为标准json
# 存档加密方式为用"key"与存档数据逐位异或后再base64编码
# 本程序将原始存档(autosave.txt)解密成json明文(DecryptedSave.txt)
import base64

OriginSave = open("autosave.txt")
DecryptedSave = open("DecryptedSave.txt", "w")
str1 = OriginSave.read()
OriginSave.close()
str2 = base64.b64decode(str1)  # 先base64解码
DataLenth = len(str2)
KeyString = 'key'  # 存档默认的加密字为key
KeyLenth = len(KeyString)
i = 0
str3 = ''
while i < DataLenth:
    str3 += chr(str2[i] ^ ord(KeyString[i % KeyLenth]))  # 字符串按位异或,str2默认取出的是ascii编码
    i = i + 1
DecryptedSave.write(str3)
DecryptedSave.close()
