# ANTI - A.T.A.K (Akıllı Tahta Akıllı Kontrol)  | Remake by m2_zm

> **m2_zm 2024-2025 © MIT**

## Özellikler
- `servisatk.exe` işlemini sonlandırıp atak'ı geçici devre dışı bırakmak için bir proje.

## Kullanım
1. Gerekli modülleri yükleyin:
   ```powershell
   pip install psutil win10toast plyer
   ```
2. .exe olarak derleyin:
   ```powershell
   .\.venv\Scripts\pyinstaller.exe --onefile --console --name anti_atak anti_atak.py --hidden-import psutil --hidden-import win10toast --hidden-import plyer --hidden-import plyer.platforms.win.notification
   ```
3. Anti-atak'ı bir usb'ye atınız.

4. Akıllı tahta'yı açıp kullanıcı giriş'i yapın sonra usb'yi tahtaya takın.

5. Akıllı tahta Windows 10 ise yeni masaüstü açıp usb içinden anti-atak'ı açın. eğerki Windows 8.1 ise sağ kısımdan sol kısma kaydırıp ara kısmına tıklayın. usb label'inizi girip anti-atak'ın dosya yolunu yazın ve açın. bir süre sonra atak gidecek ve masaüstü gelecektir. Örnek Yazılacak Yol: E:\anti_atak.exe = (E: Sizin USB Bellek Label'inizdir.)

## TESTLER

Proje Faz-2 Tahtalarda Denendi (Windows 8.1 ve Windows 10)
Pardus Yüklü Tahtalarda Olmayacaktır Diye Umuyorum. Tabi Onlarda A.T.A.K Var İse XD
(Yerli İşletim Sistem'i Dedikde Güzel Yapılmış)


## UYARI

Yakalanırsanız Ben Sorumlu Değilim Gencolar.

## Yapımcılar

Ana Geliştirici: m2_zm
Anti-Atak Fikir Sahibi: Syo

## Lisans
MIT

