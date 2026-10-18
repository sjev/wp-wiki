---
tags: [Optimalisatie, Installatie]
---

# Ontdooien

Een lucht-waterwarmtepomp haalt warmte uit de buitenlucht. Daarbij kan ijs groeien op de
verdamper. Van tijd tot tijd ontdooit de warmtepomp dat ijs. Dat heet ontdooien, *defrost*
of *deice*. Ontdooien hoort erbij en u kunt het niet uitzetten.

Voor merkspecifieke instellingen en storingen, zie
[Panasonic: backup heater bij het ontdooien](../panasonic/settings.md#backup-heater-bij-het-ontdooien)
en [Panasonic: storingen bij het ontdooien](../panasonic/troubleshooting.md#ontdooien-h65-h75).

**Zie ook:** [Buffervat](buffer-tank.md) · [Hydrauliek](hydraulics.md) · [Tapwater](hot-water.md)

## Waarom en wanneer

- **Oorzaak.** De verdamper is kouder dan de buitenlucht, soms onder 0 °C. Vocht uit de lucht
  condenseert en bevriest op de lamellen. Er kan steeds minder lucht door. Zonder ontdooien
  wordt de verdamper één blok ijs en daalt de COP richting 1.
- **Alleen als de warmtepomp draait.** Ontdooien heeft niets te maken met bevriezen van het
  water in de leidingen. Ook een unit binnen in een omkasting of op zolder ontdooit, want de
  verdamper staat in de buitenlucht.
- **Werking.** De warmtepomp keert de richting van het koudemiddel om. Hij koelt dan het
  cv-water en verwarmt de verdamper. De compressor stopt kort voor het omkeren. Het dooiwater
  loopt onder de unit weg.
- **Start.** De regeling kijkt naar de temperatuur van de verdamper (de leiding uit de
  verdamper), niet naar de buitentemperatuur. Daalt die leidingtemperatuur ver onder de
  buitentemperatuur (bijv. 10 °C eronder), dan start het ontdooien. Een afwijkende sensor
  kunt u controleren in een bak ijswater (0 °C).

### Welk weer geeft de meeste ontdooicycli

| Weer | Ontdooicycli |
|---|---|
| 3 tot 5 °C, hoge luchtvochtigheid | Begint; soms al bij 4 °C |
| Rond 0 °C met mist, sneeuw of motregen | Het meest: elke 15–60 minuten |
| Droge vorst, bijv. onder −2 °C met oostenwind | Weinig: één of twee per dag |

Bij vorst is de lucht meestal droger. Daarom ontdooit de warmtepomp dan minder vaak dan net
boven nul.

### Bronnen

- [FransvWoerkom, 2021-02-07](https://gathering.tweakers.net/forum/list_message/66041148#66041148): ijs op de verdamper, omkeren koudemiddel, dooiwater
- [Thorsd, 2024-01-25](https://gathering.tweakers.net/forum/list_message/77926688#77926688): verdamper in de buitenlucht, ook in een omkasting; niet uit te zetten
- [thehog, 2021-10-22](https://gathering.tweakers.net/forum/list_message/69141716#69141716): bevriest omdat hij draait, niet omdat hij uit staat
- [ErikKo, 2023-11-26](https://gathering.tweakers.net/forum/list_message/77303766#77303766): compressor stopt voor het omkeren
- [flippy, 2022-11-19](https://gathering.tweakers.net/forum/list_message/73520304#73520304): start op verdampertemperatuur; sensor in ijswater controleren
- [martijn v o, 2022-12-10](https://gathering.tweakers.net/forum/list_message/73752962#73752962): start als de leiding ongeveer 10 °C onder de buitentemperatuur zit
- [t.oswald, 2021-10-22](https://gathering.tweakers.net/forum/list_message/69141230#69141230): meeste ontdooicycli bij 3–5 °C en hoge luchtvochtigheid
- [dof, 2023-04-29](https://gathering.tweakers.net/forum/list_message/75196168#75196168): ontdooien bij 4 °C en vochtig weer
- [ecn1985, 2025-12-29](https://gathering.tweakers.net/forum/list_message/84279072#84279072): mist rond het vriespunt geeft veel ontdooicycli
- [FransvWoerkom, 2026-01-07](https://gathering.tweakers.net/forum/list_message/84352638#84352638): onder −2 °C bij droge oostenwind stoppen de ontdooicycli

## Hoeveel ontdooicycli zijn normaal

- In vochtig weer rond 0 °C is één ontdooicyclus per 45–60 minuten normaal. Dat zijn
  15 tot 30 per dag. Een korte periode met één per kwartier komt ook voor.
- In helder of droog weer zijn het er veel minder, bijv. één per uur of één per dag.
- Hoe meer vermogen de warmtepomp levert, hoe sneller de verdamper aanvriest. Per geleverde
  kWh maakt het weinig uit.
- Bekijk voor u gaat zoeken de verdamper vlak voor een ontdooicyclus. Zit er een dikke laag ijs
  op, dan is het ontdooien nodig.

### Bronnen

- [runeazn, 2024-11-22](https://gathering.tweakers.net/forum/list_message/80798464#80798464): vraag naar het aantal per dag
- [Arrowsong, 2024-11-22](https://gathering.tweakers.net/forum/list_message/80798514#80798514): ongeveer één per uur bij sneeuw en nattigheid
- [Cubico, 2024-11-22](https://gathering.tweakers.net/forum/list_message/80798704#80798704): 19 per dag
- [RemySoeters, 2024-11-22](https://gathering.tweakers.net/forum/list_message/80799674#80799674): 17 per dag
- [Thorsd, 2024-11-30](https://gathering.tweakers.net/forum/list_message/80882756#80882756): 28 op één dag
- [Herw76, 2022-12-10](https://gathering.tweakers.net/forum/list_message/73752238#73752238): elke 50 minuten is normaal bij dit weer
- [Beekforel, 2023-11-30](https://gathering.tweakers.net/forum/list_message/77348904#77348904): een tijdje elk kwartier; dikke laag ijs voor het ontdooien
- [Bra-Jo, 2023-11-30](https://gathering.tweakers.net/forum/list_message/77348906#77348906): 14 in 12 uur door kou en vochtige lucht
- [Appelpie3000, 2023-11-30](https://gathering.tweakers.net/forum/list_message/77349068#77349068): minder bij helder weer, meer bij mist
- [ErikVers, 2024-11-29](https://gathering.tweakers.net/forum/list_message/80882162#80882162): bij droge vorst één of twee per dag
- [ErikVers, 2025-12-29](https://gathering.tweakers.net/forum/list_message/84279244#84279244): meer afgifte geeft vaker ontdooien; per kWh weinig verschil

## Wat ontdooien kost

**Energie.** Een ontdooicyclus duurt ongeveer 6 tot 10 minuten. Op een 9 kW-unit kostte één
cyclus 0,35 tot 0,6 kWh warmte uit het cv-water. Die warmte moet de warmtepomp daarna opnieuw
maken. Rekenvoorbeeld: elke 45 minuten één cyclus van 0,6 kWh is 32 × 0,6 ≈ 19 kWh warmte per
dag. Bij een COP van 3,5 is dat ongeveer 5,5 kWh stroom. Ontdooit de warmtepomp met een
elektrisch element (COP 1), dan kost dezelfde warmte ongeveer 3,5 keer zoveel stroom. Over een
heel jaar valt het verbruik van het element vaak mee: tientallen tot ruim honderd kWh.

**Comfort.**

- Tijdens het ontdooien verwarmt de warmtepomp niet. De aanvoertemperatuur zakt, bijv. van
  35 naar 20 °C.
- Radiatoren merken dat. Vloerverwarming merkt er bijna niets van.
- Na het ontdooien draait de compressor een tijd harder om de warmte in te halen. Dat geeft
  meer geluid. Het kan lang duren voordat hij weer rustig op laag vermogen draait.
- De circulatiepomp kan tijdens het ontdooien veel harder pompen dan normaal (bijv. 30 tot
  40 l/min). Dat geeft ruis in de leidingen. Zie
  [Waar de warmte vandaan komt](#waar-de-warmte-vandaan-komt) voor oplossingen.

!!! note "Meningen verschillen"
    - **Ontdooien kost weinig.** De warmte om het ijs te smelten komt vrij bij het bevriezen
      van de waterdamp. Het grootste verlies is de tijd waarin de warmtepomp niet verwarmt.
    - **Ontdooien kost veel.** Ook zonder element kost elke cyclus energie die de warmtepomp
      daarna moet terugwinnen. Het ijs op de verdamper verlaagt bovendien de COP tussen de
      cycli in. Op vochtige dagen rond 0 °C daalde de COP van boven 4 naar onder 3.
    - **Het element is niet het grootste probleem.** Gemeten is ongeveer 2 minuten
      elementtijd per cyclus. Dure ontdooidagen komen vooral door het stoppen en starten.

### Bronnen

- [Thorsd, 2023-11-26](https://gathering.tweakers.net/forum/list_message/77306574#77306574): 0,35–0,6 kWh uit het cv-water per cyclus, gemeten met warmtemeter
- [ConQuestador, 2023-11-26](https://gathering.tweakers.net/forum/list_message/77306666#77306666): cyclus van 15 minuten kostte minder dan 1 kWh
- [Thorsd, 2024-11-29](https://gathering.tweakers.net/forum/list_message/80878966#80878966): rekenvoorbeeld 32 × 0,6 kWh; geen warmte tijdens ~6 minuten; lagere COP door ijs
- [Proton_, 2024-11-07](https://gathering.tweakers.net/forum/list_message/80643102#80643102): kosten met element versus zonder element
- [nokiaan958GB, 2024-11-07](https://gathering.tweakers.net/forum/list_message/80643536#80643536): na het ontdooien lang hoge frequentie en flow
- [t.oswald, 2021-10-22](https://gathering.tweakers.net/forum/list_message/69141230#69141230): 57 en 132 kWh per seizoen met element; geen effect op kamertemperatuur
- [ErikVers, 2024-11-29](https://gathering.tweakers.net/forum/list_message/80882162#80882162): gemiddeld 60 kWh per jaar met element
- [ErikVers, 2022-12-17](https://gathering.tweakers.net/forum/list_message/73839614#73839614): zonder element harder werken en meer geluid na het ontdooien
- [dof, 2024-01-13](https://gathering.tweakers.net/forum/list_message/77791508#77791508): aanvoer zakt van 35 naar 20 °C; radiatoren merken het, vloerverwarming niet
- [FransvWoerkom, 2021-02-07](https://gathering.tweakers.net/forum/list_message/66041148#66041148): ijs smelten kost weinig rendement; tien minuten geen verwarming
- [Beer070, 2026-01-06](https://gathering.tweakers.net/forum/list_message/84338080#84338080): COP onder 3 tussen de cycli bij vochtige lucht
- [dof, 2024-11-30](https://gathering.tweakers.net/forum/list_message/80890076#80890076): ongeveer 2 minuten elementtijd per cyclus
- [mar-10, 2026-02-04](https://gathering.tweakers.net/forum/list_message/84574134#84574134): 42 l/min tijdens het ontdooien geeft ruis
- [blb4, 2024-01-08](https://gathering.tweakers.net/forum/list_message/77725638#77725638): afgiftesysteem moet de hoge flow aankunnen

## Waar de warmte vandaan komt

De warmtepomp haalt de warmte voor het ontdooien uit het water dat terugkomt uit het huis. Is
dat niet genoeg, dan helpt een elektrisch element.

- **Vloerverwarming.** Een grote vloer bevat veel water en massa. Zonder element zakte de
  retour bij 85 m² vloerverwarming niet onder 21 °C. Buizen met een grotere diameter bevatten
  meer water.
- **Systeeminhoud.** Bij weinig water koelt het water snel af. Het element moet dan vaker
  helpen. Flow is even belangrijk als inhoud: bij te weinig flow volgt een storing.
- **Buffervat.** Een seriebuffer in de retour levert warmte voor het ontdooien. Een bypass die
  opent bij hoge pompdruk stuurt het water tijdens het ontdooien vooral over de buffer. Zo
  blijft de warmte in de vloer en ruisen de leidingen niet.
- **Klep met ontdooisignaal.** Een klep die tijdens het ontdooien een deel van de installatie
  afsluit, heeft hetzelfde effect. Dit maakt de installatie wel complexer.
- **Omvang van een buffer.** Wilt u niets van het ontdooien merken, dan moet de buffer groot
  zijn: bij 8 minuten en 32 l/min ongeveer 280 liter.
- **Lage retourtemperatuur.** Een goed afgiftesysteem draait op een lage aanvoer. De retour is
  dan koud en het element springt vaker bij.

### Bronnen

- [ErikVers, 2022-12-17](https://gathering.tweakers.net/forum/list_message/73839614#73839614): retour niet onder 21 °C bij 85 m² vloer; zonder element harder werken en meer geluid daarna
- [SkullboyNL, 2023-02-27](https://gathering.tweakers.net/forum/list_message/74597532#74597532): grotere buisdiameter, meer water voor het ontdooien
- [dirkdeman, 2021-10-22](https://gathering.tweakers.net/forum/list_message/69140256#69140256): kleine systeeminhoud, element springt eerder bij
- [thehog, 2021-10-22](https://gathering.tweakers.net/forum/list_message/69141716#69141716): energie en flow zijn belangrijk bij het ontdooien
- [blb4, 2023-01-28](https://gathering.tweakers.net/forum/list_message/74290750#74290750): seriebuffer met bypass; energie uit de buffer
- [blb4, 2023-01-24](https://gathering.tweakers.net/forum/list_message/74238616#74238616): klep op het ontdooisignaal; bypass tegen ruis
- [sjimmie, 2023-01-24](https://gathering.tweakers.net/forum/list_message/74238808#74238808): houd het eenvoudig
- [dof, 2024-01-13](https://gathering.tweakers.net/forum/list_message/77791508#77791508): buffer van ~280 liter om niets te merken
- [runeazn, 2024-11-22](https://gathering.tweakers.net/forum/list_message/80808260#80808260): lage aanvoer geeft koude retour bij het ontdooien

## Minder of kortere ontdooicycli

Het weer bepaalt het meeste. Met instellingen verandert u weinig. Dit helpt wel:

- **Niet draaien in de koudste, vochtigste uren.** Laat de warmtepomp 's nachts en rond
  zonsopkomst stilstaan, als isolatie en afgifte dat toelaten. Zo vermijdt u de uren met de
  meeste ontdooicycli en de laagste COP. Zie ook
  [Stooklijn: nachtverlaging](heating-curve.md#nachtverlaging).
- **Stooklijn niet te steil.** Bij een steile lijn moet de warmtepomp juist in het
  ontdooigebied veel harder werken als het kouder wordt. Een advies voor vloerverwarming:
  maximaal 8–10 °C verschil tussen het warme en het koude punt.
- **Minder warmtevraag.** Rustiger draaien geeft minder ontdooicycli, maar ook minder warmte in
  huis. Per geleverde kWh wint u bijna niets.

!!! note "Meningen verschillen"
    - **Aanvoer 1 °C hoger.** Een warmere retour levert meer warmte voor het ontdooien en
      vraagt minder van het element. Test het: vergelijk het totale verbruik over een paar uur
      met hetzelfde weer.
    - **Geen effect op het aantal.** Het aantal ontdooicycli hangt af van buitentemperatuur,
      luchtvochtigheid en retourtemperatuur. Een hogere aanvoer vermindert het aantal niet direct.
    - **Lagere aanvoer.** Na een overstap naar lagere aanvoer leken er iets minder ontdooicycli
      te zijn, omdat de compressor minder hard werkt. Het element moest wel langer helpen.
    - **Stille modus.** Volgens een gebruiker geeft een stille modus meer ontdooicycli. Een ander
      raadt hem bij koud weer af.

### Bronnen

- [ErikVers, 2024-11-19](https://gathering.tweakers.net/forum/list_message/80758090#80758090): niet draaien rond zonsopkomst; rustiger draaien wint bijna niets; stille modus vermijden
- [ErikVers, 2024-11-29](https://gathering.tweakers.net/forum/list_message/80882162#80882162): instellingen voorkomen ontdooien niet; niet draaien tussen 00:00 en 10:00
- [blb4, 2024-01-08](https://gathering.tweakers.net/forum/list_message/77725638#77725638): weinig te sturen; ontdooien 's nachts alleen voorkomen door niet te draaien; stille modus
- [Thorsd, 2024-11-29](https://gathering.tweakers.net/forum/list_message/80878966#80878966): stooklijn niet te steil; hogere aanvoer vermindert het aantal niet direct
- [ErikVers, 2024-11-29](https://gathering.tweakers.net/forum/list_message/80880306#80880306): maximaal 8–10 °C tussen het warme en het koude punt bij vloerverwarming
- [runeazn, 2024-11-22](https://gathering.tweakers.net/forum/list_message/80808260#80808260): aanvoer 1 °C hoger kan lonen
- [Nnoitra, 2024-11-22](https://gathering.tweakers.net/forum/list_message/80809450#80809450): aantal hangt af van buitentemperatuur, luchtvochtigheid en retour; zelf vergelijken
- [cerebrum, 2024-11-23](https://gathering.tweakers.net/forum/list_message/80810242#80810242): lagere aanvoer, iets minder ontdooicycli, element langer aan

## Plaatsing, luchtstroom en omkasting

- **Geen eigen lucht aanzuigen.** De koude uitblaaslucht mag niet terug in de inlaat komen.
  Houd daarom ongeveer 1 meter vrij en snoei planten voor de unit. Een unit die zijn eigen
  koude lucht aanzuigt, meet een te lage buitentemperatuur en vriest sneller aan.
- **Omkasting.** Elke beperking van de luchtstroom kost rendement. Een kast met dichte
  lamellen aan de uitblaaszijde duwt de lucht naar de inlaat. Gemeten: 4 tot 5 °C lagere
  buitentemperatuur, of 2 °C bij een ander model. Wilt u toch een kast, gebruik dan weinig,
  dunne lamellen onder een vlakke hoek. Scheid uitblaas en inlaat binnen de kast.
- **Dak tegen regen en sneeuw.** Regen of sneeuw op een verdamper onder 0 °C bevriest. Een dak
  of carport boven de unit beschermt, zonder de luchtstroom te beperken.
- **Wind.** Harde wind op de verdamper bij vorst laat de verdamper sneller aanvriezen en
  maakt het ontdooien moeilijker.
- **Dooiwater.** Bij een ontdooicyclus loopt veel water uit de hele verdamper. Zorg voor genoeg
  grind onder en naast de unit, of voor een afvoer. Anders groeit er een plaat ijs. IJs op
  een omkasting of voeten kan trillingen naar het huis doorgeven.

### Bronnen

- [thehog, 2021-10-11](https://gathering.tweakers.net/forum/list_message/69012044#69012044): 1 meter vrij tegen eigen lucht aanzuigen; wind op de warmtewisselaar
- [Tinkerer84, 2023-12-02](https://gathering.tweakers.net/forum/list_message/77375616#77375616): kap en planten, uitblaaslucht weer aangezogen
- [Gebruiker 2, 2023-12-02](https://gathering.tweakers.net/forum/list_message/77375254#77375254): buitentemperatuur 4–5 °C lager door een omkasting
- [ASW1, 2023-12-02](https://gathering.tweakers.net/forum/list_message/77376104#77376104): uitblaas half dicht; dunne lamellen onder een vlakke hoek
- [FransvWoerkom, 2023-12-03](https://gathering.tweakers.net/forum/list_message/77387244#77387244): belemmerde uitblaas gaat naar de inlaat
- [Aikon, 2023-12-02](https://gathering.tweakers.net/forum/list_message/77375746#77375746): een kap kost altijd rendement
- [martijn v o, 2022-08-10](https://gathering.tweakers.net/forum/list_message/72386090#72386090): afscheiding tussen uitblaas en inlaat in de kast
- [blb4, 2024-12-11](https://gathering.tweakers.net/forum/list_message/80999032#80999032): beperking luchtstroom negatief; regen en sneeuw weren positief
- [louwerens, 2024-12-11](https://gathering.tweakers.net/forum/list_message/81002024#81002024): omkasting scheelde 2 °C; na weghalen langere runs
- [dof, 2024-12-13](https://gathering.tweakers.net/forum/list_message/81021756#81021756): dakje boven de unit
- [flippy, 2022-10-03](https://gathering.tweakers.net/forum/list_message/72999218#72999218): wind en regen op de verdamper bij vorst
- [blb4, 2023-05-06](https://gathering.tweakers.net/forum/list_message/75256114#75256114): genoeg grind voor het dooiwater
- [hnq, 2023-04-30](https://gathering.tweakers.net/forum/list_message/75204856#75204856): dooiwater komt van de hele verdamper
- [twain4me, 2022-05-03](https://gathering.tweakers.net/forum/list_message/71411014#71411014): grind en afvoer; plaat ijs
- [blb4, 2026-01-08](https://gathering.tweakers.net/forum/list_message/84364512#84364512): ijs op omkasting en voeten geeft brom
