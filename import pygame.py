import requests
from bs4 import BeautifulSoup

# 📌 Liste der Restaurant-Websites
restaurant_websites = {
    "Royal M": "https://royalm.sk/denne-menu/",
    "La Cucaracha Pečovská": "https://pecovska.lacucaracha.sk/denne-menu-2/",
    "Spirit Prešov": "https://www.spiritpo.sk/spirit.php?page=obedoveMenu"
}

# 📌 Slowakische Menü-Schlüsselwörter
menu_keywords = ["Denné menu", "Obedové menu", "Dnes na obed", "Špeciálne menu"]

def scrape_menu(name, url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Falls Fehler, stoppe den Scraper
        soup = BeautifulSoup(response.text, "html.parser")

        # 🔍 Versuche, das Menü zu finden
        menu = []
        for tag in soup.find_all(["p", "div", "span", "h2"]):  
            text = tag.get_text().strip()
            if any(keyword in text for keyword in menu_keywords):  
                menu.append(text)

        # Falls kein Menü gefunden wurde, speichere die gesamte Seite zur Analyse
        if not menu:
            with open(f"{name}_raw.html", "w", encoding="utf-8") as file:
                file.write(soup.prettify())
            return f"❌ Žiadne menu sa nenašlo. (Stránka uložená ako {name}_raw.html)"

        return "\n".join(menu)

    except Exception as e:
        return f"❌ Chyba pri načítaní stránky: {e}"

# 📌 Durchsuche alle Restaurant-Websites
all_menus = []
for name, website in restaurant_websites.items():
    print(f"🔍 Hľadám menu pre {name} ({website})...")
    menu_text = scrape_menu(name, website)
    all_menus.append(f"🍽️ {name} ({website}):\n{menu_text}")

# 📌 Zeige die Ergebnisse an
final_text = "\n\n".join(all_menus)
print(final_text)

# 📌 Speichere die Menüs in eine Datei
with open("denne_menu_websites.txt", "w", encoding="utf-8") as file:
    file.write(final_text)

print("✅ Všetky menu boli uložené: denne_menu_websites.txt")
