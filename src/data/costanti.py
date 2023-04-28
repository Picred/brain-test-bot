"""Most used constants"""
START_TXT = "Benvenuto al Brain Test Quiz! Puoi metterti alla prova scegliendo una /categoria e una /difficolta\nPuoi vedere le tue informazioni con /info e, dopo aver completato le operazioni preliminari, puoi iniziare il /quiz."

LIVELLO = 'livello'

CATEGORIA = 'categoria'

PUNTEGGIO = 'punteggio'

DOMANDA_CORRENTE = 'domanda_corrente'

ESEMPIO_DATA = [
    {
        "testo": "Questa è una domanda di prova",
        'risposte': [
            {
                "testo_risposta": "Risposta 1", "corretta": True
            },
            {
                "testo_risposta": "Risposta 2", "corretta": False
            },
            {
                "testo_risposta": "Risposta 3", "corretta": False
            },
            {
                "testo_risposta": "Risposta 4", "corretta": False
            }
        ]
    }
]

ESEMPIO_COMMENTO = {
    "Logica": [
        {
            "0 punti": "commento1",
            "3 punti": "commento2",
            "5 punti": "commento3"
        }
    ]
}
