---
tags: [Optimalisatie, Installatie]
---

# COP en meten

De COP (coefficient of performance) is de warmte die de warmtepomp maakt, gedeeld door de
stroom die hij daarvoor gebruikt. Deze pagina legt uit waar de COP van afhangt, welke waarden
gebruikers in de praktijk meten en hoe u zelf warmte en stroom meet.

**Zie ook:** [Ontdooien](defrost.md) · [Pendelen](cycling.md) · [Tapwater](hot-water.md) ·
[Hydrauliek](hydraulics.md) · [Panasonic: sensoren](../panasonic/hardware/sensors.md)

## COP en SCOP

- **COP** is de verhouding op één moment of over een korte periode: warmte ÷ stroom.
  Een COP op één moment zegt weinig. Een run, een dag of een week geeft een beter beeld.
- **SCOP** (seizoens-COP) is dezelfde verhouding over een heel stookseizoen of jaar. Tel
  daarvoor energie op (kWh), niet vermogen (W): totale warmte ÷ totaal stroomverbruik.
- Tel alles mee wat u wilt beoordelen: compressor, pompen, elektronica en een elektrisch
  element. Een COP met en zonder element of ontdooien kan flink verschillen.
- De SCOP uit de folder is een labwaarde. Gebruikers halen die niet altijd.

**Vergelijken met gas.** 1 m³ gas is ongeveer 9,8 kWh warmte. Bij een COP van 4,5 vervangt
iets meer dan 2 kWh stroom 1 m³ gas. Vuistregel: het verbruik van de warmtepomp in kWh is
ongeveer 2 × het oude gasverbruik in m³. Veel tapwater verlaagt de SCOP, dus dan valt het
verbruik hoger uit. Als ondergrens voor een zinvolle warmtepomp noemen gebruikers een
SCOP van 3.

### Bronnen

- [Proton_, 2022-10-14](https://gathering.tweakers.net/forum/list_message/73129256#73129256): momentane COP weinig nuttig; voor dag-, maand- of SCOP vermogen integreren naar energie
- [Thorsd, 2024-11-04](https://gathering.tweakers.net/forum/list_message/80605606#80605606): COP betrouwbaarder over een langere periode
- [RichieB, 2026-02-01](https://gathering.tweakers.net/forum/list_message/84546934#84546934): COP met en zonder backup heater
- [Cige, 2023-03-15](https://gathering.tweakers.net/forum/list_message/74769516#74769516): SCOP uit de specificaties is optimistisch
- [sjimmie, 2024-01-22](https://gathering.tweakers.net/forum/list_message/77886868#77886868): 1 m³ ≈ 9,77 kWh; bij COP 4,5 ruim 2 kWh per m³
- [t.oswald, 2023-03-15](https://gathering.tweakers.net/forum/list_message/74770098#74770098): vuistregel kWh ≈ 2 × m³ gas
- [ercolano, 2024-01-21](https://gathering.tweakers.net/forum/list_message/77882254#77882254): veel tapwater geeft een lagere SCOP
- [blb4, 2026-01-11](https://gathering.tweakers.net/forum/list_message/84387436#84387436): SCOP van 3 als break-even met gas

## Wat de COP bepaalt

De COP hangt vooral af van het temperatuurverschil tussen buitenlucht en aanvoerwater
(de *lift*: aanvoertemperatuur − buitentemperatuur). Hoe kleiner de lift, hoe hoger de COP.
Het vermogen of de compressorfrequentie heeft veel minder invloed; zie
[Pendelen](cycling.md#waarom-pendelen-nadelig-is).

- **Aanvoertemperatuur.** Een lagere aanvoertemperatuur geeft altijd een betere COP. Gebruikers
  rekenen met ongeveer 2 % COP per graad. Dit is een vuistregel, geen meting. Een voorbeeld: 5 °C warmer water kostte ongeveer
  0,4 op een SCOP van 4.
- **Afgiftesysteem.** Een groot afgiftesysteem laat een lage aanvoer toe. Bij gelijk weer kan
  een warmtepomp op 45 °C een COP van 2 halen en op 26 °C een COP van 4 tot 5.
- **Buitentemperatuur.** 's Nachts is het kouder, dus is de COP lager dan overdag.
- **Grens van de techniek.** Goede metingen komen uit op ongeveer 50 % van de theoretische
  (Carnot) COP bij dezelfde temperaturen.
- **Tapwater en ontdooien** verlagen de COP. Zie [Tapwater: temperatuur en
  COP](hot-water.md#temperatuur-en-cop) en [Ontdooien: wat ontdooien kost](defrost.md#wat-ontdooien-kost).

### Bronnen

- [Thorsd, 2024-02-24](https://gathering.tweakers.net/forum/list_message/78247670#78247670): COP uitgezet tegen lift en buitentemperatuur; ontdooien en SWW lager; Carnot 50 %
- [pgeene, 2022-12-27](https://gathering.tweakers.net/forum/list_message/73931842#73931842): lagere aanvoertemperatuur geeft altijd een betere COP
- [Heronimo, 2022-03-25](https://gathering.tweakers.net/forum/list_message/71046988#71046988): ongeveer 2 % COP per graad lagere aanvoer
- [Pejdref, 2024-01-04](https://gathering.tweakers.net/forum/list_message/77693968#77693968): 2 % per graad als aanname
- [Andrehj, 2022-09-18](https://gathering.tweakers.net/forum/list_message/72822292#72822292): 5 °C extra kost ongeveer 0,4 COP
- [ErikVers, 2025-12-26](https://gathering.tweakers.net/forum/list_message/84264284#84264284): 45 °C en COP 2 tegenover 26 °C en COP 4–5; afgifte maakt het verschil
- [Tiesert, 2023-01-01](https://gathering.tweakers.net/forum/list_message/73985854#73985854): COP 's nachts lager door lagere buitentemperatuur
- [Peanutsonic, 2022-12-01](https://gathering.tweakers.net/forum/list_message/73652030#73652030): COP 3,92 is 49,7 % van Carnot

## COP in de praktijk

Waarden die gebruikers met een eigen kWh-meter en warmtemeter maten. Alle installaties zijn
lucht/water-monoblocs van 7 tot 9 kW.

| Situatie | Aanvoer | COP |
|---|---|---|
| Nacht, buiten 4 °C, geen ontdooicycli, vooral radiatoren | 35 °C | 4,15 |
| Etmaal, buiten 3 °C, alleen weersafhankelijk, 2 starts | 37 °C | 3,92 |
| Week in december, alleen radiatoren | 40 °C | ongeveer 2,9 |
| Maand januari 2026, inclusief element | onbekend | 2,63 (3,16 zonder element) |
| Mistige dag rond 1–2 °C, 18 ontdooicycli (schatting) | onbekend | ongeveer 2,2 |
| Heel jaar, verwarming en tapwater, 90 % radiatoren | 30–35 °C | 4,0 (SCOP) |

Het slechtste weer is vochtig weer rond 0 °C, door veel ontdooicycli. Bij droge vorst onder
−2 °C stopt het ontdooien en stijgt de COP weer boven 3.

### Bronnen

- [Thorsd, 2024-11-04](https://gathering.tweakers.net/forum/list_message/80605606#80605606): buiten 4 °C, aanvoer 35 °C, COP 4,15, externe meters
- [Peanutsonic, 2022-12-01](https://gathering.tweakers.net/forum/list_message/73652030#73652030): buiten 3 °C, aanvoer 37 °C, COP 3,92, kWh-meter en geijkte Kamstrup
- [blb4, 2022-12-17](https://gathering.tweakers.net/forum/list_message/73839890#73839890): 194 kWh stroom, 561 kWh warmte in 7 dagen, aanvoer 40 °C
- [RichieB, 2026-02-01](https://gathering.tweakers.net/forum/list_message/84546934#84546934): januari, MID-meter en Kamstrup, COP 2,63 / 3,16
- [FransvWoerkom, 2023-11-23](https://gathering.tweakers.net/forum/list_message/77272630#77272630): dagen met 18 ontdooicycli, geschatte COP 2,2
- [FransvWoerkom, 2026-01-07](https://gathering.tweakers.net/forum/list_message/84352638#84352638): onder −2 °C geen ontdooicycli, COP weer boven 3
- [Thorsd, 2023-09-01](https://gathering.tweakers.net/forum/list_message/76391160#76391160): jaar-SCOP 4, externe meters
- [Thorsd, 2024-02-24](https://gathering.tweakers.net/forum/list_message/78247670#78247670): aanvoer ongeveer 35 °C bij 0 °C en 30 °C bij 10 °C

## Stroom meten

Meet het verbruik met een eigen kWh-meter in de groep van de warmtepomp. Een tweede meter op
de groep van het elektrische element laat zien hoeveel stroom dat gebruikt.

- **S0-uitgang.** De meter geeft een puls per 0,5 of 1 Wh. Eenvoudig uit te lezen, maar bij
  laag verbruik komen de pulsen traag.
- **RS485/Modbus.** De meter geeft ook het actuele vermogen, totaalverbruik en spanning.
  Dit is beter voor laag verbruik. Uitlezen kan met een USB-naar-RS485-adapter.
- **Meterkeuze.** Veel gebruikers kiezen een meter met MID-keur. De nominale stroom
  (bijv. 5 A) bepaalt vooral de precisie; let daarnaast op de maximale stroom (bijv. 40 A).
  Een driefasige warmtepomp vraagt een driefasige meter.

!!! warning "Netspanning"
    Een kWh-meter plaatst u in een groep met 230 V of 400 V. Schakel de groep spanningsloos
    voordat u werkt. Laat het werk doen door iemand die bevoegd is als u twijfelt.

### Bronnen

- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart, *Extra's*: kWh-meters, S0-puls per 0,5 of 1 Wh, RS485-meters, warmtemeter
- [padoempats, 2022-12-01](https://gathering.tweakers.net/forum/list_message/73656492#73656492): Modbus in plaats van puls, beter voor laag verbruik
- [Thorsd, 2024-10-13](https://gathering.tweakers.net/forum/list_message/80387642#80387642): nominale stroom voor precisie, 40 A maximaal
- [ConQuestador, 2023-11-13](https://gathering.tweakers.net/forum/list_message/77160464#77160464): driefasige MID-meters
- [Thorsd, 2023-09-01](https://gathering.tweakers.net/forum/list_message/76391160#76391160): aparte meters voor warmtepomp en element

## Warmte meten

**Warmtemeter.** Een warmtemeter (bijv. Kamstrup Multical) meet flow, aanvoer- en
retourtemperatuur en telt de warmte op. Veel gebruikers lezen die uit via USB of draadloos.

- Aanvoer of retour maakt niet uit, maar er mag geen aftakking zitten tussen meter en
  warmtepomp. Plaats de meter niet vlak voor een circulatiepomp. Lucht en vuil verstoren
  de meting.
- De voelers zitten in het water. Voelers op de buitenkant van een buis meten minder goed.
- De warmte die bij het ontdooien uit het water gaat, telt een Kamstrup in een apart register.
  Let daarop als u de COP inclusief ontdooien wilt.
- Lees niet te traag uit. Eens per 2 minuten is te grof om een ontdooicyclus te volgen.

**Zelf rekenen.** Zonder warmtemeter rekent u met flow en ΔT:
vermogen (W) ≈ 70 × flow (l/min) × ΔT. Zie [Hydrauliek](hydraulics.md#flow-t-en-vermogen)
voor de formule. Gebruik de echte flow, niet de pompstand. Extra temperatuursensoren
(bijv. DS18B20) in een dompelbuis met koelpasta meten beter dan voelers op de buis.

**Sensoren controleren.** Laat het water rondpompen zonder dat de warmtepomp verwarmt. Na een
paar minuten moeten aanvoer en retour gelijk zijn. Zo niet, stel ze bij. Voor ΔT telt vooral
dat beide sensoren onderling kloppen.

### Bronnen

- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart, warmtemeter Kamstrup via USB; sensoren controleren door water rond te pompen
- [Diedo70, 2022-11-09](https://gathering.tweakers.net/forum/list_message/73403836#73403836): Kamstrup Multical 303 draadloos
- [Thorsd, 2023-12-31](https://gathering.tweakers.net/forum/list_message/77651146#77651146): aanvoer of afvoer maakt niet uit; afwijking bij verkeerde plaatsing, lucht of vuil
- [blb4, 2023-12-31](https://gathering.tweakers.net/forum/list_message/77652136#77652136): geen aftakking tussen meter en warmtepomp
- [FransvWoerkom, 2023-12-31](https://gathering.tweakers.net/forum/list_message/77653386#77653386): niet vlak voor de circulatiepomp
- [thehog, 2021-06-08](https://gathering.tweakers.net/forum/list_message/67624988#67624988): Kamstrup meet in het water, niet op de buis
- [Thorsd, 2024-11-21](https://gathering.tweakers.net/forum/list_message/80787774#80787774): ontdooiwarmte in een apart register; sensoren onderling kalibreren
- [Thorsd, 2023-11-26](https://gathering.tweakers.net/forum/list_message/77302382#77302382): uitlezen eens per 2 minuten te traag voor ontdooien
- [FransvWoerkom, 2024-11-21](https://gathering.tweakers.net/forum/list_message/80787444#80787444): P = 70 × flow × ΔT
- [sjimmie, 2022-10-14](https://gathering.tweakers.net/forum/list_message/73129542#73129542): rekenen met flow, niet met pompsnelheid
- [Erwin94, 2023-01-22](https://gathering.tweakers.net/forum/list_message/74222506#74222506): DS18B20 in dompelbuis met koelpasta

## Nauwkeurigheid

De fout in de berekende warmte is ongeveer de som van de relatieve fouten in flow en ΔT.
De fout in ΔT is tot het dubbele van de fout per sensor.

Voorbeeld: flow 20 l/min (fout 0,5 l/min) en ΔT 2 °C (fout 0,25 °C). Het vermogen is 2800 W.
De fout is 0,5/20 + 0,25/2 = 15 %, dus ongeveer 400 W. Met sensoren die op hele graden
afronden is bij 10 l/min elke stap al 700 W.

- Een grotere ΔT geeft een kleinere relatieve fout.
- Kalibreer de sensoren rond de temperatuur waarop u stookt.
- Een warmtemeter heeft geijkte, gepaarde voelers (bijv. Pt500, resolutie 0,01 °C). Een
  losse DS18B20 heeft een resolutie van 0,0625 °C en is niet gekalibreerd.
- Een constante afwijking is minder erg als u alleen wilt zien of een wijziging helpt.

!!! note "Meningen verschillen"
    - **Een warmtemeter is nodig.** Rekenen met drie onnauwkeurige sensoren geeft geen
      betrouwbare warmte. Een warmtemeter meet veel nauwkeuriger.
    - **Twee goede sensoren zijn genoeg.** Ook de flow van een warmtemeter heeft een fout van
      2 tot 5 %. Met twee goedkope DS18B20's haalt u voor weinig geld een hoge nauwkeurigheid.

### Bronnen

- [FransvWoerkom, 2024-11-21](https://gathering.tweakers.net/forum/list_message/80787444#80787444): foutberekening, voorbeeld 2800 W ± 400 W, grote ΔT helpt
- [FransvWoerkom, 2024-11-04](https://gathering.tweakers.net/forum/list_message/80606704#80606704): bij kleine ΔT fout van tientallen procenten; ijken rond de gebruikstemperatuur
- [Ep Woody, 2022-04-19](https://gathering.tweakers.net/forum/list_message/71282874#71282874): hele graden bij 10 l/min is 700 W per stap
- [dunklefaser, 2021-03-01](https://gathering.tweakers.net/forum/list_message/66351590#66351590): Pt500 met 0,01 °C, DS18B20 0,0625 °C ongekalibreerd
- [Wouter2403, 2022-08-18](https://gathering.tweakers.net/forum/list_message/72472344#72472344): constante afwijking volstaat om trends te zien
- [sjimmie, 2022-10-14](https://gathering.tweakers.net/forum/list_message/73129542#73129542): drie onnauwkeurige sensoren; liever een warmtemeter
- [FransvWoerkom, 2021-03-01](https://gathering.tweakers.net/forum/list_message/66353130#66353130): Kamstrup-flow 2–5 %; twee DS18B20's goedkoop en nauwkeurig

## Jaarverbruik

Een jaarverbruik zegt alleen iets samen met de woning. Gemeld door gebruikers:

| Woning | Afgifte | Gas vroeger | Warmtepomp |
|---|---|---|---|
| ~220 m², 1970, matig geïsoleerd; verwarming en tapwater | 90 % radiatoren | 2000 m³ | 3820 kWh + 171 kWh element; 16 000 kWh warmte |
| Grote vrijstaande woning, 1997 | radiatoren met ventilatoren | 1400–1500 m³ | gemiddeld 2500 kWh per jaar over 5 jaar |
| Woning met 7 kW split; tapwater apart | onbekend | 1000 m³ | 1006 kWh van half december tot begin maart |
| Woning met 5 kW; tapwater met warmtepompboiler | onbekend | 1000 m³ verwarming + 200 m³ tapwater | binnen de vuistregel 2 × m³, extern gemeten |

Het tweede getal komt deels uit de app van de fabrikant. Die wijkt af van een eigen meter.

### Bronnen

- [Thorsd, 2023-09-01](https://gathering.tweakers.net/forum/list_message/76391160#76391160): 220 m², 1970, 3820 + 171 kWh, 16 000 kWh warmte
- [Carboy54, 2022-02-20](https://gathering.tweakers.net/forum/list_message/70661962#70661962): vrijstaand 1997, radiatoren met ventilatoren, 2500 kWh per jaar
- [Carboy54, 2022-11-22](https://gathering.tweakers.net/forum/list_message/73562956#73562956): 2500 kWh gemiddeld over 5 jaar voor 1400–1500 m³; afwijking ten opzichte van eigen meter
- [Cige, 2023-03-15](https://gathering.tweakers.net/forum/list_message/74769516#74769516): 1000 m³, 1005,7 kWh van 12-12-2022 tot 8-3-2023
- [t.oswald, 2023-03-15](https://gathering.tweakers.net/forum/list_message/74770098#74770098): 1000 + 200 m³, haalt 2 × m³ zonder moeite
