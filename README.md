# Simulazione Chinook TdP

Progetto base per allenamento su database **Chinook**, strutturato come i temi d'esame TdP recenti in Python.

## Avvio

1. Apri la cartella in PyCharm.
2. Crea/usa un virtual environment.
3. Installa i requisiti:

```bash
pip install -r Requirements.txt
```

4. Controlla `database/connector.cnf` e verifica che il nome del database sia corretto, ad esempio `chinook` oppure `Chinook`, in base a come lo hai importato in MySQL/MariaDB.
5. Avvia:

```bash
python main.py
```

## Cosa è già pronto

- View completa con dropdown, textfield, bottoni e area risultati.
- Controller con i metodi essenziali già dichiarati ma vuoti.
- Model con struttura base del grafo e metodi da completare.
- DAO con metodi SQL da completare.
- Classe `Artist` già pronta.
- `DB_connect.py` e `connector.cnf` già predisposti.

## Cosa devi completare tu

- Query in `DAO.py`.
- Costruzione grafo in `model.py`.
- Validazione input e stampa output in `controller.py`.
- Eventuale riempimento del dropdown artisti dopo la creazione del grafo.

La traccia completa è in `TRACCIA_ESAME.md`.
