# Anti-Atak | Made by m2_zm

> **m2_zm 2023-2025 © MIT**

## Özellikler
- `servisatk.exe`işlemini sonlandırıp atak'ı geçici devre dışı bırakma.

## Kullanım
1. Gerekli modülleri yükleyin:
   ```powershell
   pip install psutil win10toast plyer
   ```
2. Programı çalıştırın:
   ```powershell
   python anti_atak.py
   ```
3. .exe olarak derleyin:
   ```powershell
   .\.venv\Scripts\pyinstaller.exe --onefile --console --name anti_atak anti_atak.py --hidden-import psutil --hidden-import win10toast --hidden-import plyer --hidden-import plyer.platforms.win.notification
   ```
   Çıktı: `dist/anti_atak.exe`

4. anti-atak'ı bir usb'ye atınız.

5. akıllı tahta'yı açıp giriş yapın sonra usb'yi takın.

6. akıllı tahta Windows 10 ise yeni masaüstü açıp usb içinden anti-atak'ı açın. eğerki Windows 8.1 ise sağ kısımdan sol kısma kaydırıp ara kısmına tıklayın. usb label'inizi girip anti-atak'ın dosya yolunu yazın ve açın. bir süre sonra atak gidecek ve masaüstü gelecektir.

Örnek Yol: E:\anti_atak.exe = (E: Sizin USB Bellek Label'inizdir.)


## Dikkat
- Program explorer.exe'yi yeniden başlatır ve bazı işlemleri sonlandırır. 

## Lisans
MIT
