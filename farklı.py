from PIL import Image

def sarı_nokta_ekle(resim_yolu):
    # Resmi aç
    im = Image.open(resim_yolu)

    # Resmin boyutlarını al
    genişlik, yükseklik = im.size

    # Orta noktayı belirle
    orta_nokta = (genişlik // 2, yükseklik // 2)

    # Y ekseninin 1512'den başlayacağına göre bu noktayı ayarla
    orta_nokta = (orta_nokta[0], 1512)

    for x in range(genişlik):
        for y in range(orta_nokta[1], yükseklik):
            # Belirtilen pikselin rengini al
            renk = im.getpixel((x, y))

            # Eğer kırmızı aralıkta ise, sarı renk ile değiştir
            if renk[0] > 150 and renk[1] < 100 and renk[2] < 100:
                im.putpixel((x, y), (255, 255, 0))

    # Sonuç resmi kaydet
    im.save('yeni_resim.png')

# Fonksiyonu çağır
sarı_nokta_ekle('images/JPG8.jpg')
