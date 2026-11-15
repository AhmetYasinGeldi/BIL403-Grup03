# KampüsEmanet

Kampüste bulunan eşyaların tek bir yerde kaydedilmesini ve sahiplerine doğrulanarak teslim edilmesini sağlayan web uygulaması. BIL403 Yazılım Mühendisliği dönem projesi, Grup 03.

- **Öğrenci:** bulunan eşyaları kategori, yer ve tarihe göre arar, ayırt edici özelliği yazarak sahiplenme talebi gönderir ve talebinin durumunu izler.
- **Görevli:** bulunan eşyayı kaydeder, talepleri gizli ayırt edici detayla karşılaştırıp onaylar ya da reddeder, teslimi kaydeder.

## Teknoloji

Python 3.11+, Flask, SQLite (Flask-SQLAlchemy), Flask-Login, pytest, flake8.

## Kurulum

```bash
git clone https://github.com/AhmetYasinGeldi/BIL403-Grup03.git
cd BIL403-Grup03

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

`.env.example` dosyasını `.env` adıyla kopyalayın ve değerleri doldurun:

```bash
# Windows
copy .env.example .env
# macOS / Linux
cp .env.example .env
```

## Çalıştırma

```bash
python run.py
```

Uygulama http://127.0.0.1:5000 adresinde açılır.

## Testler ve statik analiz

```bash
pytest
flake8 app tests
```

## Klasör yapısı

```
app/            Uygulama kodu (Flask)
tests/          Otomatik testler (pytest)
docs/           Gereksinim ve plan belgesi, diyagramlar, sprint notları
```

## Süreç

- Ürün listesi: GitHub Issues (Zorunlu / Önemli / İsteğe bağlı etiketleri)
- Sprint panosu: [BIL403-Grup03 Sprint Panosu](https://github.com/users/AhmetYasinGeldi/projects/1)
- Sprint 1: 16–29 Kasım 2026 · Sprint 2: 30 Kasım – 13 Aralık 2026

Her hikaye ayrı bir dalda geliştirilir ve `main`'e testleri geçen bir pull request ile birleştirilir.

## Ekip

| Üye | GitHub | Rol |
| --- | --- | --- |
| Ahmet Yasin Geldi | AhmetYasinGeldi | Ürün sahibi, geliştirici |
| Hüseyin Melih Özbek | Huseyin-creator | Scrum Master, geliştirici |
| Mustafa Emin Çebi | mustafacebi | Geliştirici |
| Ömer Faruk Karasan | OmerFarukKolapsi | Geliştirici |

Uygulamadaki bütün örnek kayıtlar uydurma veridir; gerçek kişisel veri kullanılmaz (KVKK).
