# Currency Stock Crypto Backend 📊💰

## 📖 Projekt: Mobilní aplikace pro kurzy měn, akcií a kryptoměn

### **Popis**
Tato aplikace umožňuje sledování aktuálních i historických kurzů měn, akcií a kryptoměn. 
Je navržena tak, aby běžela buď na starším hardware prostřednictvím **Termux**, nebo na moderních zařízeních s podporou **Dockeru**. Díky optimalizaci nabízí rychlý výkon, zabezpečení a moderní uživatelské rozhraní.

---

## 🛠 Technologie

### **Frontend** 🌐
- **React Native**:
  - 📈 Grafy: `React Native Chart Kit` nebo `Victory Charts`.
  - 🌐 Detekce připojení: `NetInfo`.
  - 🔒 Bezpečné ukládání API klíčů: `Secure Storage`.
  - 🚀 Automatické aktualizace aplikace: `Expo OTA`.
  - 📱 Detekce OS a verze: `react-native-device-info`.
- **pnpm**: Rychlá a efektivní správa balíčků.

### **Backend** ⚙️
- **Python**:
  - 🛠 Framework: `Sanic` (asynchronní API).
  - 💾 Databáze a cache: `Dragonfly`.
  - ⚡ Zrychlení běhu Python kódu: `PyPy`.
  - 🧹 Izolace závislostí: `venv`.
  - 📊 Knihovny pro zpracování dat:
    - `yfinance` (akciové kurzy).
    - `ccxt` (kryptoměnové burzy).
    - `forex-python` (směnné kurzy).
    - `matplotlib` a `plotly` (vizualizace dat).
- **CI/CD**:
  - 🤖 Automatizace buildů pomocí `GitHub Actions`.
  - 🧪 Testování a sestavení pro Termux a Docker.

---

## ✨ Hlavní funkce
1. **Zobrazení kurzů**:
   - 📈 Data aktualizovaná každou minutu.
   - 📊 Sledování vybraných akcií, měn a kryptoměn.
2. **Grafy**:
   - 🖼 Lokálně vykreslované jednoduché grafy.
   - 🌐 Komplexní grafy generované na backendu.
3. **Offline režim**:
   - 🗄 Uchovávání posledních dat v `Dragonfly`.
   - 🕒 Informace o poslední aktualizaci dat.
4. **Zabezpečení**:
   - 🔒 API klíče uložené v `Secure Storage`.
   - 🛡 Šifrovaná komunikace přes HTTPS.

---

## 📂 Struktura projektu

```plaintext
project/
├── frontend/
│   ├── App.js                 # Hlavní React Native soubor
│   ├── components/            # Komponenty pro grafy a přehledy
│   │   ├── Chart.js           # Komponenta pro zobrazení grafů
│   │   └── DataList.js        # Přehled sledovaných dat
│   ├── services/              # Služby pro aplikaci
│   │   ├── api.js             # API volání na backend
│   │   ├── secureStorage.js   # Práce se Secure Storage
│   │   ├── deviceInfo.js      # Zjištění OS a verze zařízení pomocí react-native-device-info
│   ├── TermuxRedirect.js      # Přesměrování na Termux instalaci
│   ├── DockerFlow.js          # Spuštění Docker varianty
│   ├── assets/                # Ikony, obrázky
│   ├── package.json           # Konfigurace projektu
│   └── pnpm-lock.yaml         # Zamknuté verze závislostí
├── backend/
│   ├── app/
│   │   ├── routes.py          # API endpointy
│   │   ├── services/          # Služby pro zpracování dat
│   │   │   ├── termux_service.py # Specifické služby pro Termux
│   │   │   ├── docker_service.py # Specifické služby pro Docker
│   │   │   ├── yfinance_service.py
│   │   │   ├── ccxt_service.py
│   │   │   ├── forex_service.py
│   │   │   └── graph_service.py
│   │   ├── db.py              # Připojení k Dragonfly
│   │   └── scheduler.py       # Plánování úloh
│   ├── termux_install.sh      # Skript pro Termux instalaci
│   ├── Dockerfile             # Docker konfigurace pro backend
│   ├── requirements.txt       # Závislosti backendu
│   └── main.py                # Hlavní soubor backendu
├── dragonfly/
│   ├── dragonfly.conf         # Konfigurace Dragonfly
│   ├── init_cluster.sh        # Skript pro inicializaci clusteru
├── ci/
│   ├── github-actions/
│   │   ├── build-docker.yml   # CI pipeline pro Docker verzi
│   │   ├── build-termux.yml   # CI pipeline pro Termux verzi
│   │   └── deploy.yml         # Nasazení na Google Play
├── templates/
│   ├── CreativeTim/           # Šablony z Creative Tim
│   ├── Themeforest/           # Šablony z Themeforest
└── README.md                  # Dokumentace projektu
```

---

## 🚀 Instalace a spuštění

### **Frontend**
📦 Nainstalujte závislosti:
```bash
pnpm install
```
🚀 Spusťte Expo server:
```bash
expo start
```

---

## **Backend**

📦 Nainstalujte Python závislosti:
```bash
pip install --no-cache-dir -r requirements.txt
```
🛠 Spusťte backend:
```bash
python main.py
```

---

## **Databáze**

🗄 Spusťte Dragonfly:
```bash
dragonfly --config dragonfly.conf
```

---

## 🧹 Optimalizace a doporučení

### **Velikost aplikace**
- Typická velikost aplikace je pod **50 MB** díky optimalizaci (`pnpm prune`).
- Docker image backendu optimalizován na méně než **200 MB**.

### **Výkon**
- **Dragonfly** efektivně spravuje paměť (limitujte cache na 100 MB).
- **PyPy** zrychluje běh backendového kódu.

### **Kompatibilita**
- Testováno na **Android 8.0+** a **iOS 12+**.
- Ověřte správnou konfiguraci `Secure Storage`:
  - iOS: Použijte **CocoaPods**.
  - Android: Nastavte oprávnění v `AndroidManifest.xml`.

---

## 💡 Doporučení pro vylepšení

- 🔍 **Testování**:
  - Testujte aplikaci na starších verzích Androidu a iOS.
- 🛡 **Zabezpečení**:
  - Omezte přístup k API na nezbytné endpointy.
  - Šifrujte citlivá data na backendu.
- 📏 **Optimalizace velikosti**:
  - Minimalizujte závislosti a používejte dynamické načítání dat.
- 🎨 **Uživatelský zážitek**:
  - Použijte moderní šablony (např. Creative Tim nebo Themeforest).

---

## 📜 Licence

Tento projekt je chráněn licencí **MIT**. Podrobnosti najdete v souboru [LICENSE](./LICENSE).
