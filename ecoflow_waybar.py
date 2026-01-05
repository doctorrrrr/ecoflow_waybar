import os
import hashlib
import hmac
import time
import secrets
import requests
import json
from pathlib import Path

# Спробуємо завантажити ключі з оточення
# Для локального тестування можна використовувати python-dotenv
ACCESS_KEY = os.getenv("ECOFLOW_ACCESS_KEY")
SECRET_KEY = os.getenv("ECOFLOW_SECRET_KEY")
SN = os.getenv("ECOFLOW_SN")

class EcoFlowMonitor:
    def __init__(self):
        self.url = "https://api-e.ecoflow.com/iot-open/sign/device/quota/all"

    def get_signature(self, params_str, nonce, timestamp):
        str_to_sign = f"{params_str}&accessKey={ACCESS_KEY}&nonce={nonce}&timestamp={timestamp}"
        return hmac.new(
            SECRET_KEY.encode(), 
            str_to_sign.encode(), 
            hashlib.sha256
        ).hexdigest()

    def fetch_data(self):
        if not all([ACCESS_KEY, SECRET_KEY, SN]):
            return {"text": "󱊤 Env Err", "class": "error", "tooltip": "Missing API Keys"}

        nonce = str(secrets.randbelow(900000) + 100000)
        timestamp = str(int(time.time() * 1000))
        params_str = f"sn={SN}"
        
        headers = {
            "accessKey": ACCESS_KEY,
            "nonce": nonce,
            "timestamp": timestamp,
            "sign": self.get_signature(params_str, nonce, timestamp)
        }

        try:
            res = requests.get(self.url, headers=headers, params={"sn": SN}, timeout=10)
            res.raise_for_status()
            data = res.json().get("data", {})
            
            soc = int(float(data.get("cmsBattSoc", data.get("soc", 0))))
            pv = int(float(data.get("powGetPvSum", 0)))
            load = int(float(data.get("powGetSysLoad", 0)))

            css_class = "normal"
            if soc < 20: css_class = "warning"
            if soc < 10: css_class = "critical"

            return {
                "text": f"󱊦 {soc}% ☀️ {pv}W 🏠 {load}W",
                "tooltip": f"EcoFlow Status\nBattery: {soc}%\nSolar: {pv}W\nLoad: {load}W",
                "class": css_class,
                "percentage": soc
            }
        except Exception as e:
            return {"text": "󱊤 Error", "class": "error", "tooltip": str(e)}

if __name__ == "__main__":
    monitor = EcoFlowMonitor()
    print(json.dumps(monitor.fetch_data()))
