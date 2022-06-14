print('Pilih Menu Escrim di bawah ini')

escrime = ['Es Kiko      : 2000','Es koki      : 1500','Es Capuccino : 1000']
for es in escrime:
    print(es)


biaya = int(input('bayar berapa :'))


if biaya >= 2000:
    print('anda boleh beli Es kiko ')
elif biaya >= 1500:
    print('Anda boleh beli Es koki')
elif biaya >= 1000:
    print('Anda boleh beli Es capuccino')
else:
        print('uang anda tidak cukup buat beli eskrim')
    