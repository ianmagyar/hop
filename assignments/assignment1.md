# Zadanie 1

Cieľom prvého zadania je implementovať vybraný heuristický algoritmus a aplikovať ho na riešenie ukážkového problému. Algoritmus implementujete v jazyku Python (po dohode s vyučujúcim je možné zmeniť programovací jazyk), štruktúra riešenia je na Vás, odovzaný projekt ale musí osbahovať minimálne nasledovné súbory:

1. Python skript s implementovaným algoritmom (súbor `.py`) - algoritmus môžete implementovať ako funkciu alebo ako triedu
2. textový súbor s ukážkovým príkladom - súbor bude obsahovať definíciu ukážkového problému podľa pravidiel určených pre konkrétny algoritmus
3. Python skript s aplikáciou algoritmu (bod 1) na riešenie ukážkového problému (bod 2)

Vaša odovzdávka môže obsahovať aj ďalšie súbory podľa potreby (napríklad implementáciu algoritmu a spracovanie vstupu môžete rozdeliť do osobitných súborov). Na zadaní pracuje **každý sám**.

## Odovzdanie a hodnotenie
Vypracované zadania môžete odovzdať a obhájiť od 9. týždňa do 11. týždňa. Súčasťou odovzdania je aj obhajoba, kde budete musieť reagovať na otázky týkajúce sa Vášho riešenia. Riešenie odovzdávate cez MS Teams kde je vytvorený assignment pre tento účel. Za zadanie môžete získať maximálne 5 bodov a to nasledovne:

1. algoritmus - 3 body
2. aplikácia algoritmu na riešenie problému - 1 bod (testuje sa aj s iným problémom ako ukážkový)
3. obhajoba - 1 bod

## Úlohy
### Variant 1 - Problém obchodného cestujúceho
* Vstupom je textový súbor, kde každý riadok predstavuje hranu medzi uzlami (mestami) v grafe a jej váhu (cenu) v tvare `číslo_uzla1 číslo_uzla2 váha`, napríklad

`1 2 0.8`

* Výstupom algoritmu je textový súbor obsahujúci celkovú cenu cesty v prvom riadku a postupnosť uzlov (miest) ako ich obchodný cestujúci navštívi v druhom riadku (uzly sú oddelené čiarkami):

```
13
1,4,3,2,...
```

Problém budete riešiť vybraným algoritmom z nasledujúceho zoznamu:

* 1.1. Nearest Neighbor
* 1.2. Nearest insertion of arbitrary city
* 1.3. Nearest insertion
* 1.4. Farthest insertion
* 1.5. Cheapest insertion

### Variant 2 - Problém farbenia grafov
* Vstupom je textový súbor, v ktorom každý riadok predstavuje hranu medzi uzlami v grafe v tvare `uzol1 uzol2`, napríklad:

```
1 2
1 4
2 3
3 4
```

* Výstupom algoritmu je textový súbor, v ktorom každý riadok predstavuje uzol a jemu priradenú farbu v tvare `uzol farba`; farby reprezentujete číslami 1 až n, napríklad:

```
1 1
2 2
3 1
4 2
```

* Počet farieb bude vstupným parametrom algoritmu.

Problém budete riešiť vybraným algoritmom z nasledujúceho zoznamu:

* 2.1. Largest Degree First
* 2.2. paralelné farbenie grafu
* 2.3. sekvenčné farbenie grafu

Pridelenú úlohu s hodnotením nájdete [v tomto dokumente](https://docs.google.com/spreadsheets/d/1xuz-1zpo0cCQ-jQopO5S2HLovNgknWJysYeFafeY4Kw/edit?usp=sharing).
