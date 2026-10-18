---
tags: [Veiligheid, Installatie, J-serie, L-serie, M-serie, T-CAP]
---

# Bekabeling en beveiliging

Deze pagina gaat over de elektrische aansluiting van een Panasonic Aquarea: voedingskabels,
automaten, aardlek, werkschakelaars en de stuurdraden naar de print.

!!! warning "Netspanning en de norm"
    Op de voeding, de print en de klepaansluitingen staat 230 V of 400 V. Schakel alle groepen
    uit en meet na voordat u iets aanraakt. Deze pagina vervangt de installatiehandleiding
    en de NEN 1010 niet. Twijfelt u? Laat een erkend installateur de aansluiting maken.

**Zie ook:** [Kamerthermostaat op `CN2`/`CN4`](../settings.md#kamerthermostaat) ·
[Communicatiefout `H90`](../troubleshooting.md#communicatie-h90) ·
[Heaterstoringen `H70`, `H91`](../troubleshooting.md#heaters-h70-h91) ·
[Backup heater](backup-heater.md) · [Sensoren](sensors.md)

## Twee voedingen

Een 1-fase monoblock heeft twee voedingen: één voor de compressor (*power supply 1*) en één
voor de backup heater van 3 kW (*power supply 2*). Elke voeding krijgt een eigen groep en
een eigen kabel.

- In de unit zitten twee aardlekschakelaars (RCCB's). Die beveiligen de voedingskabel niet.
  Zet elke kabel in de meterkast dus achter een eigen automaat of aardlekautomaat.
- Gangbaar is per groep een kabel 3×2,5 mm² (bijv. YMvK). Een dikkere kabel (6 mm²) geeft
  geen voordeel en is stug om in de unit te leggen.

### Bronnen

- [frisianstar, 2021-11-15](https://gathering.tweakers.net/forum/list_message/69448762#69448762): 7 kW monoblock: twee voedingen (compressor, heater 3 kW); interne beveiliging beschermt de kabel niet
- [Carboy54, 2022-09-16](https://gathering.tweakers.net/forum/list_message/72804068#72804068): twee aardlekschakelaars in de unit
- [Tranquility, 2023-02-04](https://gathering.tweakers.net/forum/list_message/74362020#74362020): 5J: twee 16 A-aardlekautomaten, twee kabels 3×2,5 YMvK
- [Deismyna, 2023-09-02](https://gathering.tweakers.net/forum/list_message/76403596#76403596): 7J: 20 A voor de pomp, 16 A voor de backup heater, twee kabels 3×2,5 mm²
- [bbbrumbrum, 2024-08-03](https://gathering.tweakers.net/forum/list_message/79743334#79743334): 6 mm² geeft geen voordeel boven 2,5 mm²

## Automaten: B16, B20 of C16

De service manual van de 9L noemt 25 A voor *power supply 1* en 16 A voor de backup heater.
Met een netaansluiting van 3×25 A kiezen de meeste gebruikers lager:

| Model | Praktijk |
|---|---|
| 5 kW | B16 is ruim genoeg. |
| 7 en 9 kW | Formeel tot 17 A. Meestal gaat B16 goed; B20 geeft meer marge. |
| 9L | Toert terug bij 14,8 A en stopt met een foutcode bij 18 A (service manual). |

Een C-automaat mag. De kans dat de hoofdzekering eerder uitschakelt, is dan iets groter.
Een C-karakteristiek lost een te lage stroomwaarde niet op.

!!! note "Meningen verschillen"
    Sommigen kiezen B20 voor de compressor: stroom boven 16 A komt zelden voor, maar een B16
    zet de unit dan uit. Anderen houden B16 aan, omdat B20 dicht bij een hoofdzekering van
    25 A zit en niet selectief is. Een B20 op 2,5 mm² kan ook te hoog zijn bij een lange kabel.

### Bronnen

- [twain4me, 2022-10-06](https://gathering.tweakers.net/forum/list_message/73030708#73030708): 5 kW op B16; 7 en 9 kW tot 17 A; liever 20 A dan C
- [FransvWoerkom, 2023-11-28](https://gathering.tweakers.net/forum/list_message/77326300#77326300): C mag, hoofdzekering slaat iets eerder af
- [Tranquility, 2023-11-28](https://gathering.tweakers.net/forum/list_message/77326712#77326712): 2×C16 zonder problemen
- [ErikVers, 2024-10-11](https://gathering.tweakers.net/forum/list_message/80374756#80374756): 9L: manual 25 A / 16 A; terugtoeren bij 14,8 A, stop bij 18 A
- [Thorsd, 2024-10-12](https://gathering.tweakers.net/forum/list_message/80375484#80375484): B20 bij 3×25 A; selectiviteit en kabellengte
- [Tinkerer84, 2024-10-12](https://gathering.tweakers.net/forum/list_message/80375478#80375478): keuze 16 of 20 A hangt af van de kans op maximaal vermogen

## Aardlek

- Gebruik een aardlekautomaat of aardlekschakelaar **type A**. Type AC reageert alleen op
  sinusvormige lekstroom. Een oude type AC is ongeschikt voor de warmtepomp.
- De handleiding van de J-serie noemt voor één voeding type AC. Type A kan altijd.
- Het beste is per voeding een eigen aardlekautomaat. Deelt de warmtepomp een aardlek met
  andere groepen, dan tellen de lekstromen op. De aardlek kan dan uitschakelen terwijl er
  geen fout is. U ziet dan ook niet of het lek in de unit, de kabel of de werkschakelaar zit.
- Laat de aardlekschakelaars in de unit zitten. Bij een aardfout ziet u dan of de fout in de
  unit of in de kabel zit.
- Doet de testknop van een aardlekschakelaar in de unit niets? Dan staat er geen spanning op.

Praktijkgeval (J-serie): de aardlek in de meterkast schakelde na uren of dagen uit. Achter die
aardlek zaten ook drie lichtgroepen. Een eigen aardlekautomaat voor de warmtepomp loste het op.

### Bronnen

- [FransvWoerkom, 2022-02-16](https://gathering.tweakers.net/forum/list_message/70618924#70618924): type A en AC; interne RCCB's laten zitten; per groep aardlekautomaat type A
- [.Frank, 2022-02-16](https://gathering.tweakers.net/forum/list_message/70613368#70613368): J-handleiding noemt type AC voor één voeding
- [FransvWoerkom, 2024-02-20](https://gathering.tweakers.net/forum/list_message/78192564#78192564): eigen aardlekautomaten; oude type AC ongeschikt
- [John lamers, 2024-02-20](https://gathering.tweakers.net/forum/list_message/78193260#78193260): aardlek met lichtgroepen schakelt uit
- [John lamers, 2024-02-28](https://gathering.tweakers.net/forum/list_message/78280176#78280176): opgelost met eigen aardlekautomaat
- [Speedy-Andre, 2024-02-28](https://gathering.tweakers.net/forum/list_message/78281046#78281046): optelsom van lekstromen
- [FransvWoerkom, 2024-02-28](https://gathering.tweakers.net/forum/list_message/78282402#78282402): niet-sinusvormige lekstroom
- [Maurice1066, 2024-03-06](https://gathering.tweakers.net/forum/list_message/78358220#78358220): interne aardlekschakelaars laten zitten
- [FransvWoerkom, 2024-12-12](https://gathering.tweakers.net/forum/list_message/81007714#81007714): testknop doet niets = geen spanning

## 1-fase unit in een 3-fase meterkast

Een 1-fase unit kunt u op twee manieren op een 3-fase kast aansluiten:

1. **Twee losse groepen**, elk met een eigen kabel 3×2,5 mm².
2. **Eén 3-fase aardlekautomaat** (16 of 20 A) op twee fasen, met één 5-aderige kabel.
   De derde fase dopt u af. In de unit lust u de nul door naar beide aardlekschakelaars;
   elke aardlekschakelaar krijgt een eigen fase. Eén nul is genoeg: bij 16 A op twee fasen
   loopt er ook 16 A door de nul. U maakt zo de hele kabel in één handeling spanningsloos.

Sluit de unit niet als 1-fase kookgroep aan op een netaansluiting van 3×25 A. Compressor
en backup heater samen vragen dan te veel van één fase.

!!! note "Meningen verschillen"
    Volgens één gebruiker moeten twee losse groepen op dezelfde fase zitten, omdat er anders
    400 V tussen de groepen staat. Anderen gebruiken juist twee fasen met een gedeelde nul,
    via een 3-fase automaat. Twee losse 1-fase groepen in één 5-aderige kabel mag volgens
    sommigen niet: wie één groep uitzet, denkt dat de unit spanningsloos is. Een ander zegt
    dat meer mag dan vaak wordt beweerd, mits u aan de voorwaarden voldoet.

### Bronnen

- [frisianstar, 2021-11-15](https://gathering.tweakers.net/forum/list_message/69448762#69448762): twee groepen op dezelfde fase (400 V-risico)
- [Thorsd, 2023-05-16](https://gathering.tweakers.net/forum/list_message/75357340#75357340): één nul volstaat bij twee fasen
- [flippy, 2023-07-10](https://gathering.tweakers.net/forum/list_message/75894388#75894388): 1-fase unit met twee groepen: 2× 3×2,5 mm²
- [Makrolon, 2024-08-03](https://gathering.tweakers.net/forum/list_message/79741466#79741466): twee groepen in één kabel mag niet; krachtgroep met gesplitste nul kan
- [blb4, 2024-08-03](https://gathering.tweakers.net/forum/list_message/79743002#79743002): er mag meer dan vaak gezegd wordt
- [nMad, 2025-01-03](https://gathering.tweakers.net/forum/list_message/81198676#81198676): 3-fase aardlekautomaat op twee fasen, 5-aderige kabel, nul doorlussen
- [FransvWoerkom, 2025-01-03](https://gathering.tweakers.net/forum/list_message/81203108#81203108): derde fase afdoppen; niet als kookgroep op 1 fase

## T-CAP en andere 3-fase units

Een 3-fase T-CAP heeft twee 3-fase voedingen: één voor de unit en één voor de backup heater.
Gangbaar zijn twee 3-fase aardlekautomaten van 16 A en twee 5-aderige kabels.

- In het installateursmenu kiest u een backup heater van 3, 6 of 9 kW.
- Volgens het schema van de MXC12H9E8 gebruikt de heater L1 en L2 alleen bij 6 en 9 kW.
  De detectie zit op L3. Sluit toch alle drie de fasen aan; de kabel trekt u toch al.
- *Power supply 1* van de T-CAP kan ook op een 16 A-aardlekautomaat.

### Bronnen

- [FransvWoerkom, 2022-01-13](https://gathering.tweakers.net/forum/list_message/70207402#70207402): T-CAP 12 kW: 16 A voor PS1, 3/6/9 kW instelbaar, L1/L2 alleen bij 6/9 kW
- [flippy, 2022-01-12](https://gathering.tweakers.net/forum/list_message/70201950#70201950): detectie op L3; sluit alle drie de fasen aan
- [FransvWoerkom, 2023-06-15](https://gathering.tweakers.net/forum/list_message/75653868#75653868): T-CAP: twee groepen 3×16 A, twee 5-aderige kabels

## Werkschakelaar

Een werkschakelaar staat bij de unit. Zo kan wie aan de unit werkt de spanning zelf uitzetten.
Bij de meterkast voegt hij niets toe.

- Bij onderhoud zetten veel gebruikers de groepen in de meterkast uit en de twee
  aardlekschakelaars in de unit.
- Twee fasen van één 3-fase automaat mogen samen door één 3- of 4-polige werkschakelaar.
  Beide fasen gaan dan samen uit.
- Per groep loopt maximaal 16 A. Kies de werkschakelaar daarop.
- Bekende storing: een draad die niet goed vastzit in een buitenwerkschakelaar, samen met
  vocht. Dat geeft uitval van de unit of `H90`.

!!! warning "Spanning via de thermostaat"
    Een extern gevoede thermostaat op `CN2` kan 230 V op de print zetten, ook als de groepen
    en werkschakelaars uit staan. Zie [Kamerthermostaat](../settings.md#kamerthermostaat).

!!! note "Meningen verschillen"
    Volgens sommigen is een werkschakelaar officieel verplicht, met slot in de uit-stand.
    Anderen zeggen dat de NEN 1010 hem niet verplicht en dat een automaat als lastscheider
    mag dienen. Ook een stopcontact tot 16 A kan als lastscheider dienen.

### Bronnen

- [davevleugel, 2022-09-16](https://gathering.tweakers.net/forum/list_message/72805020#72805020): officieel een afsluitbare werkschakelaar
- [Jojan265, 2022-11-11](https://gathering.tweakers.net/forum/list_message/73434488#73434488): NEN 1010 verplicht geen werkschakelaar
- [Murkmans, 2022-11-12](https://gathering.tweakers.net/forum/list_message/73436516#73436516): groepen mechanisch samen schakelen; stopcontact als lastscheider
- [Jojan265, 2022-11-12](https://gathering.tweakers.net/forum/list_message/73437386#73437386): twee fasen in één werkschakelaar mag
- [ErikVers, 2022-11-16](https://gathering.tweakers.net/forum/list_message/73493170#73493170): 230 V via thermostaat op de print
- [bbbrumbrum, 2023-02-05](https://gathering.tweakers.net/forum/list_message/74367182#74367182): werkschakelaar hoort bij het apparaat
- [FransvWoerkom, 2023-06-15](https://gathering.tweakers.net/forum/list_message/75653868#75653868): bij onderhoud groepen en interne aardlekken uit
- [FransvWoerkom, 2023-11-24](https://gathering.tweakers.net/forum/list_message/77292642#77292642): losse schroef en vocht in werkschakelaar, `H90`
- [Thorsd, 2024-02-19](https://gathering.tweakers.net/forum/list_message/78190312#78190312): vocht in buitenwerkschakelaar
- [hemertje, 2025-01-03](https://gathering.tweakers.net/forum/list_message/81196484#81196484): maximaal 16 A per groep

## Afstandsbediening en HeishaMon

- De afstandsbediening (controller) gebruikt een 2-aderige zwakstroomkabel, bijv.
  2×0,75 mm². Een UTP-kabel werkt ook, in de praktijk tot 25 m.
- Leg bij voorkeur een kabel met extra aders (bijv. 4×0,8 mm²). Dan kunt u later een
  thermostaat of sensor aansluiten.
- HeishaMon gaat op `CN-CNT`, de plek van de CZ-TAW1. HeishaMon wordt geleverd met een
  5-polig kabeltje. Zie de [HeishaMon-documentatie](https://github.com/Egyras/HeishaMon).

### Bronnen

- [ErikVers, 2022-11-22](https://gathering.tweakers.net/forum/list_message/73563530#73563530): 4×0,8 mm² voor later
- [CurlyMo, 2022-11-22](https://gathering.tweakers.net/forum/list_message/73563360#73563360): controller op 2-aderig zwakstroom
- [The-Source, 2022-11-23](https://gathering.tweakers.net/forum/list_message/73564620#73564620): UTP werkt tot 25 m
- [CurlyMo, 2023-02-20](https://gathering.tweakers.net/forum/list_message/74521646#74521646): 5-polige stekker zit bij HeishaMon
- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart: HeishaMon op `CN-CNT`
- [Deismyna, 2023-09-02](https://gathering.tweakers.net/forum/list_message/76403596#76403596): 7J: controller op 2×0,75 mm²

## Driewegklep en andere uitgangen op de print

- Een driewegklep heeft drie draden: open-dicht-nul, of open (of dicht)-nul-fase. Op de
  print schakelt 230 V tussen `O` en `C`. Gebruik kabel met isolatie voor 230 V.
- WH-MDC07J3E5: de klep gaat op `CN1`-4/5/6. Gebruik geen geel-groene ader voor iets anders
  dan aarde.
- De handleiding (J-serie) noemt 1,5 mm² en maximaal 9,8 W voor de klepuitgang. Twee kleppen
  op één uitgang mogen samen niet boven 9,8 W komen.
- Kies een klep die standaard open of dicht is (NO/NC) zoals u hem nodig hebt. Draden
  omwisselen werkt niet: veel kleppen gebruiken de waterstroom om te sluiten.
- Een droogkookbeveiliging van de SWW-tank gaat op `CN6`-1/2, anders een draadbrug.
  Zie [`H91`](../troubleshooting.md#heaters-h70-h91).
- Aquarea M standalone (SDC0316M9E8): op `CN3` zit een schakelcontact voor een ketel of een
  ontdooiklep.

**Klep schakelt niet (9J).** Maak de draden los en start de klep via *actuator check* in het
servicemenu. Meet op de print tussen `N` en `O` en tussen `N` en `C`. Meet u 0 V, terwijl de
tweewegklepuitgang ernaast wel 230 V geeft? Dan zit de fout in het relais (`RY-V3`), de
schroefklemmen of de print.

### Bronnen

- [FransvWoerkom, 2022-11-29](https://gathering.tweakers.net/forum/list_message/73627274#73627274): MDC07J3E5: klep op `CN1`-4/5/6; geel-groen alleen voor aarde
- [FransvWoerkom, 2023-08-01](https://gathering.tweakers.net/forum/list_message/76101190#76101190): drie draden; isolatie voor 230 V
- [Pejdref, 2023-08-02](https://gathering.tweakers.net/forum/list_message/76107334#76107334): handleiding: 1,5 mm², maximaal 9,8 W
- [.Frank, 2023-08-06](https://gathering.tweakers.net/forum/list_message/76141556#76141556): twee kleppen samen onder 9,8 W
- [flippy, 2023-08-06](https://gathering.tweakers.net/forum/list_message/76141662#76141662): NO/NC kiezen; omdraaien werkt niet
- [FransvWoerkom, 2023-06-19](https://gathering.tweakers.net/forum/list_message/75696494#75696494): droogkookbeveiliging op `CN6`-1/2 of draadbrug
- [Tinkerer84, 2023-10-05](https://gathering.tweakers.net/forum/list_message/76738982#76738982): 9J: 0 V op klepuitgang, 230 V op tweewegklep
- [Thorsd, 2023-10-05](https://gathering.tweakers.net/forum/list_message/76739208#76739208): relais `RY-V3` of schroefklemmen
- [blb4, 2023-10-04](https://gathering.tweakers.net/forum/list_message/76731410#76731410): 230 V schakelt tussen `O` en `C`
- [FransvWoerkom, 2026-02-05](https://gathering.tweakers.net/forum/list_message/84575740#84575740): M standalone: `CN3` voor ketel of ontdooiklep
