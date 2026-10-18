---
tags: [Installatie, Veiligheid, J-serie, T-CAP]
---

# Backup heater

De backup heater (BUH, BH) is een elektrisch element in de waterkring van de Panasonic Aquarea.
Het element heeft een COP van 1. Elke kWh warmte kost dus 1 kWh stroom. De warmtepomp
gebruikt het element als reserve: bij een koude start, bij het ontdooien, als
vorstbeveiliging, als het vermogen tekortschiet en voor de sterilisatierun.

**Zie ook:** [Ontdooien](../../general/defrost.md) ·
[Backup heater bij het ontdooien (Tr < 27 °C)](../settings.md#backup-heater-bij-het-ontdooien) ·
[Storingen `H70`, `H75`](../troubleshooting.md#heaters-h70-h91) · [Bekabeling](wiring.md) · [Plaatsing](installation.md)

## Vermogen en aansluiting

| Uitvoering | Vermogen backup heater | Stroom |
|---|---|---|
| 1-fase (bijv. 5J) | 3 kW | ongeveer 13 A |
| T-CAP 3-fase (bijv. `MXC12H9E8`, `MXC12J9E8`) | instelbaar: uit, 3, 6 of 9 kW | max. 13 A per fase bij 9 kW |

- De backup heater heeft een eigen voeding: *Power Supply 2*. De warmtepomp zelf zit op
  *Power Supply 1*.
- Bij de 3-fase T-CAP gebruikt alleen de 6 en 9 kW-stand de fasen L1 en L2. U kiest het
  vermogen in de systeeminstellingen.
- Op dezelfde voeding zit ook de aansluiting voor de tankheater (booster heater).

!!! warning "Aparte groep"
    De handleiding vraagt aparte groepen voor de warmtepomp en de backup heater.
    Een 5 kW-unit kan ongeveer 2,6 kW uit het net halen, de backup heater 3 kW. Samen is dat
    ongeveer 25 A. Op één groep van 20 A gaat dat mis op het moment dat u de warmte het hardst
    nodig hebt, bijv. bij vorst terwijl u niet thuis bent.

!!! note "Meningen verschillen"
    Volgens één gebruiker past een 5J met backup heater samen onder 20 A, omdat de 5J bij
    A2W35 nog geen 7 A trekt. Anderen wijzen erop dat dit niet volgens de handleiding is.

### Bronnen

- [FransvWoerkom, 2021-12-05](https://gathering.tweakers.net/forum/list_message/69721994#69721994): `MXC12H9E8`: 3-fase Power Supply 2, keuze 3, 6 of 9 kW
- [FransvWoerkom, 2022-01-13](https://gathering.tweakers.net/forum/list_message/70207402#70207402): vermogen in systeeminstellingen; L1 en L2 alleen bij 6 en 9 kW
- [_Piwi_, 2022-01-28](https://gathering.tweakers.net/forum/list_message/70399908#70399908): uit, 3, 6 of 9 kW; 13 A
- [ErikKo, 2023-08-04](https://gathering.tweakers.net/forum/list_message/76123812#76123812): Power Supply 2: 3-fase, 13 A, 9 kW
- [FransvWoerkom, 2022-11-23](https://gathering.tweakers.net/forum/list_message/73568264#73568264): backup heater en tankheater op Power Supply 2
- [FransvWoerkom, 2024-03-24](https://gathering.tweakers.net/forum/list_message/78530360#78530360): 05J plus 13 A backup heater onder 20 A
- [Joris 407, 2024-03-24](https://gathering.tweakers.net/forum/list_message/78531468#78531468): handleiding: aparte groepen
- [ErikVers, 2024-03-24](https://gathering.tweakers.net/forum/list_message/78533930#78533930): 2590 W plus 3000 W, samen 25 A
- [Makrolon, 2024-03-24](https://gathering.tweakers.net/forum/list_message/78531690#78531690): groep valt uit bij extreem weer

## Wanneer de backup heater aangaat

| Situatie | Regel |
|---|---|
| Koude start | Retour (Tr) na 20 minuten nog onder 20 °C: heater aan. |
| Ontdooien | Tr onder 27 °C: zie [instellingen](../settings.md#backup-heater-bij-het-ontdooien). |
| Vorstbeveiliging | Aanvoer of retour onder 6 °C en de pomp draait al 4 minuten: heater aan. Boven 28 °C: uit. |
| Vermogen tekort | Volgens de instellingen *Heater AAN/UIT*: buitentemperatuur, vertraging en watertemperatuur. |
| Begin SWW-run | Inlaat kort onder 20 °C bij een bijna koud vat: heater kort aan. |
| Sterilisatie | Compressor tot 53 °C, daarna de heater tot 65 °C. |

- **Koude start.** Dit gebeurt vooral na een lange stilstand of bij een koude vloer. Een
  `MDC05H3E5` stond na zo'n start 20 uur op de heater en verbruikte 60 kWh. Help de warmtepomp
  door minder groepen tegelijk te openen, een bypass te openen of de Ta in kleine stappen te
  verhogen.
- **Vermogen tekort.** De menu-items heten *Vrijgave buitentemperatuur*,
  *Vertragingstijd voor Heater AAN* en *Watertemperatuur voor Heater AAN/UIT*. Voorbeeld:
  onder −5 °C buiten, Ta 10 minuten 6 °C onder het doel: heater aan; nog 3 °C verschil: uit.
  Zet u de buitentemperatuur op −20 °C, dan gaat de heater bij gewone verwarming praktisch
  nooit aan.
- **T-CAP.** Een T-CAP ontdooit vooral op de compressor. Zie de discussie bij
  [storingen: ontdooien](../troubleshooting.md#ontdooien-h65-h75).
- **SWW.** De heater bij de start van een SWW-run kunt u niet apart uitzetten. Alleen de hele
  heater uitzetten helpt.

### Bronnen

- [vandermark, 2021-04-29](https://gathering.tweakers.net/forum/list_message/67115606#67115606): heater 3 minuten aan, 20 minuten na de start
- [reneeke1970, 2021-04-30](https://gathering.tweakers.net/forum/list_message/67124064#67124064): Tr na 20 min onder 20 °C: heater aan
- [ErikVers, 2024-12-27](https://gathering.tweakers.net/forum/list_message/81141612#81141612): retour < 20 °C na > 20 min; bij ontdooien onder 27 °C
- [Maestro, 2022-03-31](https://gathering.tweakers.net/forum/list_message/71108442#71108442): `MDC05H3E5`: 20 uur en 60 kWh na een koude start
- [Ep Woody, 2022-03-31](https://gathering.tweakers.net/forum/list_message/71108496#71108496): minder groepen open of kortsluiten
- [ErikVers, 2022-03-31](https://gathering.tweakers.net/forum/list_message/71108506#71108506): bypass openen voor hogere Tr
- [koevlaas2, 2022-04-02](https://gathering.tweakers.net/forum/list_message/71124602#71124602): Ta in kleine stappen verhogen
- [thehog, 2021-10-02](https://gathering.tweakers.net/forum/list_message/68917612#68917612): vorstbeveiliging: pomp bij < 6 °C, heater na 4 minuten
- [dirkdeman, 2021-10-22](https://gathering.tweakers.net/forum/list_message/69142982#69142982): service manual: aan < 6 °C, uit > 28 °C
- [klump4u, 2022-03-07](https://gathering.tweakers.net/forum/list_message/70858890#70858890): namen van de menu-items *Heater AAN/UIT*
- [Ep Woody, 2022-02-10](https://gathering.tweakers.net/forum/list_message/70550542#70550542): heater aan bij 4+ °C onder doel, uit bij 2 °C onder doel
- [Nnoitra, 2026-01-09](https://gathering.tweakers.net/forum/list_message/84377020#84377020): voorbeeld −5 °C, 6 °C, 10 minuten, 3 °C
- [sjimmie, 2021-04-30](https://gathering.tweakers.net/forum/list_message/67121594#67121594): heater pas vanaf −20 °C buiten
- [ASW1, 2024-01-26](https://gathering.tweakers.net/forum/list_message/77935984#77935984): buitentemperatuur voor heater op −20 °C
- [FransvWoerkom, 2022-11-23](https://gathering.tweakers.net/forum/list_message/73568264#73568264): T-CAP ontdooit op de compressor
- [cerebrum, 2024-02-08](https://gathering.tweakers.net/forum/list_message/78082104#78082104): inlaat < 20 °C bij SWW-start; niet apart uit te zetten
- [FransvWoerkom, 2025-01-07](https://gathering.tweakers.net/forum/list_message/81235506#81235506): sterilisatie: 53 °C op compressor, daarna heater tot 65 °C

## Verbruik in de praktijk

Het verbruik verschilt sterk per huis, weer en instelling. Een 3 kW-element verbruikt 3 kWh
per uur. De urenteller in de warmtepomp laat zien hoe lang de heater heeft gedraaid.

| Model | Situatie | Verbruik backup heater |
|---|---|---|
| `MDC05H3E5` | een heel jaar | ongeveer 85 uur, 250 kWh |
| 5 kW H-serie | een heel jaar | bijna 100 uur |
| — | 5 jaar | 100 uur (300 kWh), gemiddeld 60 kWh per jaar |
| 9J | 2e stookseizoen | 70 uur, tegen 2607 uur compressor |
| 9J | +1 tot +2 °C, 9 uur | 9 keer aan, elke keer ongeveer 10 minuten |
| 7J | vorst, Ta 34 °C | een paar minuten per ontdooicyclus, ongeveer 1 kWh per dag |
| 7J | vorst, Ta 28–33 °C, 22 ontdooicycli | 5–8 minuten per cyclus, 5 kWh per dag |
| 7J | vorst, Ta 29 °C, ΔT 3 | 7 uur, 21 kWh in 24 uur |

Een hogere aanvoer houdt de Tr boven de grens voor het ontdooien en vermindert het gebruik van
de heater. Zie [Backup heater bij het ontdooien](../settings.md#backup-heater-bij-het-ontdooien)
en [Wat ontdooien kost](../../general/defrost.md#wat-ontdooien-kost).

### Bronnen

- [SJB, 2021-12-02](https://gathering.tweakers.net/forum/list_message/69673398#69673398): `MDC05H3E5`, 85 uur, ongeveer 250 kWh per jaar
- [falconz, 2021-12-03](https://gathering.tweakers.net/forum/list_message/69682818#69682818): 5H, bijna 100 uur per jaar
- [ErikVers, 2024-11-29](https://gathering.tweakers.net/forum/list_message/80882162#80882162): 100 uur in 5 jaar, 60 kWh per jaar
- [nokiaan958GB, 2024-11-30](https://gathering.tweakers.net/forum/list_message/80888854#80888854): 9J, 70 uur; 9 keer 10 minuten
- [blb4, 2026-01-09](https://gathering.tweakers.net/forum/list_message/84372106#84372106): 7J, Ta 34 °C, ongeveer 1 kWh per dag
- [Nnoitra, 2026-01-09](https://gathering.tweakers.net/forum/list_message/84377020#84377020): 7J, 22 ontdooicycli, 5 kWh
- [Phyc, 2026-01-09](https://gathering.tweakers.net/forum/list_message/84371758#84371758): 7J, 7 uur en 21 kWh in 24 uur

## Beperken of uitzetten

Zet de backup heater uit in het menu, niet met de groep in de meterkast. Zonder voeding geeft
de warmtepomp `H70` (zie [storingen](../troubleshooting.md#heaters-h70-h91)).

Er zijn drie plaatsen waar u de heater kunt uitzetten:

| Plaats | Instelling | Effect |
|---|---|---|
| Gebruikersmenu → *Functie instellen* | *Vrijgave backup heater* | Heater uit voor verwarming, ook bij ontdooien |
| *Custom Menu* | *Back-up heater*: aan/uit | Heater uit, ook bij ontdooien |
| Installateursmenu → *Heater AAN/UIT* | *Vrijgave buitentemperatuur* | Heater pas onder deze buitentemperatuur |

Voor de sterilisatierun moet de heater in beide menu's aan staan.

Het *Custom Menu* opent u met de toetscombinatie hamburgerknop + pijl omlaag + pijl links.
Houd de toetsen 5 tot 10 seconden vast.

Bij een koude start na een lange stilstand zette alleen de combinatie van alle uit-standen de
heater uit. Het opwarmen duurde daarna lang, met een lage COP.

!!! warning "Risico's als de heater uit staat"
    - **Bevriezing.** Alleen de circulatiepomp beschermt dan het water. Dat werkt alleen
      zolang het water vrij door het huis kan stromen, zonder dichte zoneregeling.
    - **Ontdooien mislukt.** Zonder heater haalt de warmtepomp de energie uit het cv-water.
      Is dat te koud, dan ontdooit de verdamper niet helemaal. De warmtepomp kan dan vastlopen
      zonder foutmelding, of stopt met `H75`.
    - **Geen reserve.** Valt de compressor uit, dan verwarmt de heater het huis niet meer.
    - **Geen sterilisatie** met de interne heater.

!!! note "Meningen verschillen"
    - **Uitzetten.** Bij een grote vloer met genoeg afgifte kan de heater uit. Een 7J draaide
      4 jaar zonder heater zonder problemen. Met de heater aan kostte één koude dag 21 kWh extra.
    - **Aan laten.** De besparing is klein: ongeveer €9 per jaar bij 60 kWh. Een hogere
      stooklijn om de heater te ontwijken kost ook energie. Laat de heater aan en kijk in
      koude periodes niet te veel naar de grafieken.

### Bronnen

- [Maestro, 2022-03-31](https://gathering.tweakers.net/forum/list_message/71108442#71108442): groep uit geeft `H70`
- [FransvWoerkom, 2026-01-05](https://gathering.tweakers.net/forum/list_message/84331184#84331184): uitzetten via menu; geen ontdooien, `H75`; alleen de pomp tegen bevriezing
- [Maestro, 2022-04-02](https://gathering.tweakers.net/forum/list_message/71126610#71126610): drie uit-standen; lage COP bij opwarmen
- [Cubico, 2026-01-04](https://gathering.tweakers.net/forum/list_message/84327864#84327864): toetscombinatie, 10 seconden; geen beveiliging meer
- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart: Custom Menu, 5 seconden; heater aan voor sterilisatie en ontdooien
- [FransvWoerkom, 2026-08-15](https://gathering.tweakers.net/forum/list_message/85933774#85933774): sterilisatie: backup heater vrijgeven in het gebruikersmenu
- [frisianstar, 2021-02-21](https://gathering.tweakers.net/forum/list_message/66247920#66247920): uitgezet met de drie-toetsencode
- [ASW1, 2024-01-26](https://gathering.tweakers.net/forum/list_message/77935984#77935984): buitentemperatuur op −20 °C
- [I-King, 2022-12-15](https://gathering.tweakers.net/forum/list_message/73813418#73813418): heater uit, verdamper ontdooit niet, vastgelopen zonder foutmelding
- [thehog, 2021-11-03](https://gathering.tweakers.net/forum/list_message/69289546#69289546): heater verwarmt als de compressor defect is
- [flippy, 2022-02-10](https://gathering.tweakers.net/forum/list_message/70550032#70550032): uitzetten bij grote vloer met genoeg afgifte
- [Phyc, 2026-01-09](https://gathering.tweakers.net/forum/list_message/84371758#84371758): 4 jaar zonder heater; 21 kWh op één dag
- [ErikVers, 2024-11-30](https://gathering.tweakers.net/forum/list_message/80889436#80889436): €8,75 per jaar; hogere stooklijn niet waard
- [ErikVers, 2023-11-29](https://gathering.tweakers.net/forum/list_message/77337384#77337384): niet uitzetten, niet naar de grafieken kijken

## Tankheater (booster heater)

De tankheater is een apart element in het SWW-vat. Het is niet de backup heater.

- De instelling *Tankverwarming* kiest het element. *Intern*: de backup heater verwarmt het
  vat. *Extern*: een element in het vat.
- De software zet backup heater en tankheater nooit tegelijk aan. Gaat de backup heater aan bij
  een ontdooicyclus, dan stopt de tankheater.
- De software rekent met een tankheater van 3 kW. Losse Panasonic-vaten hebben een element van
  1,5 kW. De binnenunit `ADC0309` met ingebouwd vat heeft een tankheater van 3 kW.
- De tankheater komt pas na de ingestelde vertraging (standaard 20 minuten), als het vat dan nog
  onder doel min delta is (gemeld voor de J-serie). Slaat het element vaak aan bij een gewone
  run, verhoog dan de vertraging.
- Zonder aparte droogkookbeveiliging moet op `CN6` een draadbrug (zie
  [`H91`](../troubleshooting.md#heaters-h70-h91)).

Voor de keuze tussen element en backup heater bij de legionellarun, zie
[Legionella: welke verwarming](../../general/legionella.md#welke-verwarming).

!!! warning "Netspanning"
    Een tankheater werkt op netspanning. Schakel de spanning uit voordat u aan het element of
    de aansluiting werkt.

### Bronnen

- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart: *Tankverwarming* intern of extern
- [FransvWoerkom, 2022-01-13](https://gathering.tweakers.net/forum/list_message/70207402#70207402): nooit backup heater en tankheater tegelijk
- [Diedo70, 2022-03-13](https://gathering.tweakers.net/forum/list_message/70924118#70924118): nooit tegelijk; software gaat uit van 3 kW, vaten hebben 1,5 kW
- [FransvWoerkom, 2022-03-13](https://gathering.tweakers.net/forum/list_message/70924512#70924512): `ADC0309` heeft een tankheater van 3 kW
- [Pejdref, 2026-01-20](https://gathering.tweakers.net/forum/list_message/84454584#84454584): tankheater uit als de backup heater ontdooit
- [Pejdref, 2024-10-18](https://gathering.tweakers.net/forum/list_message/80435894#80435894): J-serie: tankheater na vertraging onder doel min delta
- [blb4, 2024-06-17](https://gathering.tweakers.net/forum/list_message/79301330#79301330): heater delay: na hoeveel tijd het element bijspringt
- [nMad, 2024-08-15](https://gathering.tweakers.net/forum/list_message/79850624#79850624): standaard vertraging 20 minuten
- [FransvWoerkom, 2024-01-27](https://gathering.tweakers.net/forum/list_message/77950934#77950934): `CN6`, OLP booster heater
