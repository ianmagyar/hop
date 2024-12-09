## Okruh 1
1. Popíšte pojmy: komponent, kandidát, priestor kandidátov.
2. Vysvetlite pojmy podmienky a kvalita riešenia. Pre aký typ problému sa definujú?
3. Aký je rozdiel medzi problémom, modelom, riešením a výsledkom?
4. Aký je postup pri použití heuristík a benchmarkovských problémov pri riešení problému?
5. Čo je to heuristika a čo je cieľom jej použitia?
6. Navrhnite riešenie ľubovoľného problému, a pomocou neho vysvetlite pojmy problém, komponenty, kandidát, priestor kandidátov.
7. Aký je rozdiel medzi problémom a inštanciou problému? Aký je rozdiel medzi kandidátom a riešením? Vysvetlite tieto pojmy.
8. Čo je to general problem solver? Ako sa dá využívať pri riešení problémov?
9. Uveďte príklad problému, kde sa definujú podmienky pre kandidáta, ďalší príklad kde sa definuje kvalita riešenia, a príklad kde sa definujú obe.
10. Popíšte štruktúru problému z pohľadu riešenia problému.

## Okruh 2
1. Popíšte farbenie grafov ako prototypový problém. Je to model ktorého typu problémov? Ako sa definuje inštancia problému a čo je úlohou? Aké sú typy problému farbenia grafov?
2. Popíšte problém splniteľnosti ako prototypový problém. Je to model ktorého typu problémov? Ako sa definuje inštancia problému a čo je úlohou? Aké sú typy problému splniteľnosti?
3. Popíšte problém obchodného cestujúceho ako prototypový problém. Je to model ktorého typu problémov? Ako sa definuje inštancia problému a čo je úlohou? Aké sú typy problému TSP?
4. Aký je rozdiel medzi numerickými a kombinatorickými problémami? Uveďte príklady pre oba typy problémov.
5. Čo je to rozhodovací problém a aké sú jeho varianty? Uveďte príklady.
6. Čo je to optimalizačný problém a aké sú jeho varianty? Uveďte príklady.
7. Čo je to kombinovaný problém? Čo charakterizuje riešenie kombinovaného problému?
8. Aké charakteristiky môže mať kandidát z pohľadu riešenia rozhodovacích a optimalizačných problémov?
9. Odvoďte veľkosť inštancie a veľkosť priestoru kandidátov pri probléme splniteľnosti pri úplnom, a parciálnom priradení.
10. Odvoďte veľkosť inštancie a veľkosť priestoru kandidátov pri probléme obchodného cestujúceho.
11. Odvoďte veľkosť inštancie a veľkosť priestoru kandidátov pri probléme farbenia grafov.

## Okruh 3
1. Aký je rozdiel medzi perturbačným a konštrukčným prehľadávaním? Ako sa dajú kombinovať tieto dve paradigmy?
2. Ako sa využíva jednotkový literál a orezávanie pri DPLL algoritme? Ako sa definuje ukončenie algoritmu?
3. Aká je základná štruktúra riešenia problému prehľadávaním? Popíšte jednotlivé kroky. V čom sa líšia jednotlivé algoritmy patriace do tejto skupiny algoritmov?
4. Aký je rozdiel medzi systematickým a lokálnym prehľadávaním kandidátov? Ako sa dajú kombinovať tieto dve paradigmy?
5. Krátko popíšte a vysvetlite výhody a nevýhody úplného a konštrukčného algoritmu prehľadávania. Na základe čoho vyberáme použitú paradigmu riešenia?
6. Aký je rozdiel medzi úplnými a neúplnými algoritmami prehľadávania? Aké sú ich výhody a nevýhody? Kedy sa používa ktorý z nich?
7. Popíšte kombinované paradigmy lokálne + perturbačné/konštrukčné. Ako fungujú a ako nájdu riešenie problému?
8. Popíšte kombinované paradigmy systematické + perturbačné/konštrukčné. Ako fungujú a ako nájdu riešenie problému?
9. Čo je to výberová heuristika a na čo sa používa v DPLL algoritme? Aké sú základné typy a ako fungujú?
10. Popíšte jednotlivé kroky DPLL algoritmu na základe pseudokódu:

```
Input: množina klauzúl Φ
Output: pravdivostná hodnota (splniteľnosť)

(I, Φ) ← UNIT-RESOLUTION(Φ)
if Φ = {}, return true
if {} ∊ Φ, return false
choose a literal L from Φ
if DPLL(Φ ∪ {{L}}) = true, return true
if DPLL(Φ ∪ {{¬L}}) = true, return true
return false
```

## Okruh 4
1. Čo je to okolie pri lokálnom prehľadávaní? Ako sa definuje? Uveďte príklady a ohraničenia pre každý typ definície.
2. Čo je to lokálne prehľadávanie, na čo sa používa a ako funguje? Ako sa definuje globálne riešenie pre rôzne typy problémov? Aký je rozdiel medzi globálnym a lokálnym riešením pri rôznych typoch problémov?
3. Popíšte definíciu okolia pre lokálne prehľadávanie na základe vzdialenosti. Uveďte príklady a popíšte, ako by sa dali používať pri rôznych inštanciách problému. Ako sa definuje funkcia vzdialenosti?
4. Popíšte definíciu okolia pre lokálne prehľadávanie na základe mapovania. Uveďte príklady a popíšte, ako by sa dali používať pri rôznych inštanciách problému. Ako sa dá používať mapovanie kandidátov pri prehľadávaní?
5. Čo je to graf okolia a čo vyjadruje? Vysvetlite vlastnosti symetria, stupeň vrcholu, ako aj regulárnosť, dostupnosť a priemer grafu.
6. Aké sú komponenty lokálneho prehľadávania? Vysvetlite ich rolu a uveďte príklady.
7. Pre aký typ problému sa používa nasledovná štruktúra lokálneho prehľadávania? Popíšte jednotlivé kroky.

```
input: π
output: s ∊ S |  ⃞
( s, m ) = init(π) 
while( not term( s, m ) )
	( s, m ) = step( s, m )
endwhile
if( valid(s) ) then
	return s
else
	return   ⃞
endif
```

8. Pre aký typ problému sa používa nasledovná štruktúra lokálneho prehľadávania? Popíšte jednotlivé kroky.

```
input: π
output: r ∊ S |  ⃞
( s, m ) = init(π)
r = s
while( not term( s, m ) )
	( s, m ) = step( s, m )
	if( f( s ) < f( r )  ) then
		r = s
	endif
endwhile
if( valid(r) ) then
	return r
else
	return   ⃞
endif
```

9. Čo je to prehľadávacia trajektória, od čoho závisí a čo nám povie o prehľadávaní? Uveďte a vysvetlite príklady neinformovanej stratégie pri prehľadávaní.
10. Nasledovný pseudokód popisuje lokálne prehľadávanie pre optimalizačný problém. Popíšte jednotlivé kroky, napíšte, či sa jedná o minimalizačnú alebo maximalizačnú úlohu, a vysvetlite, čo by sme potrebovali zmeniť pre riešenie druhého typu úlohy.

```
input: π
output: r ∊ S |  ⃞
( s, m ) = init(π)
r = s
while( not term( s, m ) )
	( s, m ) = step( s, m )
	if( f( s ) > f( r )  ) then
		r = s
	endif
endwhile
if( valid(r) ) then
	return r
else
	return   ⃞
endif
```

## Okruh 5
1. Čo je to ohodnocovacia funkcia a ako sa používa pri iteračnom vylepšovaní? Ako sa dá definovať pre rozhodovací a optimalizačný problém?
2. Aký je rozdiel medzi informovanou a neinformovanou stratégiou pri lokálnom prehľadávaní? Ako sú možné definície ukončovacej podmienky pre jednotlivé stratégie?
3. Aké podmienky musia platiť pre ohodnocovaciu funkciu pri iteračnom vylepšovaní v prípade rozhodovacieho a optimalizačného problému?
4. Poukážte na rozdiely medzi ohodnocovacou funkciou v prípade štandardnej a optimalizačnej podoby rozhodovacích problémov na príklade SAT a MAXSAT problému.
5. Popíšte a vysvetlite funkciu step v iteračnom vylepšovaní pre minimalizačnú podobu úlohy.
6. Ako sa definuje funkcia init pre iteračné vylepšovanie? Kedy končí iteračné vylepšovanie a aké to má dôsledky?
7. Vysvetlite jednotlivé kroky iteračného vylepšovania na pseudokóde:

```
input: π
output: s ∊ S |  ⃞
s = urp()
while( #I( s ) > 0 )
	s = select( I( s ) )
endwhile
if( valid( s ) ) then
	return s
else
	return  ⃞
endif
```

8. Aká je trajektória prehľadávania v prípade iteračného vylepšovania? Akého kandidáta nájde algoritmus v prípade jedného resp. viacerých lokálnych extrémov?
9. Čím je spôsobené uviaznutie v lokálnom optime pri iteračnom vylepšovaní? Ako to ovplyvňuje nájdenie riešenia?
10. Popíšte a vysvetlite funkciu step v iteračnom vylepšovaní pre maximalizačnú podobu úlohy.

## Okruh 6
1. Čím je spôsobené uviaznutie v lokálnom extréme pri iteračnom vylepšovaní? Ako pomôže akceptácia horšieho riešenia pri úniku z lokálneho optima? Uveďte príklad algoritmu pre akceptáciu horšieho riešenia.
2. Uveďte príklad pre zakázané lokálne prehľadávanie a krátko ho popíšte. Ako sa dá rozšíriť zakázané lokálne prehľadávanie pomocou ašpiračného kritéria a dlhodobej pamäte?
3. Ako pomôžu opakované reštarty pri úniku z lokálneho optima v iteračnom vylepšovaní? Vysvetlite, kedy a prečo môžeme používať tento prístup?
4. Ako pomôže použitie väčšieho okolia pri úniku z lokálneho optima v iteračnom vylepšovaní? Vysvetlite výhody a nevýhody tohto prístupu.
5. Uveďte základné typy pivotného pravidla pri výbere nasledujúceho kandidáta pre iteračné vylepšovanie.
6. V čom spočíva princíp prepínania okolí pri iteračnom vylepšovaní a ako funguje? Ako to funguje v algoritme VND? Kedy tento algoritmus končí?
7. Ako pomôže použitie dlhého kroku pri úniku z lokálneho optima v iteračnom vylepšovaní? Vysvetlite výhody a nevýhody tohto prístupu. Ako funguje generovanie kandidátov v Lin-Kernighan algoritme a kedy ukončíme proces generovania?
8. Krátko popíšte algoritmy randomizované a pravdepodobnostné iteračné zlepšovanie. Čo majú spoločné a v čom sa líšia? Ako zabraňujú uviaznutiu v lokálnom optime?
9. Čo je to dynamické lokálne prehľadávanie a ako zabraňuje uviaznutiu v lokálnom optime? Aké sú základné charakteristiky použitej stratégie? Ako sa aplikuje penalizácia pri dynamickom lokálnom prehľadávaní?
10. Uveďte základné prístupy úniku z lokálneho optima a jednou vetou ich popíšte.

## Okruh 7
1. Aký je rozdiel medzi hrami s nulovým resp. nenulovým súčtom?
2. Aký je rozdiel medzi kooperatívnymi a antagonistickými hrami?
3. Čo je to Nashova rovnováha a kedy je dosiahnutá?
4. Ako je definovaná a na čo slúži bodovacia funkcia pri algoritme Minimax.
5. Vysvetlite princíp fungovania Minimax algoritmu.
6. Ako funguje alfa-beta orezávanie v Minimax algoritme?
7. Uveďte a vysvetlite základný princíp interakcie medzi agentom a prostredím v učení posilňovaním.
8. Ako prebieha učenie v algoritmoch učenia posilňovaním?
9. Ako sa definuje kumulatívna odmena pre istý stav prostredia pri algoritmoch učenia posilňovaním?
10. Ako dokážeme nájsť optimálnu politiku pomocou algoritmov učenia posilňovaním?

## Okruh 8
1. Ako sa použije feromón pri optimalizácii mravčích kolónií?
2. Popíšte, ako by ste použili optimalizáciu mravčích kolónií pre riešenie problému obchodného cestujúceho.
3. Na čom je založené hľadanie najkratšej cesty pri optimalizácii mravčích kolónií?
4. Aké sú základné vlastnosti umelého mravca pre optimalizáciu mravčích kolónií?
5. Popíšte mravčí svet pri optimalizácii mravčích kolónií: model a jeho vlastnosti.
6. Vysvetlite ako sa vyberie smer pohybu pri optimalizácii mravčích kolónií.
7. Aký je rozdiel medzi statickou a dynamickou váhou pri optimalizácii mravčích kolónií, na čo sa používajú a ako sú definované?
8. Čo obsahuje pamäť umelého mravca pri optimalizácii mravčích kolónií a ako sa použije pri výbere smeru pohybu?
9. Na čo slúži odparovanie feromónu vo feromónovom hospodárstve pri optimalizácii mravčích kolónií? Ako sa definuje a kedy sa aplikuje?
10. Vysvetlite jednotlivé kroku optimalizácie mravčích kolónií na pseudokóde:

```
input: π, max
output: r ∊ S
r =   ⃞, g( r ) = ∞
i = 1
repeat
	initialize-ants()
	while ( not memory-full() )
		move-ants()
		update-memory()
	endwhile
	s = shortest-path()
	if ( g( s ) < g( r ) ) then
		r = s
	endif
	contributions()
	update()
	i = i + 1
until i > max
return r
```

## Okruh 9
1. Aký je rozdiel medzi chemotaxickým, reprodukčným a disperzným cyklom pri algoritme BFO?
2. Ako je definovaná reprodukcia a čo je jej účelom pri algoritme BFO?
3. Na riešenie akých problémov sa používa algoritmus BFO a ako vyzerá priestor kandidátov? Popíšte funkciu step pre tento algoritmus. 
4. Aký je typický priebeh priemernej kvality kandidátov pri algoritme BFO? Ako túto hodnotu ovplyvňujú jednotlivé cykly?
5. Ako sa definuje a využíva sociálne chovanie pri algoritme BFO?
6. Popíšte reprodukciu a disperziu pre algoritmus BFO. Na čo slúžia a ako sú implementované?
7. Ako sa pohybuje simulovaná baktéria v algoritme BFO? V ktorej časti algoritmu je pohyb riešený a aký má význam pre prehľadávanie?
8. V čom sa líši simulovaný pohyb baktérie od skutočného pohybu baktéri pri BFO? Ako sa to prejavuje a ako je to implementované v algoritme?
9. Využíva sa pamäť v algoritme BFO? Prečo je resp. nie je potrebná? Ak sa používa, tak čo uchováva a pri ktorom kroku algoritmu sa aktualizuje?
10. Ako sa určuje dĺžka pohybu baktérie v algoritme BFO? Aké sú podmienky ukončovania pre maximalizačné a pre minimalizačný problém?

## Okruh 10
1. Aké úlohy môžu hrať včely v algoritme ABC? Krátko ich popíšte.
2. Aká je základná štruktúra iterácií v algoritme ABC? Krátko popíšte jednotlivé kroky.
3. Popíšte, ako a kedy sa zmení rola včely v algoritme ABC.
4. V akom prostredí sú namodelované včely v algoritme ABC? Čomu zodpovedá včela a čomu zdroj potravy počas priebehu algoritmu?
5. Čomu zodpovedá v algoritme vyťažovanie, opustenie a nájdenie zdroja? Aké dôsledky majú tieto akcie pre prehľadávanie?
6. Ako prebieha vyťažovanie zdroja v algoritme ABC? Ako sa určí, ktorého kandidáta včela navštívi?
7. Kedy sa využíva pravdepodobnostná, lačná a náhodná selekcia v algoritme ABC?
8. Aký je rozdiel medzi exploatáciou a exploráciou? Ktoré včely sú zodpovedné za jednotlivé správania v algoritme ABC? Ako ovplyvňuje čistá explorácia a čistá exploatácia prehľadávanie?
9. Ako vyberá zdroj pre navštevu zásobovačka, pozorovateľka a prieskumníčka v algoritme ABC? Ako sú tieto správania implementované?
10. Aké úlohy môžu hrať včely v algoritme ABC a ako sa mení ich podiel v populácii počas priebehu algoritmu?
