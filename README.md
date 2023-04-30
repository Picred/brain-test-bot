# Brain Test Bot
[![CodeFactor](https://www.codefactor.io/repository/github/picred/brain-test-bot/badge)](https://www.codefactor.io/repository/github/picred/brain-test-bot)

Brain Test Bot è un bot di Telegram che consente agli utenti di testare la loro intelligenza e le loro abilità cognitive attraverso una serie di quiz e rompicapi. Il bot presenta domande di diversi argomenti, tra cui:
- Grammatica
- Logica
- Matematica
- Cultura generale

Sono inoltre presenti 3 tipi di difficoltà, quali:
- Facile -> timer: 10s
- Intermedio -> timer: 7s
- Difficile -> timer: 5s
# Installazione
Per utilizzare Brain Test Bot, è necessario avere un account Telegram attivo. Dopo aver creato un nuovo bot Telegram tramite il BotFather, clona la repository e installa tutte le dipendenze necessarie utilizzando il seguente comando:

```shell
pip install -r requirements.txt
```

Una volta installate tutte le dipendenze, crea un file chiamato `token.txt` nella directory principale e aggiungi il tuo token di autenticazione del bot.

Infine, esegui il bot utilizzando il seguente comando:
```shell
python main.py
```

# Guida all'uso
Seguire i seguenti passaggi al fine di evitare errori:
1. Individuare la chat del proprio bot con l'aiuto di BotFather
2. Per iniziare è necessario avviare il bot con il comando `/start`
3. Successivamente si deve impostare la `/categoria` desiderata e quindi la `/difficolta` (_l'ordine di queste operazioni non è importante_)
    - _NB: Il tempo a disposizione per ogni domanda diminuisce man mano che la difficoltà viene incrementata._
4. Iniziare il quiz con il comando `/quiz`


# Contributi
Siamo sempre alla ricerca di contributi e miglioramenti per Brain Test Bot. Se vuoi contribuire al progetto, sentiti libero di creare/commentare una *pull request* o di dare un'occhiata oppure aprire una *issue* nella sezione *Issues*.

# Autori
Brain Test Bot è stato sviluppato da:
- [Picred](https://github.com/Picred)
- [Mattia Puglia](https://github.com/mattiapuglia)

# Struttura del progetto
```bash
├───.github
│   └───workflows # contiene i file per Github Actions
├───src
│   ├───data # contiene le costanti principali e i file delle domande del quiz
│   └───handlers # contiene tutte le funzioni usate
└───tests # contiene tutti i file per i test
```
