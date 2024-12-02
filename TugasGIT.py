data_panen = {
    'lokasi1':{
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2':{
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3':{
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
      }
    },
    'lokasi4':{
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
      }
    },
    'lokasi5':{
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
      }
    }
}

def panen (list):
    print("No.1")
    [print(f"Lokasi Panen {value['nama_lokasi'] } \nHasil Panen Tahun ini:\nPadi {value['hasil_panen']['padi']}\njagung {value['hasil_panen']['jagung']}\nKedelai {value['hasil_panen']['kedelai']}{'\n'}")for value in list.values()]
    print('No 2')
    [print(f"Lokasi Panen {value ['nama_lokasi']}\nHasil Panen: \nJagung {value['hasil_panen']['jagung']}{'\n'}")for key,value in list.items() if key == 'lokasi2']
    print('No 3')
    [print(f"Nama Lokasi {value['nama_lokasi']}{'\n'}")for key,value in list.items() if key == 'lokasi3']

    #No 4
    padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
    padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
    padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
    padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
    padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
    kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
    kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
    kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
    kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
    kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

    print('No 5')
    jumlah_padi = padi_lokasi1 + padi_lokasi2 + padi_lokasi3 + padi_lokasi4 + padi_lokasi5
    jumlah_kedelai = kedelai_lokasi1 + kedelai_lokasi2 + kedelai_lokasi3 + kedelai_lokasi4 + kedelai_lokasi5
    print("\nJumlah Total Panen Padi: ",jumlah_padi)
    print("Jumlah Total Panen Kedelai: ",jumlah_kedelai)  
    print('\n')

    print("No 6")
    [print(f"Lokasi {key} memerlukan perhatian khusus") if value['hasil_panen']['padi'] > 1300 or value['hasil_panen']['jagung'] > 800 else print(f"Lokasi {key} dalam kondisi baik ") for key, value in list.items()]



panen(data_panen)
print('1')
print('2')