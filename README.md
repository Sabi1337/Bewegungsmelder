# Bewegungserkennung mit Flask und OpenCV

## 🔍 Über das Projekt

Dieses Projekt ist eine Webanwendung zur Bewegungserkennung mit einer Kamera. Es nutzt **Flask**, **OpenCV** und **YOLO**, um Bewegungen zu erkennen und Personen zu detektieren. Zusätzlich werden Telegram-Benachrichtigungen gesendet, wenn eine Bewegung erkannt wird.

## 👩‍💻 Features

- Live-Video-Stream der Kamera 🎥
- Bewegungserkennung mit OpenCV 🚶
- Personenerkennung mit YOLO 🤖
- Telegram-Benachrichtigungen bei erkannter Bewegung 📢
- Aufnahmefunktion für Videos 🎤
- Wechsel zwischen verschiedenen Kameras 🎬 (noch nicht perfekt)
- **Konfigurierbare Einstellungen über `config.ini`** ⚙️
- **Ngrok-Unterstützung für externen Zugriff** 🌍
- Zukünftig: Login-System und eigene Telegram-Bot-Unterstützung

## 🛠️ Voraussetzungen

Damit das Projekt funktioniert, benötigst du:

- **Python 3.8+**
- **Flask**
- **OpenCV** (`opencv-python`)
- **YOLO Gewichtsdateien** (`yolov4.weights`, `yolov4.cfg`, `coco.names`)
- **Telegram Bot** (für Benachrichtigungen, siehe unten)
- **Ngrok** (für externen Zugriff)

## 🛠️ Installation

1. **Repository klonen:**

   ```bash
   git clone https://github.com/dein-benutzername/bewegungserkennung.git
   cd bewegungserkennung
   ```

2. **Virtuelle Umgebung erstellen und aktivieren:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Abhängigkeiten installieren:**

   ```bash
   pip install -r requirements.txt
   ```

4. **YOLO-Dateien in das `yolo` Verzeichnis legen** (falls nicht vorhanden, herunterladen)

5. **Konfigurationsdatei `config.ini` anlegen:**

   Erstelle eine Datei `config.ini` im Hauptverzeichnis und füge folgende Inhalte hinzu:

   ```ini
   [Telegram]
   BOT_TOKEN = dein_token
   CHAT_ID = deine_chat_id

   [MotionDetection]
   MIN_AREA = 8000
   BLUR_SIZE = 25,25
   THRESHOLD = 30

   [Ngrok]
   AUTHTOKEN = dein_ngrok_token
   ```

   - **Telegram-Bot einrichten:**
     - Erstelle einen Bot mit [BotFather](https://t.me/BotFather)
     - Chat-ID ermitteln: Schicke deinem Bot eine Nachricht und rufe `https://api.telegram.org/botDEIN_TOKEN/getUpdates` auf
   
   - **Ngrok einrichten:**
     - Erstelle ein Konto auf [Ngrok](https://ngrok.com/)
     - Installiere Ngrok und führe folgenden Befehl aus:
       ```bash
       ngrok authtoken DEIN_NGROK_AUTHTOKEN
       ngrok http 5000
       ```

6. **Anwendung starten:**

   ```bash
   python app.py
   ```

## 🌎 Nutzung

- **Webinterface:** Rufe `http://127.0.0.1:5000/` im Browser auf
- **Kamera wechseln:** (noch nicht perfekt) Über das Webinterface eine andere Kamera auswählen
- **Aufnahme starten/stoppen:** Knopf im Webinterface nutzen
- **Einstellungen anpassen:** `config.ini` bearbeiten
- **Externen Zugriff nutzen:** Die von Ngrok generierte URL verwenden

## 🔧 To-Do / Zukünftige Features

- 🔒 Login-System für mehr Sicherheit
- 📲 Mehr Flexibilität bei Telegram-Bots
- 🎬 Bessere Kamera-Wechsel-Funktion
- 🌀 Performance-Optimierung

## 👤 Autor

Projekt von **Osman Serkan Sahin** 🚀

Falls du Feedback hast, erstelle ein Issue oder mach einen Pull Request! 💪

