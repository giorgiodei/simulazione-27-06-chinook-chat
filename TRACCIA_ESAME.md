# Simulazione d'esame TdP - Database Chinook

## Contesto

Si consideri il database **Chinook**. L'applicazione deve permettere di analizzare le vendite musicali tramite un grafo costruito sugli artisti.

La struttura del progetto è già predisposta secondo lo schema tipico dei temi d'esame TdP in Python:

- `main.py`
- `UI/view.py`
- `UI/controller.py`
- `model/model.py`
- `database/DAO.py`
- `database/DB_connect.py`

Il codice iniziale deve avviarsi correttamente. La logica di `Controller`, `Model` e `DAO` è volutamente lasciata da completare.

---

# Punto 1 - Costruzione del grafo

## 1.a - Popolamento della UI

All'avvio dell'applicazione, popolare due menu a tendina:

1. un menu con tutti i generi musicali presenti nella tabella `Genre`;
2. un menu con tutti i Paesi presenti tra i clienti nella tabella `Customer`.

La UI deve inoltre permettere all'utente di inserire una soglia numerica `S`, rappresentante la spesa minima complessiva associata a un artista.

---

## 1.b - Creazione del grafo

Alla pressione del pulsante **Crea grafo**, costruire un grafo **non orientato**.

I vertici del grafo sono gli artisti che soddisfano tutte le seguenti condizioni:

- hanno almeno una traccia appartenente al genere selezionato;
- hanno venduto almeno una traccia a clienti del Paese selezionato;
- la somma degli importi delle righe di fattura associate alle loro tracce è maggiore o uguale alla soglia `S` inserita dall'utente.

Formalmente, per ogni artista si considera il totale:

`SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity)`

calcolato solo sulle vendite relative al genere e al Paese selezionati.

---

## 1.c - Creazione degli archi

Inserire un arco tra due artisti distinti `A` e `B` se esiste almeno un cliente che ha acquistato almeno una traccia di entrambi gli artisti, sempre limitatamente al genere e al Paese selezionati.

Il peso dell'arco è pari al numero di clienti distinti che hanno acquistato tracce di entrambi gli artisti.

Il grafo deve quindi contenere:

- nodi = artisti filtrati;
- archi = coppie di artisti con almeno un cliente in comune;
- peso = numero di clienti comuni.

---

## 1.d - Output richiesto

Dopo la costruzione del grafo, visualizzare:

1. numero di nodi;
2. numero di archi;
3. numero di componenti connesse;
4. dimensione della componente connessa più grande;
5. i 5 archi con peso maggiore, stampando:
   - nome artista 1;
   - nome artista 2;
   - peso dell'arco.

Al termine della costruzione, popolare il menu a tendina del Punto 2 con tutti gli artisti presenti nel grafo.

---

# Punto 2 - Analisi su un artista

## 2.a - Analisi componente

L'utente seleziona un artista `A` tra quelli presenti nel grafo.

Alla pressione del pulsante **Analisi componente**, stampare:

1. la dimensione della componente connessa contenente `A`;
2. il grado pesato di `A`, cioè la somma dei pesi degli archi incidenti su `A`;
3. l'artista della stessa componente con grado pesato massimo.

---

## 2.b - Ricerca percorso migliore

L'utente inserisce un intero `K`.

Alla pressione del pulsante **Trova percorso migliore**, trovare il percorso semplice migliore che:

- parte dall'artista selezionato `A`;
- contiene al massimo `K` archi;
- non ripete mai lo stesso artista;
- massimizza la somma dei pesi degli archi attraversati.

In caso di parità di peso totale, preferire il percorso con più archi.

Stampare:

1. il peso totale del percorso;
2. il numero di archi del percorso;
3. la sequenza ordinata degli artisti attraversati.

---

# Suggerimento operativo

Una possibile impostazione, coerente con il modo classico di risolvere questi temi, è:

1. `View` crea dropdown, textfield e bottoni;
2. `Controller` legge i valori dalla view, valida gli input e chiama il model;
3. `Model` costruisce il grafo e gestisce NetworkX;
4. `DAO` contiene solo query SQL e restituisce dati semplici o oggetti model;
5. `DB_connect` gestisce la connessione al database.

La traccia è pensata per allenare:

- dropdown da query;
- filtro con due parametri;
- grafo non orientato;
- peso calcolato via query;
- componenti connesse;
- ordinamento archi;
- visita ricorsiva/backtracking su percorso semplice.
