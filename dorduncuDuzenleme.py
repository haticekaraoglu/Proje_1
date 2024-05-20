
# Word dosyasını aç
from docx import Document

# Yeni bir Word belgesi oluştur
doc = Document()

# Yeni bir tablo oluştur (satır sayısı + başlık satırı, sütun sayısı)
tablo = doc.add_table(rows=1, cols=2)

# Başlık satırını oluştur ve hücrelere başlıkları ekle
hdr_cells = tablo.rows[0].cells
hdr_cells[0].text = 'Renk'
hdr_cells[1].text = 'Açıklama'

# Yeni veriler
yeni_veriler = [
    ["MAVİ", "'mavi' kelimesi beklenen 71 kez geçti."],
    ["BEYAZ", "'beyaz' kelimesi beklenen 0 kez geçti."],
    ["TURUNCU", "'turuncu' kelimesi beklenen 15 kez geçti."],
    ["TURKUVAZ", "'turkuvaz' kelimesi beklenen 2 kez geçti."],
    ["SİYAH", "'siyah' kelimesi beklenen 0 kez geçti."],
    ["YESİL", "'yesil' kelimesi beklenen 0 kez geçti."],
    ["GRİ", "'gri' kelimesi beklenen 0 kez geçti."],
    ["PEMBE", "'pembe' kelimesi beklenen 0 kez geçti."],
    ["SARI", "'sari' kelimesi beklenen 0 kez geçti."],
    ["TANIMSIZ", "'tanımsız' kelimesi beklenen 0 kez geçti."]
]

# Verileri tabloya ekle
for renk, aciklama in yeni_veriler:
    satir_hucreler = tablo.add_row().cells
    satir_hucreler[0].text = renk
    satir_hucreler[1].text = aciklama

# Belgeyi kaydet
doc.save('yeni_tablo.docx')
