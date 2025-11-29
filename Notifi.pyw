import json
import time
from winotify import Notification
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "Tugas.json")
ICON_FILE = os.path.join(BASE_DIR, "LMS.ico")

def kirim_notifikasi():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        tasks = data.get("tasks", [])
        pending = [t for t in tasks if not t.get("completed", False)]
        jumlah_tugas = len(pending)

        msg = f"Ada {jumlah_tugas} tugas yang belum selesai."

        toast = Notification(
            app_id="Kerjain Tugas dulu wok",
            title="Tugas Belum Selesai",
            msg=msg,
            icon=ICON_FILE,
            duration="long"
        )
        toast.add_actions(label="Buka Dashboard", launch="http://127.0.0.1:5500/no.html")
        toast.show()
    except Exception as e:
        with open(os.path.join(BASE_DIR, "error.log"), "a", encoding="utf-8") as log:
            log.write(str(e) + "\n")

kirim_notifikasi()

# Lalu loop setiap 20 menit
while True:
    time.sleep(1200) 
    kirim_notifikasi()
