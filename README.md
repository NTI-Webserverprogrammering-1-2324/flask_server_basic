# Flask Server: Basic 🚀

Detta repo ger en översikt över hur man sätter upp en enkel Flask-server genom att följa en steg-för-steg-guide från början. För en djupare insikt, se notebook-filen `Flask_Server_Intro`.

## Innehållsförteckning 📖
- [Introduktion](#introduktion)
- [Klienten vs Servern](#klienten-vs-servern)
- [Steg-för-Steg-guide](#steg-för-steg-guide)
- [Kontakt](#kontakt)

## Introduktion 🌐
I vår kurs "Webserverprogrammering 1" kommer vi ständigt att stöta på två centrala aktörer: **klienten** och **servern**. Flask är ett av de mest populära ramverken för att skapa webbapplikationer och backend-API:er med Python. Tack vare dess enkelhet och användarvänlighet har vi valt att fokusera på Flask i denna kurs.

## Klienten vs Servern 🔄
- **Klienten**: Klienten, ofta en **webbläsare**, skickar förfrågningar till en server och väntar tålmodigt på ett svar, redo att presentera informationen för användaren.
  
- **Servern**: Servern tar emot förfrågningar, behandlar dem och skickar tillbaka lämpligt innehåll. All denna kommunikation sker via **HTTP** (HyperText Transfer Protocol).

🍴 Tänk dig att du (klienten) besöker en restaurang (servern). Du frågar efter en specifik rätt från deras meny (applikationen), och restaurangen förbereder och serverar den åt dig.

## Steg-för-Steg-guide 📝
- **Importera Flask-klassen**: Ett kritiskt steg för att skapa en Flask-webbapplikation.
    ```python
    from flask import Flask
    ```

- **Skapa en Flask-instans**: Här skapar vi en Flask-instans, kallad `app`.
    ```python
    app = Flask(__name__)
    ```

- **Definiera en route och funktion**: En central del av Flask är dess route-koncept.
    ```python
    @app.route("/")
    def hello():
        return "Hello World!"
    ```

- **Aktivering av Flask-appen**: Denna kodsnutt ser till att servern startar när scriptet körs direkt från terminalen, vilket sätter Flask-applikationen i drift.
    ```python
    if __name__ == "__main__":
        app.run(debug=True, port=3000)
    ```

## Kör igång Flask-servern 🚀
- **Installera Flask**: Om ni inte redan har installerat Flask kan ni enkelt göra det med pip:
   ```
   pip install Flask
   ```

- **Starta servern**: När ni har installerat Flask, kan ni starta servern med följande kommando:
   ```
   python app.py
   ```

   När servern är igång bör ni se ett meddelande som talar om att den körs på adressen `http://127.0.0.1:3000/`.

- **Öppna i webbläsaren**: Besök `http://127.0.0.1:3000/` i er webbläsare för att se er Flask-applikation live!

## Kontakt 📬
För ytterligare information eller frågor, vänligen kontakta: **KaahinAtNTI**.
