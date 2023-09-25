# Zadanie 1

Cieľom prvého zadania je implementovať vybraný heuristický algoritmus a aplikovať ho na riešenie ukážkového problému. Algoritmus implementujete v jazyku Python, štruktúra kódu je daná kostrou riešenia. Odovzaný projekt musí obsahovať minimálne nasledovné súbory:

1. Python skript s implementovaným algoritmom (súbor `algorithm.py`) - algoritmus implementujte podľa predpísanej štruktúry
2. textový súbor s ukážkovým príkladom - súbor obsahuje definíciu ukážkového problému podľa pravidiel určených pre konkrétny algoritmus; vytvorte vlastný príklad
3. Python skript s aplikáciou algoritmu (bod 1) na riešenie ukážkového problému (bod 2)

Vaša odovzdávka môže obsahovať aj ďalšie súbory podľa potreby (napríklad implementáciu algoritmu a spracovanie vstupu môžete rozdeliť do osobitných súborov). Na zadaní pracuje **každý sám**.

**Keďže odovzdané riešenie bude hodnotené automatizovanými testami, je dôležité, aby ste dodržali definovanú štruktúru a návratové hodnoty zadaných funkcií.**

## Odovzdanie a hodnotenie
Vypracované zadania môžete odovzdať do 8. týždňa. Po odovzdaní riešenia Vás čaká obhajoba, kde budete musieť reagovať na otázky týkajúce sa Vášho riešenia. Riešenie odovzdávate cez MS Teams kde bude vytvorený assignment pre tento účel. Za zadanie môžete získať maximálne 5 bodov a to nasledovne:

1. algoritmus - 5 bodov
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

[Ukážkové príklady a riešenia pomocou rôznych metód nájdete tu.](tsp_examples.zip)

Pre **problém obchodného cestujúceho** súbor `algorithm.py` musí obsahovať funkciu **find_path(file_path)** s jedným parametrom, ktorý predstavuje cestu k súboru, ktorý popisuje graf podľa určeného formátu. Funkcia má tri návratové hodnoty:

1. zoznam vrcholov v nájdenej trase, štartovacie mesto sa nachádza v zozname iba raz (teda pre graf so šiestimi mestami je to napr. zoznam: `[5, 3, 2, 1, 4, 6]`);
2. celková cena nájdenej trasy ako číslo;
2. zoznam medzivýsledkov, kde každý prvok tohto zoznamu je zoznam reprezentujúci čiastočnú trasu, posledný prvok je výsledok rovnaký prvej návratovej hodnote (pre príklad vyššie to môže byť: `[[5], [5, 1], [5, 3, 1], [5, 3, 1, 4], [5, 3, 2, 1, 4], [5, 3, 2, 1, 4, 6]]`).

Ak v súbore s hranami grafu chýba niektoré číslo, znamená to, že uzol s daným číslom neexistuje. Počet vrcholov grafu je daný počtom unikátnych hodnôt uzlov v zozname hrán.

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

Problém budete riešiť vybraným algoritmom z nasledujúceho zoznamu:

* 2.1. Largest Degree First
* 2.2. paralelné farbenie grafu
* 2.3. sekvenčné farbenie grafu

[Ukážkové príklady a riešenia pomocou rôznych metód nájdete tu.](coloring_examples.zip)

Pre **farbenie grafov** súbor `algorithm.py` musí obsahovať funkciu **color_graph(file_path)** s jedným parametrom, ktorý predstavuje cestu k súboru, ktorý popisuje graf podľa určeného formátu. Funkcia má dve návratové hodnoty:

1. zoznam farieb jednotlivých vrcholov (čiže pre graf s 8 vrcholmi to bude zoznam 8 čísel);
2. zoznam medzivýsledkov (pre graf s 8 vrcholmi to bude zoznam medzivýsledkov po jednotlivých iteráciách, pričom každý prvok je zoznam určujúci farbu vrcholov, pre nezafarbené uzly používajte číslo 0).

Ak v súbore s hranami grafu chýba niektoré číslo, znamená to, že daný uzol nemá suseda. Počet uzlov v grafe je daný najvyšším číslom uzlu zo zoznamu hrán.
