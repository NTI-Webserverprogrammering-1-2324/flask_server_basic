
# Flask Server: Basic 🚀

Detta repo ger en översikt över hur man sätter upp en enkel Flask-server genom att följa en steg-för-steg-guide från början. För en djupare dykning, se notebook-filen `Flask_Server_Intro`.

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
1. **Importera Flask-klassen**: Ett kritiskt steg för att skapa en Flask-webbapplikation.
    ```python
    from flask import Flask
    ```

2. **Skapa en Flask-instans**: Här skapar vi en Flask-instans, kallad `app`.
    ```python
    app = Flask(__name__)
    ```

3. **Definiera en route och funktion**: En central del av Flask är dess route-koncept.
    ```python
    @app.route("/")
    def hello():
        return "Hello World!"
    ```

4. **Starta servern**: Använd följande kod för att starta servern och sätta din Flask-app i drift.
    ```python
    if __name__ == "__main__":
        app.run(debug=True, port=3000)
    ```

## Kontakt 📬
För ytterligare information eller frågor, vänligen kontakta: **KaahinAtNTI**.
