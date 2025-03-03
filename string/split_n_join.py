sentence = '''Tim Hukum KPK meminta penundaan sidang praperadilan jilid II Sekjen PDIP Hasto Kristiyanto terkait penetapan status tersangka. Kuasa hukum Hasto berharap penundaan itu bukan akal-akalan KPK untuk menyelesaikan berkas perkara.'''

sentence_split = sentence.split(' ')
short_sentence = ' '.join(sentence_split[:6])

print(short_sentence.lower())
print(short_sentence.upper())
print(short_sentence.capitalize())
print(short_sentence.replace("KPK","Komisi Pemberantasan Korupsi"))