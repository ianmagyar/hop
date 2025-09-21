# Zadanie 2
V druhom zadaní aplikujete teoretické poznatky o optimalizácii pri riešení konkrétneho optimalizačného problému. Zadanie vypracúvate v štvročlenných tímoch, pričom k dispozícii budete mať ukážkové dáta a formát z ktorého máte vychádzať pri načítavaní údajov. Takisto budete mať popísanú očakávanú štruktúru výstupu vášho riešenia (výsledok optimalizácie teda uložíte do súboru). Špecifikácia úlohy je v niektorých prípadoch vágnejšia, a dáva vám možnosť vlastnej interpretácie. V prípade nejasností sa obráťte na vyučujúceho.

Vypracované zadanie sa skladá z nasledujúcich častí:

1. Analýza problému - Popísanú úlohu potrebujete formálne analyzovať, identifikovať typ optimalizačného problému, ktorý potrebujete vyriešiť, ako aj navrhnúť niekoľko možných riešení. Súčasťou analýzy musí byť špecifikácia úlohy, komponentov, z čoho sa bude skladať kandidát, aké sú podmienky pri optimalizácii a ako sa definujú kritériá a kvalita riešenia (ak je to aplikovateľné).
2. Návrh modelu problému - na základe analýzy navrhnite programovú reprezentáciu problému. Krátko popíšte, ako budete reprezentovať jednotlivé komponenty, kandidátov, a ako implementujete kriteriálnu funkciu alebo kontrolu spĺňania podmienok.
3. Implementácia riešenia - programová implementácia riešenia, pričom potrebujete vyriešiť načítanie dát, vytvorenie programovej reprezentácie úlohy, implementáciu vhodného optimalizačného algoritmu, reprezentáciu možných riešení a ukladanie výsledku. Vaše riešenie musí byť všeobecne aplikovateľné na inštancie problému, ktoré sú definované špecifikovanou formou, nestačí, ak riešenie bude fungovať iba pre ukážkový príklad.
4. Technická dokumentácia vášho riešenia - musí obsahovať body 1 a 2, a popis programovej implementácie (môže byť okomentovaný kód alebo textová dokumentácia riešenia). Súčasťou dokumentácie musí byť návod na nastavenie prostredia pre spustenie vášho riešenia (potrebné programové nástroje, knižnice, frameworky, atď.) ako aj návod na prácu s riešením.

Vašu odovzdávku môžete rozšíriť. Programovú časť môžete implementovať v ľubovoľnom jazyku.

## Odovzdanie a hodnotenie
Vypracované riešenie odovzdáte v dvoch fázach. Krátky report s analýzou problému a návrhom modelu (body 1 a 2) odovzdáte najneskôr v 7. týždni (do 9. 11.). Táto odovzdávka slúži na odhalenie možných nepresností vo vašom pochopení úlohy.

Finálne riešenie odovzdávate do konca 11. týždňa (do 7. 12.), následne vaše riešenie potrebujete obhájiť v 12. alebo 13. týždni semestra. Časy obhajob budú upresnené v priebehu semestra.

Riešenie odovzdávate cez MS Teams kde bude vytvorený assignment pre tento účel (odovzdáva iba jeden študent za tím). Za zadanie môžete získať maximálne 20 bodov a to nasledovne:

1. analýza problému a návrh riešenia - 7 bodov
2. implementácia riešenia - 7 bodov
3. efektivita riešenia (miera optimalizácie) - 3 body
4. obhajoba riešenia - 3 body

## Úlohy
*TBA*

<!--
1. [Úloha 1](#task1)
2. [Úloha 2](#task2)
3. [Úloha 3](#task3)
4. [Úloha 4](#task4)
5. [Úloha 5](#task5)
6. [Úloha 6](#task6)

### Úloha 1 <a name="task1"></a>
Členovia záhradkárskeho spolku sa rozhodli, že v letných mesiacoch budú strážiť úrodu a techniku na ich záhradkách stálou službou, pričom v službe bude stále jeden člen spolku na 24-hodinovej službe, a k nemu sa pridajú dvaja na každú noc. Záhradkárska osada má tvar jednej dlhej cesty so záhradkami na oboch stranách, číslovanie záhradok začnite od vchodu na ľubovoľnej strane, v číslovaní pokračujeme na tejto strane až do konca cesty, a následne sa vrátime k vchodu (najväčšie číslo záhradky teda bude oproti 1).

Pomôžte záhradkárskemu spolku navrhnúť službu po dobu 16 týždňov. K dispozícii máte zoznam preferenčných dní služby každého člena ([ukážkový príklad nájdete tu](samples/a2v1.txt)). V tomto súbore každý riadok obsahuje zoznam dní, v ktorých by mal člen najradšej službu (1 - pondelok, 2 - utorok, atď.). Čísla sú oddelené jednou medzerou a za posledným číslom hneď nasleduje znak pre nový riadok.

Pri vytvorení rozpisu dbajte na to, aby každý člen mal približne rovnaký počet 24-hodinových a nočných služieb (maximálny dovolený rozdiel je 1, počet ľudí bude taký, aby umožnil takéto rozdelenie). Okrem preferenčných dní berte do úvahy aj pokrytie v rámci zahrádkárskej osady - každý člen, ktorý má službu vie efektívne strážiť svoju záhradku, 5 záhradok v oboch stranách, aj na protiľahlej strane cesty. Optimalizovať teda chcete spokojnosť členov s dňami, v ktoré slúžia, ako aj zabezpečiť čo najväčšie pokrytie záhradok počas služby.

Na výstupe vygenerujte `.txt` súbor, v ktorom každý riadok obsahuje tri čísla - poradové číslo človeka, ktorý má v daný deň službu. Prvý z nich je člen na dennej službe, ďalší dvaja sú na nočnej. Každý riadok reprezentuje jeden deň, pričom prvý riadok bude považovaný za prvý pondelok. Číslovanie členov spolku začnite od 1, jednotlivé čísla oddeľte jednou medzerou a na konci riadku má byť znak pre nový riadok bez medzery.

### Úloha 2 <a name="task2"></a>
Pomôžte katedre počítačovej vedy univerzity navrhnúť úväzky, teda rozdeliť, ktorý vyučujúci aké predmety bude vyučovať v nadchádzajúcom školskom roku. K dispozícii máte `csv` súbor ([ukážkový príklad nájdete tu](samples/a2v2.csv)), ktorý obsahuje riadky v nasledujúcom formáte (pozor na bodkočiarky a čiarky):

```
CS497;5;assist.prof. Trevor Edwards,prof. Jack Thompson,assoc.prof. Theo Gardner, Veronica Hill
```

Prvá hodnota v každom riadku vyjadruje kód predmetu, nasleduje počet cvičení, ktoré treba zabezpečiť, ako aj zoznam zamestnancov, ktorí sú kvalifikovaní na výučbu tohto predmetu. Preferencie pritom majú profesori (*prof.*), docenti (*assoc.prof.*) a odborní asistenti (*assist.prof.*). V niektorých riadkoch nájdete aj doktorandov, iba v takom prípade, ak ich školiteľ preferuje daný predmet. Doktorandov by ste mali prideľovať primárne na takéto predmety, ale ak je potrebné, môžu vyučovať ľubovoľný predmet. Okrem cvičení musíte myslieť aj na prednášky, pre jednoduchosť ale každý predmet má iba jednu rozvrhovú jednotku pre prednášky. Napríklad pre vyššie uvedený predmet musíte nájsť vyučujúcich pre jednu prednášku a 5 cvičení.

Vašou úlohou je navrhnúť úväzky zamestnancom, pričom profesor môže učiť maximálne 5 rozvrhových jednotiek, docent ich môže mať 8, odborný asistent 11 a doktorand 4 (musia byť iba cvičenia). Môžete si byť istí, že počet hodín je možné zabezpečiť v rámci hodinovej kapacity vyučujúcich. Každý predmet má aspoň jedného kvalifikovaného vyučujúceho. Ak na predmete máte ako cvičiacich dvoch profesorov alebo docentov, tí musia zdieľať aj prednášku, v takomto prípade sa prednáška ráta do ich úväzkov iba polovične (0,5). Traja profesori alebo docenti na jednom predmete nesmú byť.

Na výstupe vygenerujte `.csv` súbor, v ktorom každý riadok reprezentuje rozdelenie úväzkov pre konkrétny predmet vo forme:

`CS497;prof. Jack Thompson/assist.prof. Trevor Edwards,assist.prof. Trevor Edwards,assist.prof. Trevor Edwards,Veronica Hill,Veronica Hill,Veronica Hill`

Prvá hodnota je naďalej kód predmetu, a po bodkočiarke nasleduje zoznam vyučujúcich jednotlivých rozvrhových jednotiek. Prvá z nich je prednáška, v tomto prípade vidíte, že prednáška je zabezpečená dvomi vyučujúcimi (mená oddeľte `/`, ak máte iba jedného prednášajúceho, samozrejme lomku netreba použiť). Potom nasleduje čiarkou oddelený zoznam cvičiacich - dve cvičenia zabezpečuje doc. Trevor Edwards, tri jeho doktorandka Veronica Hill.

### Úloha 3 <a name="task3"></a>
Firma, ktorá predáva súčiastky do chladiacich zariadení, musí tieto súčiastky pred dodaním vypáliť v špeciálnych peciach. Proces prebieha tak, že súčiastky sú položené vedľa seba na plech. Aby nedošlo k poškodeniu súčiastok, musia byť medzi ne umiestnené izolačné bloky z tepelne odolného materiálu. Tieto bloky majú jednotne šírku 5 cm.

Pomôžte firme optimalizovať proces tepelnej úpravy pomocou lepšieho umiestnenia súčiastok na plechy tak, aby ste maximalizovali priestor. Viete pritom, že každý plech má rozmery *5m x 5m*, a izolačný materiál musí byť okolo súčiastky z každej strany (aj keď je súčiastka na okraji plechu). Ak dve súčiastky sú vedľa seba, musí medzi nimi byť *10cm* izolačného materiálu (2 bloky). Súčiastky musia ležať, teda musia byť položené najväčšou stranou. V súčasnosti firma dáva súčiastky na plech úplne jednoducho - súčiastky umiestňuje podľa poradia, ako prišli objednávky (najprv teda dajú súčiastky z prvej objednávky, potom z druhej, atď.). Ak sa ďalšia súčiastka nezmestí na plech, dajú ju na ďalší plech a priestor ostáva nevyužitý (aj keby sa tam zmestila súčiastka z inej objednávky).

Na vstupe máte `csv` súbor ([ukážkový príklad nájdete tu](samples/a2v3.csv)), ktorý obsahuje riadky popisujúce objednávky. Každý riadok má štruktúru:

```
MR-009,40x30x10,5,2024-09-16 00:26:41
```

kde prvá hodnota je názov súčiastky, potom nasledujú jej rozmery, počet objednaných kusov a čas objednávky. Záznamy s rovnakým časom sú súčasťou jednej objednávky. Firma sa rozhodla, že plechy do pece pripraví dvakrát za deň: na základe objednávok od polnoci do obeda, a znova pre objednávky od obeda do polnoci. Na výstupe vygenerujte `.csv` súbor, ktorý bude obsahovať riadky so štruktúrou:

```
1,MR-009,2024-09-16 00:26:41,5,5
```

kde prvé číslo je číslo plechu (ak sa ďalšia súčiastka nezmestí na plech, inkrementujte túto hodnotu a začnite nový plech), potom nasleduje názov súčiastky (ak v objednávke máte 5 súčiastok, na výstupe budete mať 5 riadkov), čas objednávky súčiastky, a následne pozícia ľavého horného rohu (z pohľadu zhora) súčiastky na plechu (hodnoty sú uvedené v centimetroch). Ak ste spracovali všetky objednávky do obedu resp. do polnoci, číslovanie plechov začnite od 1. Efektivitu optimalizácie vyčíslite porovnaním využitého priestoru plechov v percentách oproti chronologického umiestneniu súčiastok na plech.

### Úloha 4 <a name="task4"></a>
Napíšte modelové riešenie pre optimalizáciu objednávky surovín do reštaurácie. K dispozícii máte informácie o rôznych surovinách, ktoré potrebujete kúpiť a potrebné množstvo (v rôznych jednotkách, ale ceny sa uvádzajú štandardizovane). Hľadáte pritom najlepšiu kombináciu objednania minimálneho potrebného množstva týchto surovín z ponuky niekoľkých dodávateľov, pričom do úvahy beriete aj plat zamestnanca, ktorý bude tento tovar preberať a čas, ktorý prejde medzi prvou a poslednou dodávkou.

Na vstupe máte `json` súbor ([ukážkový príklad nájdete tu](samples/a2v4.json)), ktorý popisuje ponuku jednotlivých dodávateľov, kde každý dodávateľ má vlastnú tabuľku, napríklad:

```
{
    "time": 12,
    "offer": {
        "pasta": [[0.5, 0.69], [2, 2.69], [3, 4.19], [5, 6.99]],
        "salad": [[0.5, 1.39], [1, 2.69]],
        "beef": [[1, 7.79], [3, 22.99]]
    }
}
```

kde pod kľúčom `time` nájdete hodinu, kedy dodávajú tovar, a `offer` obsahuje dvojice kľúč-hodnota pre rôzne suroviny. Z informácií pre surovinu viete prečítať, v akom množstve danú surovinu ponúkajú a za akú cenu (napríklad vo vyššom príklade šalát môžete kúpiť v polkilovom a kilovom balení za 1,39 respektíve 2,69). Pri optimalizácii berte do úvahy okrem celkovej ceny objednávky aj čas, ktorý musíte čakať medzi prvou a poslednou dodávkou, keďže na prevzatie tovaru potrebujete zamestnať niekoho, kto by mohol vykonávať iné úlohy v tom istom čase. Plat tohto zamestnanca vám vyjde na 30 eur za každú hodinu, čiže keby ste istou kombinácou objednávok ušetrili 40 eur, ale posledná objednávka by prišla o 2 hodiny neskôr, takáto kombinácia je horšia ako pôvodná alternatíva (keďže na zamestnanca musíte vydať 60 eur navyše). Pri výplate berte do úvahy každú začatú hodinu, teda ak prvá dodávka príde o 6 a posledná o 10, celkovo ho musíte platiť za 5 hodín.

Ako ďalší vstup máte informácie o potrebnom množstve jednotlivých surovín (zadefinujte priamo v kóde). Túto informáciu uveďte ako dvojice kľúč-hodnota, napríklad:

```
{
    "flour": 12,
    "pasta": 6,
    "beef": 4
}
```

čo znamená, že musíte objednať aspoň 12 jednotiek múky, 6 jednotiek cestovín a 4 jednotky hovädzieho mäsa. Samozrejme, objednať si môžete aj viac. Pri optimalizácii môžete objednať maximálne od 3 dodávateľov, ale rovnakú surovinu môžete kúpiť od viacerých (napríklad ak niekto má menšie balenie za výhodnejšiu cenu).

Na výstupe vygenerujte `json` súbor, ktorý bude obsahovať informáciu o objednávke v nasledujúcej forme:

```
{
    0: {
        "flour": [[2, 5]]
    },
    1: {
        "eggs": [[1, 30], [1, 6]]
    },
    7: {
        "flour": [[1, 1]],
        "rice": [[2, 5], [1, 3]]
    } 
}
```

kde číselný kľúč vyjadruje index dodávateľa v zozname dodávateľov, a nasleduje zoznam surovín, ktoré od neho objednáte. Pre každú surovinu uveďte zoznam, kde budete mať množstvo a veľkosť objednaných balení. Napríklad od posledného dodávateľa v príklade vyššie objednáme 2 päťkilové balenia ryže a 1 trojkilové balenie.

### Úloha 5 <a name="task5"></a>
V tejto úlohe riadite úrad pre spracovanie rôznych žiadostí, a vašou úlohou je rozdeliť spracovanie žiadostí medzi vašimi zamestnancami tak, aby žiadosti boli spracované v čo najkratšom čase. Vyberáte z niekoľkých úradníkov, pričom nie každého musíte zavolať do práce, resp. nie každého musíte zamestnať na spracovanie žiadostí. Cieľom optimalizácie je teda alokovať pracovníkov tak, aby najpomalší z nich končil čo najskôr, pričom predpokladáte, že všetci začnú spracovávať alokované žiadosti v rovnakom čase, a pracujú nezávisle, teda nikdy nemusia čakať na iného kolegu.

Na vstupe máte `json` súbor ([ukážkový príklad nájdete tu](samples/a2v5.json)), ktorý popisuje preferovanú agendu jednotlivých úradníkov a ich rýchlosť pri spracovaní rôznych typov žiadostí, napríklad:

```
{
    "CLI-989": 4,
    "OPT-451": 4,
    "EBC-794": 2
}
```

kde kľúče sú názvy rôznych formulárov, ktoré má daný úradník spracovať a hodnota je čas potrebný na spracovanie daného typu formulára v minútach. Ak sa niektorý formulár nenachádza medzi kľúčmi daného úradníka, neznamená to, že ho nedokáže spracovať, len sa použije defaultný čas 5 minút. Pri alokácii môžete využiť aj skutočnosť, že ak úradník má po sebe spracovávať formuláre rovnakého typu, dokáže ešte viac zefektívniť proces, a to o 5% pri každom následnom spracovaní. Napríklad vyššie uvedený úradník by spracoval prvý formulár typu `CLI-989` za 4 minúty, ďalší za 3 minúty a 48 sekúnd (0,95 * 240s), tretí za 3 minúty a 36 sekúnd (0,9 * 240s), atď. Ak následne spracuje formulár iného typu (napríklad `EBC-794`), a potom zase má spracovávať formulár typu `CLI-989`, tak ten mu bude trvať zase 4 minúty. Maximálne zefektívnenie je na úrovni 50%, teda náš ukážkový úradník nikdy nebude spracovávať formuláre typu `CLI-989` za menej ako 2 minúty.

Ako ďalší vstup máte informácie o počte rôznych typov formulárov, ktoré majú byť spracované. Túto informáciu uveďte ako dvojice kľúč-hodnota priamo v kóde, napríklad:

```
{
    "CLI-989": 59,
    "OPT-451": 38,
    "IRV-843": 67
}
```

čo znamená, že musíte spracovať 59 formulárov typu `CLI-989`, 38 formulárov `OPT-451` a 67 formulárov `IRV-843`. Vždy používajte iba názvy formulárov, ktoré sú definované v príslušnom `.json` súbore pre úradníkov (možnosti načítajte zo súboru).

Na výstupe vygenerujte `csv` súbor, ktorý bude obsahovať informáciu o alokácii formulárov jednotlivým úradníkom v nasledovnej forme:

```
0,CLI-989,CLI-989,CLI-989,OPT-451,...
4,OPT-451,OPT-451,IRV-843,...
5,CLI-989,CLI-989,CLI-989,CLI-989,...
```

kde prvá hodnota je index úradníka v pôvodnom `.json` súbore (indexujeme od 0), a následne máte čiarkou oddelené konkrétne formuláre, ktoré má úradník spracovať. Na konci `.csv` súboru nechajte jeden riadok prázdny, ak niektorého úradníka nepovoláte, preňho nepridajte riadok (v príklade vyššie sú to úradníci 1, 2, 3). Pri optimalizácii okrem času berte do úvahy aj plat úradníkov - za každú začatú hodinu musíte zaplatiť 30 eur každému úradníkovi. Samozrejme, ak jeden úradník končí za menej ako 2 hodiny a druhý bude pracovať cez 3 hodiny, tak prvému zaplatíte dve hodiny a druhému štyri.

### Úloha 6 <a name="task6"></a>
Vašou úlohou je optimalizovať alokáciu výpočtových procesov, pričom rôznym úlohám musíte priradiť zariadenie a čas vykonania úlohy. Máte teda zoznam zariadení, a zoznam úloh, pričom pre každú úlohu máte definovaný názov úlohy, trvanie úlohy (v minútach), zoznam zariadení, na ktorých môže byť daná úloha vykonaná, ako aj zoznam prerekvizít, teda úloh, ktoré musia byť dokončené pred tým, než sa spustí daná úloha.

Na vstupe máte `json` súbor ([ukážkový príklad nájdete tu](samples/a2v6.json)), ktorý popisuje zadanie vo forme štruktúry s dvomi kľúčmi. Prvý kľúč je `devices`, ktorý obsahuje zoznam zariadení (všetky názvy sú reťazce). Následne máte zoznam úloh pod kľúčom `tasks`, pričom každá úloha je popísaná nasledovne:

```
{
    "name": "KPK-128",
    "duration": 46,
    "devices": ["IU-26"],
    "prerequisites": ["MOT-900", "LJU-255", "TTZ-191"]
}
```

teda úlohu `KPK-128` môžete spustiť iba na zariadení `IU-26`, kde bude bežať 46 minút, ale pred samotným spustením musíte dokončiť vykonávanie úloh `MOT-900`, `LJU-255` a `TTZ-191`.

Na výstupe vygeneruje `.csv` súbor, kde pre každú úlohu budete mať jeden riadok vo forme:

```
KPK-128,IU-26,342
```

kde prvá hodnota je názov úlohy, druhá hodnota je meno zariadenia, na ktorom sa spustí úloha, a tretia hodnota udáva časový okamih, v ktorom sa spustí riešenie úlohy. Táto hodnota je udávaná v minútach a ráta sa od začiatku spustenia prvej úlohy (prvá úloha sa spustí v čase 0). Na konci súboru nechajte jeden prázdny riadok.

Pri optimalizácii dbajte na to, aby ste poslednú úlohu dokončili čo najskôr. Samozrejme musíte dodržať všetky prerekvizity jednotlivých úloh, a nesmiete dopustiť, aby viaceré úlohy bežali súbežne na tom istom zariadení.
-->
