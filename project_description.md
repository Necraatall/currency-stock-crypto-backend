# project_description.md
# Návrh projektu: Mobilní aplikace pro kurzy měn, akcií a kryptoměn

## Úvod
Aplikace umožňuje sledování aktuálních a historických kurzů měn, akcií a kryptoměn. Je navržena tak, aby běžela lokálně na mobilním zařízení, s podporou pro starší i moderní hardware. Podle typu zařízení a OS je rozhodováno, zda bude backend provozován v **Termux** nebo v prostředí **Docker**.

---

## Technologie

### **Frontend**
- **React Native**:
  - **React Native Chart Kit** nebo **Victory Charts** pro grafy.
  - **NetInfo**: Detekce připojení.
  - **Secure Storage**: Bezpečné ukládání API klíčů.
  - **Expo OTA aktualizace**: Automatické aktualizace aplikace.
  - **react-native-device-info**: Detekce operačního systému (iOS/Android) a verze.
- **pnpm**: Efektivní správa balíčků.

### **Backend**
- **Python**:
  - **Sanic**: Asynchronní framework pro API.
  - **Dragonfly**: Cache a databáze.
  - **PyPy**: Pro zrychlení běhu Python kódu.
  - **venv**: Virtuální prostředí pro izolaci závislostí.
- **Knihovny**:
  - `yfinance`: Akciové kurzy.
  - `ccxt`: Kryptoměnové burzy.
  - `forex-python`: Směnné kurzy.
  - `matplotlib` a `plotly`: Generování grafů.

### **Databáze**
- **Dragonfly**:
  - Rychlejší a efektivnější než Redis.
  - AOF (Append-Only File) pro trvalé ukládání dat.

### **CI/CD**
- **GitHub Actions**:
  - Automatizace buildů pro frontend i backend.
  - Pipeline pro sestavení a testování variant pro Termux a Docker.
  - Nasazení aplikace na Google Play.

---

## Funkce

1. **Zobrazení kurzů**:
   - Data aktualizovaná každou minutu.
   - Sledování vybraných akcií, měn a kryptoměn.
2. **Grafy**:
   - Jednoduché grafy vykreslované lokálně.
   - Složitější grafy generované na backendu.
3. **Offline režim**:
   - Uchovávání posledních dat v Dragonfly.
   - Informace o poslední aktualizaci dat.
4. **Zabezpečení**:
   - API klíče uložené v Secure Storage.
   - HTTPS komunikace mezi frontendem a backendem.

---

## Zjišťování hardwaru a OS

### Detekce zařízení pomocí `react-native-device-info`
- Zjištění operačního systému (iOS nebo Android) a jeho verze:
  ```javascript
  import DeviceInfo from 'react-native-device-info';

  export const getDeviceInfo = async () => {
    const osName = DeviceInfo.getSystemName(); // 'iOS' nebo 'Android'
    const osVersion = DeviceInfo.getSystemVersion(); // Např. '12.0.1' nebo '9'

    return { osName, osVersion };
  };

---

## Rozhodování mezi Termux a Docker

   - Na základě zjištěných informací se aplikace rozhodne:
       - Termux: Pro starší zařízení (např. Android < 8.0).
       - Docker: Pro modernější zařízení s vyššími zdroji.

---

## Struktura projektu

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

## Instalace a spuštění

### **Frontend**
1. Nainstaluj závislosti:
   ```bash
   pnpm install```
2. Spusť Expo server:
   ```bash
   expo start```

### **Backend**
1. Nainstaluj Python závislosti:
   ```bash
   pip install --no-cache-dir -r requirements.txt```
2. Spusť backend:
   ```bash
   python main.py```

### **Databáze**
1. Spusť Dragonfly:
   ```bash
   dragonfly --config dragonfly.conf```

---

## Optimalizace a doporučení

### Velikost aplikace
- Typická velikost pod **50 MB** díky optimalizaci (`pnpm prune`).
- Docker image backendu optimalizuj na méně než **200 MB**.

### Výkon
- **Dragonfly** efektivně spravuje paměť (limituj cache na 100 MB).
- **PyPy** zrychluje běh backendového kódu.

### Kompatibilita
- Testováno na **Android 8.0** a **iOS 12+**.
- Ujisti se, že **Secure Storage** je správně nakonfigurován:
  - Na iOS: Použij **CocoaPods**.
  - Na Android: Nastav oprávnění v `AndroidManifest.xml`.

### Zabezpečení
- API klíče jsou ukládány v **Secure Storage**.
- Šifrovaná komunikace probíhá přes **HTTPS**.

### Uživatelská zkušenost
- **Aktualizace na pozadí** pomocí Expo OTA.
- **Moderní vzhled** s využitím šablon z Creative Tim nebo Themeforest.

---

## Hodnocení

Tento projekt je optimalizovaný pro:

- **Rychlost a výkon**: PyPy a Dragonfly snižují zatížení zařízení.
- **Zabezpečení**: API klíče jsou chráněny Secure Storage, komunikace je šifrovaná.
- **Kompatibilitu**: Funguje na starších verzích Android a iOS.
- **Moderní design**: Připraveno pro přehledný a profesionální vzhled.

**Projekt je připraven k nasazení na Google Play.**

##############################################
############ HINTY
##############################################
pip install --no-cache-dir -r requirements.txt
##############################################
Riziko: Některé nativní knihovny (např. Secure Storage) mohou vyžadovat dodatečné nastavení na iOS (CocoaPods) nebo Android (permissions v AndroidManifest.xml).
Doporučení: Otestuj aplikaci na starších verzích Androidu (např. 8.0) a iOS (např. 12) pro zajištění zpětné kompatibility.
##############################################
React Native aplikace má tendenci být větší kvůli nativním modulům. Typická velikost je však pod 50 MB, což je přijatelné.
Doporučení: Minimalizuj závislosti v projektu (pnpm prune) a používej dynamické načítání dat, aby velikost aplikace zůstala nízká.
##############################################
Procesor:

    Multithreading Dragonfly využije moderní CPU efektivněji než Redis.

Doporučení:

    Udržuj trvalý dohled nad velikostí cache (např. limit 100 MB), aby se zabránilo přetížení paměti zařízení.
##############################################
Zkontroluj velikost Docker image backendu. Měla by být optimalizována na méně než 200 MB.
##############################################
Schopnost uživatele pracovat během instalace

    Expo OTA aktualizace:
        Pokud je Expo správně nakonfigurováno, uživatel může stahovat aktualizace na pozadí.
        Aplikace by neměla blokovat uživatelské akce při instalaci aktualizace.
##############################################
Seznam problémů a vylepšení

    Kompatibilita:
        Otestuj aplikaci na starších verzích Android a iOS.
        Ujisti se, že všechny knihovny (např. Secure Storage) jsou správně nakonfigurovány.

    Optimalizace výkonu:
        Omez velikost cache na backendu (Dragonfly).
        Použij PyPy a efektivní načítání dat pro backend.

    Velikost a doba instalace:
        Minimalizuj závislosti v React Native a Python.
        Optimalizuj Docker image backendu.

    Vzhled a uživatelská zkušenost:
        Přidej moderní šablonu pro React Native.
        Umožni uživateli pracovat během instalace nebo aktualizace aplikace.
##############################################
Celkové hodnocení: Projekt je dobře navržený a plní požadavky na rychlost, zabezpečení a multiplatformní kompatibilitu. Doporučuji:

    Otestovat kompatibilitu na starších zařízeních.
    Optimalizovat velikost a instalaci závislostí.
    Přidat profesionální vzhled pomocí šablon z Creative Tim nebo Themeforest.

Rizika a vylepšení

    Riziko: Secure Storage vyžaduje dodatečné nastavení.
        Řešení: Přidej detailní instrukce pro iOS a Android.
##############################################
    Riziko: Velikost aplikace může být velká.
        Řešení: Minimalizace závislostí a dynamické načítání dat.

    Vylepšení bezpečnosti:
        Omez přístup k API pouze na potřebné endpointy.
        Použij šifrování citlivých dat na backendu.

    Doporučení:
        Udržuj trvalý dohled nad velikostí cache (max. 100 MB).
        Zajisti optimalizaci Docker image backendu (méně než 200 MB).
##############################################
