---
tags: [Installatie, Veiligheid, J-serie, T-CAP]
---

# Plaatsing en installatie

Een Panasonic Aquarea monoblock kunt u zelf installeren. Alle koeltechniek zit in de
buitenunit. U sluit alleen water en stroom aan. Deze pagina gaat over plaatsing, fundering,
dooiwater, wateraansluitingen, expansievat, vorst, vullen en isolatie.

Voor leidingmaten, filters, lucht en druk in het algemeen, zie
[Hydrauliek](../../general/hydraulics.md). Voor flowstoringen na de eerste start, zie
[Storingen en foutcodes](../troubleshooting.md).

**Zie ook:** [Ontdooien](../../general/defrost.md) · [Buffervat](../../general/buffer-tank.md) ·
[Instellingen](../settings.md) · [Bekabeling](wiring.md) · [Modellen](../index.md)

!!! warning "Split en bibloc: koelleidingen alleen door een gecertificeerd installateur"
    Bij een split of bibloc loopt koudemiddel tussen binnen- en buitenunit. Aansluiten,
    vacuüm trekken en vullen van die leidingen is werk onder de F-gassenregels. Doe dit niet
    zelf. Een gecertificeerd (STEK-)monteur doet dit. De rest (plaatsen, water, stroom) kunt u
    wel zelf voorbereiden. Een monoblock heeft dit probleem niet, maar het water buiten kan
    bevriezen (zie [Vorst en stroomuitval](#vorst-en-stroomuitval)).

### Bronnen

- [twain4me, 2022-03-02](https://gathering.tweakers.net/forum/list_message/70792870#70792870): monoblock zelf te installeren maar bevriezingsgevaar; split vraagt STEK-diploma
- [flippy, 2023-09-13](https://gathering.tweakers.net/forum/list_message/76511676#76511676): vacuüm trekken is koeltechnisch werk onder F-gassen
- [ijhas, 2022-02-01](https://gathering.tweakers.net/forum/list_message/70448818#70448818): split zelf geplaatst; koelleidingen door een aircomonteur aangesloten

## Plek en vrije ruimte

De algemene regels voor luchtstroom, omkasting, dak en wind staan bij
[Ontdooien: plaatsing](../../general/defrost.md#plaatsing-luchtstroom-en-omkasting).
Voor Panasonic komt daar bij:

- **Ruimte achter de unit.** Houd ruimte voor de luchttoevoer, de leidingen, de buigstraal
  van de flexslangen en onderhoud. In de praktijk houden
  gebruikers 250 tot 300 mm aan.
- **Gewicht.** Een unit met water en steunen weegt ongeveer 100 kg. Houd daar rekening mee
  bij plaatsing op een dak.

!!! note "Meningen verschillen"
    - Volgens de handleiding van de J-serie is 100 mm aan de achterkant genoeg.
    - De oudere design manual (H-serie) noemt 300 mm. Gebruikers vinden 100 mm te krap voor
      leidingen en onderhoud.
    - 250–300 mm is volgens een leverancier genoeg, omdat er ook lucht van onderen komt.

### Bronnen

- [FransvWoerkom, 2022-04-04](https://gathering.tweakers.net/forum/list_message/71144068#71144068): minimaal 300 mm aan de achterkant
- [Carboy54, 2022-04-04](https://gathering.tweakers.net/forum/list_message/71144616#71144616): 25–30 cm is genoeg; toevoer ook van onderen
- [twain4me, 2022-04-04](https://gathering.tweakers.net/forum/list_message/71145618#71145618): J-serie 100 mm, toch 300 mm aanhouden voor leidingen
- [davevleugel, 2022-04-04](https://gathering.tweakers.net/forum/list_message/71147754#71147754): 100 mm in handleiding J, 300 mm in design manual (H); 250 mm voor buigstraal flex
- [davevleugel, 2022-03-07](https://gathering.tweakers.net/forum/list_message/70854712#70854712): 100 mm te weinig voor onderhoud
- [ErikVers, 2021-02-11](https://gathering.tweakers.net/forum/list_message/66118272#66118272): unit met water en steunen ongeveer 100 kg

## Fundering

- **Twee betonbanden haaks op de unit.** De handleiding toont twee blokken onder de unit
  (30 × 15 × 60 cm). Veel gebruikers leggen twee opsluitbanden of betonbanden van 60–80 cm
  dwars onder de unit.
- **Gebruik de buitenste montagegaten.** De compressorkant (rechts) is veel zwaarder dan
  links. Steunpunten verder naar binnen maken de unit instabiel.
- **Bouten.** De gaten in de voeten zijn 13 mm. Maximaal M12 past.
- **Waterpas en hoogte.** Met draadeind en moeren op bigfoots stelt u de unit waterpas en
  staat hij vrij boven het grind. Dat helpt ook bij het dooiwater.

!!! note "Meningen verschillen"
    - **Demping.** Bigfoots, rubber of veren onder de unit beperken trillingen en geluid.
    - **Massa.** Veren en dempers zijn niet nodig. Bout de unit vast op zwaar beton
      (ongeveer 100 kg), zodat hij niet kan bewegen.

### Bronnen

- [Bra-Jo, 2022-10-03](https://gathering.tweakers.net/forum/list_message/72993702#72993702): handleiding: twee betonblokken 30 × 15 × 60
- [LinuZZ, 2022-08-26](https://gathering.tweakers.net/forum/list_message/72557010#72557010): opsluitbanden haaks op de unit, zoals de handleiding
- [Carboy54, 2022-08-27](https://gathering.tweakers.net/forum/list_message/72565948#72565948): betonbanden 60–80 cm; buitenste gaten; rechterkant zwaarder
- [Motorfret, 2022-05-03](https://gathering.tweakers.net/forum/list_message/71409346#71409346): gaten 13 mm, maximaal M12
- [CurlyMo, 2022-10-03](https://gathering.tweakers.net/forum/list_message/72993772#72993772): bigfoots met draadeind, waterpas stellen, grindbak
- [sjimmie, 2022-03-07](https://gathering.tweakers.net/forum/list_message/70853776#70853776): beton voor stabiliteit; grind en demping aanbevolen
- [reneeke1970, 2021-02-08](https://gathering.tweakers.net/forum/list_message/66068190#66068190): massa werkt tegen trillingen, veren onnodig

## Dooiwater en condens

Net als een koelkast loost de buitenunit condens- en dooiwater. Bij een ontdooicyclus komt
er veel water uit de hele bodemplaat (*base pan*), ook uit de gaten helemaal links.

- **Grindbed.** Gebruikelijk is 40–50 cm grind onder en naast de unit. Maak het bed breder
  dan de unit. Anders loopt een deel van het water over de tegels en bevriest het.
- **Afvoer.** Zonder afvoer groeit er bij vorst een plaat ijs. Strooien met zout helpt
  tijdelijk, maar is geen oplossing.
- **Rubberdoppen.** De meegeleverde doppen voor de gaten in de bodemplaat horen bij een
  bodemplaatverwarming met één open afvoer. Gaten dichtmaken zonder die verwarming geeft
  kans op ijs in de bodemplaat.

!!! note "Afvoer onder een binnenunit (all-in-one, bibloc)"
    Onder sommige binnenunits zit een extra afvoeropening. Wat die doet, is niet duidelijk.
    Panasonic noemde hem een waterafvoer en adviseerde aansluiten op het riool (K-serie).
    Een installateur noemt het een aftappunt om de tank te legen. Bij een L-serie bibloc
    schrijft Panasonic een 17 mm slang voor, geïsoleerd als er condens kan ontstaan (koelen).
    Een gebruiker met een split T-CAP ziet er geen water uit komen.

### Bronnen

- [FransvWoerkom, 2021-12-19](https://gathering.tweakers.net/forum/list_message/69913684#69913684): condens- en dooiwater, anders een ijsbaan
- [blb4, 2023-02-04](https://gathering.tweakers.net/forum/list_message/74362114#74362114): grindbed 40–50 cm
- [hnq, 2023-04-30](https://gathering.tweakers.net/forum/list_message/75204856#75204856): water van de hele verdamper; grindbak te krap
- [blb4, 2023-04-30](https://gathering.tweakers.net/forum/list_message/75205776#75205776): water uit alle gaten in de base pan; rubberdoppen alleen met base pan heater
- [twain4me, 2022-05-03](https://gathering.tweakers.net/forum/list_message/71411014#71411014): grind tussen opsluitbanden; plaat ijs; zout tijdelijk
- [kjoosten, 2023-10-16](https://gathering.tweakers.net/forum/list_message/76853968#76853968): Panasonic: afvoer H op riool
- [ErikVers, 2023-10-31](https://gathering.tweakers.net/forum/list_message/77027640#77027640): afvoer is een aftapkraan voor de tank
- [Jeroenrobbins, 2025-01-16](https://gathering.tweakers.net/forum/list_message/81332636#81332636): L-serie bibloc: 17 mm slang, geïsoleerd
- [BiLLY_daKid, 2023-10-16](https://gathering.tweakers.net/forum/list_message/76854886#76854886): split T-CAP: geen water uit afvoer H

## Wateraansluitingen

De monoblock heeft voor aanvoer en retour 5/4" (1¼") **buitendraad**. Een 1"-fitting past
niet.

- **RVS-flexslang.** Sluit de unit aan met een RVS-flexslang. Die vangt trillingen op en
  maakt aansluiten makkelijker. Een slang met nominaal 1" en een 5/4"-wartel aan de kant van
  de warmtepomp is gebruikelijk.
- **Overgang naar de leiding binnen.** Fittingen in 5/4" zijn duur en slecht leverbaar.
  Opties: een stalen perssok 5/4" × 28 mm, of een 5/4"-knelpuntstuk met een verloopbus. Elke
  extra draadverbinding is een extra kans op lekken.
- **Draad afdichten.** Loctite 55 is een eenvoudig alternatief voor hennep en teflontape.
- **Filter en kranen.** Zet een afsluiter voor en na het vuilfilter en een in de aanvoer.
  Zorg dat u het filter makkelijk kunt legen; anders doet u het niet. Meer over filters staat
  bij [Hydrauliek: water](../../general/hydraulics.md#water-filter-lucht-druk-en-spoelen).
- **Zand.** Dop de buizen af tot u ze aansluit.
- Blijft de oude cv-ketel in het circuit? Zie
  [Hydrauliek: bypass](../../general/hydraulics.md#bypass-en-overstort).

!!! note "Meningen verschillen"
    - Gebruik binnen liever meerlaagse buis of Hep2O, en houd de omvlochten slang buiten.
    - Flexslang tot binnen is makkelijker voor doe-het-zelvers, maar lastig als u wilt koelen.

### Bronnen

- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart, *Koppelingen* en *Lek dichting*: 5/4" buitendraad, RVS-flex, Loctite 55
- [flippy, 2022-01-31](https://gathering.tweakers.net/forum/list_message/70430756#70430756): 1¼" op de buitenunit, adapter naar 1" nodig
- [twain4me, 2022-01-31](https://gathering.tweakers.net/forum/list_message/70430766#70430766): 5/4", 1" past niet
- [Thorsd, 2023-07-27](https://gathering.tweakers.net/forum/list_message/76046320#76046320): wartel 5/4" aan de WP, slang nominaal 1"
- [Diedo70, 2022-11-09](https://gathering.tweakers.net/forum/list_message/73403836#73403836): 1" RVS-flex, dan Hep2O 28 mm
- [marcop23, 2023-09-03](https://gathering.tweakers.net/forum/list_message/76412730#76412730): 5/4"-fittingen duur; stalen perssok 5/4" × 28
- [Boxbal, 2023-09-05](https://gathering.tweakers.net/forum/list_message/76433398#76433398): knelpuntstuk en verloopbus; dubbel afdichten, één lekte
- [FransvWoerkom, 2022-07-26](https://gathering.tweakers.net/forum/list_message/72251000#72251000): afsluiters rond vuilafscheider en in aanvoer; buizen afdoppen
- [twain4me, 2022-07-26](https://gathering.tweakers.net/forum/list_message/72247430#72247430): voorkeur meerlaagse buis; vuilafscheider goed te legen
- [Carboy54, 2022-07-26](https://gathering.tweakers.net/forum/list_message/72247876#72247876): flexslang makkelijk voor doe-het-zelf, problematisch bij koelen

## Expansievat en waterinhoud

In de monoblock zit een expansievat van 6 L. Volgens de handleiding is dat genoeg voor
150 L systeeminhoud (1-fase) of 200 L (3-fase). Hoe u de waterinhoud uitrekent, staat bij
[Hydrauliek: druk](../../general/hydraulics.md#druk).

- **Die grens geldt voor radiatortemperaturen.** Vloerverwarming wordt hooguit ongeveer
  35 °C. Het water zet dan veel minder uit. Ook met iets meer dan 150 L is een extra vat dan
  vaak niet nodig.
- **Zelf uitrekenen.** De Panasonic design manual (2018), paragraaf 5.3.5 *Expansion
  Vessel*, geeft de berekening.
- **Extra vat.** U kunt het overal in het circuit plaatsen, bijv. op zolder. Trek de 6 L van
  het interne vat af van wat u nodig hebt. Een gebruiker noemt een voordruk van 0,5 bar
  bovenin en 1 bar beneden, maar is niet zeker. Controleer dit voor uw situatie.
- **Hoogte.** Boven ongeveer 7–9 m hoogteverschil vraagt Panasonic volgens gebruikers een
  extra vat. Controleer de grens in de handleiding van uw model.
- **Verwarming in het vat.** Het interne vat heeft een elektrisch element tegen bevriezing.
  Sommige leveranciers kunnen het interne vat verwijderen.
- **Minimale inhoud.** De design manual noemt voor de J-serie tot 9 kW een minimale
  systeeminhoud van 30 L. Zie [Buffervat](../../general/buffer-tank.md).

!!! note "Meningen verschillen"
    Voor de grootte van een extra vat noemen gebruikers twee vuistregels: 10 % van de
    waterinhoud (cv) of 4 % (warmtepomp, volgens warmtepomp-weetjes).

### Bronnen

- [ConQuestador, 2022-12-01](https://gathering.tweakers.net/forum/list_message/73656038#73656038): handleiding: 150 L (1-fase), 200 L (3-fase)
- [Separator, 2023-08-28](https://gathering.tweakers.net/forum/list_message/76351062#76351062): expansievat 6 L voor 150 L
- [FransvWoerkom, 2022-12-02](https://gathering.tweakers.net/forum/list_message/73662164#73662164): uitzetting bij vloerverwarming; design manual 5.3.5
- [FransvWoerkom, 2024-02-04](https://gathering.tweakers.net/forum/list_message/78037134#78037134): 150 L gebaseerd op radiatortemperatuur; extra vat vaak niet nodig
- [ConQuestador, 2022-12-01](https://gathering.tweakers.net/forum/list_message/73657128#73657128): op lage temperatuur weinig uitzetting
- [blb4, 2024-02-04](https://gathering.tweakers.net/forum/list_message/78037150#78037150): plaats vrij; 10 % of 4 %; 6 L aftrekken; voordruk 0,5/1 bar
- [betaplayer, 2024-02-05](https://gathering.tweakers.net/forum/list_message/78037828#78037828): extra vat vanaf 7 of 9 m hoogte
- [flippy, 2022-03-03](https://gathering.tweakers.net/forum/list_message/70808554#70808554): andere eisen boven 7–8 m hoogteverschil
- [Thorsd, 2022-12-02](https://gathering.tweakers.net/forum/list_message/73665380#73665380): intern vat met elektrische verwarming; door leverancier verwijderd
- [hnq, 2024-01-10](https://gathering.tweakers.net/forum/list_message/77760642#77760642): minimale systeeminhoud 30 L (J tot 9 kW)

## Vorst en stroomuitval

Bij een monoblock staat water buiten. Zolang er stroom is, beschermt de vorstbeveiliging
van de warmtepomp het water: de pomp gaat draaien en zo nodig ook de compressor. Bij een lange stroomuitval in de winter kan de unit bevriezen.

- **De warmtepomp gaat soms aan na uitzetten.** Bij een T-CAP (WH-WXG12ME8) startte de
  vorstbeveiliging kort na het uitzetten, met hoge flow. Volgens een installateur houdt de
  unit zonder binnendeel de retour op 26 °C bij minder dan 4 °C buiten, en op 28 °C bij
  minder dan 0 °C. Zet de unit bij nachtvorst liever niet uit.
- **Backup heater op een aparte groep** helpt alleen als de voeding van de buitenunit
  uitvalt, niet bij een volledige stroomuitval.
- **Glycol** wordt afgeraden.

!!! warning "Bevriezing bij stroomuitval"
    Valt de stroom lang uit bij vorst, dan bevriest het water in de buitenunit en de
    buitenleidingen. Bent u thuis: schakel de stroom uit, sluit de afsluiters en draai de
    slangen los om af te tappen.

!!! note "Meningen verschillen"
    - **Risico accepteren.** Veel gebruikers plaatsen geen vorstkleppen. Een lange
      stroomstoring terwijl u niet thuis bent, is zeldzaam. Zij zorgen voor afsluiters en een
      aftappunt.
    - **Vorstkleppen** (bijv. Caleffi) zijn bij een leverancier standaard. Zij laten de unit
      leeglopen als het water te koud wordt. Ze werken alleen goed met een vulautomaat, en
      mogelijk storen ze de eigen vorstbeveiliging van Panasonic.

### Bronnen

- [Tromp.et, 2025-11-17](https://gathering.tweakers.net/forum/list_message/83955324#83955324): T-CAP WH-WXG12ME8 start na uitzetten met hoge flow
- [ErikVers, 2025-11-17](https://gathering.tweakers.net/forum/list_message/83955668#83955668): retourvoorwaarde 26 °C onder 4 °C en 28 °C onder 0 °C; niet uitzetten
- [Norwayr, 2023-11-09](https://gathering.tweakers.net/forum/list_message/77120892#77120892): backup heater op aparte groep; risico bij volledige uitval
- [Thorsd, 2023-11-09](https://gathering.tweakers.net/forum/list_message/77122120#77122120): grootste risico als u niet thuis bent; afsluiters dicht en slangen los
- [twain4me, 2020-12-20](https://gathering.tweakers.net/forum/list_message/65324014#65324014): meeste mensen nemen het risico; afsluiters en aftappunt
- [dirkdeman, 2020-12-20](https://gathering.tweakers.net/forum/list_message/65324170#65324170): gecalculeerd risico
- [Carboy54, 2022-09-13](https://gathering.tweakers.net/forum/list_message/72758358#72758358): vorstbeveiliging standaard bij installatie; glycol afgeraden
- [ErikVers, 2025-11-16](https://gathering.tweakers.net/forum/list_message/83950984#83950984): vorstkleppen vragen een vulautomaat
- [Beer070, 2025-11-15](https://gathering.tweakers.net/forum/list_message/83946556#83946556): Caleffi kan storen met interne vorstbeveiliging

## Vullen, ontluchten en eerste start

1. **Manometer.** Zet een drukmeter bij het vulpunt. Anders moet u de unit openschroeven om
   de druk te zien.
2. **Automatische ontluchter openen.** Draai het dopje van de ontluchter boven in de unit een
   hele slag open, zoals de handleiding zegt.
3. **Vullen.** Vul het systeem en ontlucht de radiatoren. De handleiding vraagt minimaal
   0,5 bar. Druk en hoogte: zie [Hydrauliek: druk](../../general/hydraulics.md#druk).
4. **Ontluchtingsprogramma (*air purge*).** Laat het minstens 15 minuten draaien. Lucht in de
   backup heater geeft anders `H70`. De pomp draait dan op hoge flow (gemeld: 47 l/min) en
   stopt na ongeveer een kwartier vanzelf. Vul water bij als de druk zakt.
5. **Na elke keer bijvullen** opnieuw het ontluchtingsprogramma draaien.
6. **Controleer de instellingen**: kalibratie van de sensoren en de maximale pompflow per
   model. Zie [Instellingen](../settings.md).

Krijgt u `H62` of `H20`? Zie [Storingen en foutcodes](../troubleshooting.md).

!!! note "Meningen verschillen"
    - Laat de automatische ontluchter open staan.
    - Druppelt hij na een paar dagen nog, dan mag hij dicht. Ontlucht dan af en toe op het
      hoogste punt en bij het filter. Druppelen komt vaak door lucht die nog in het systeem
      zit.

### Bronnen

- [Erwin94, 2023-01-22](https://gathering.tweakers.net/forum/list_message/74222506#74222506): drukmeter bij vulopening vergeten; unit openschroeven
- [Baxke, 2023-10-29](https://gathering.tweakers.net/forum/list_message/76997248#76997248): handleiding: ontluchter een hele slag open (J-serie 5 kW)
- [Cr3ator, 2024-09-24](https://gathering.tweakers.net/forum/list_message/80213698#80213698): handleiding: waterdruk > 0,5 bar, stand air purge valve
- [Phyc, 2022-12-02](https://gathering.tweakers.net/forum/list_message/73664976#73664976): minstens 15 min air purge tegen `H70`
- [wheli, 2025-01-05](https://gathering.tweakers.net/forum/list_message/81213762#81213762): air purge tot 47 l/min, stopt na een kwartier; altijd na bijvullen
- [ErikVers, 2024-01-07](https://gathering.tweakers.net/forum/list_message/77716512#77716512): bij inbedrijfstelling sensoren kalibreren en max pompflow controleren
- [blb4, 2023-10-29](https://gathering.tweakers.net/forum/list_message/76998190#76998190): ontluchter niet dichtdraaien
- [ErikVers, 2023-10-29](https://gathering.tweakers.net/forum/list_message/76998854#76998854): blijft hij druppelen, dan sluiten; elders ontluchten
- [FransvWoerkom, 2023-09-02](https://gathering.tweakers.net/forum/list_message/76405700#76405700): druppelen door resterende lucht

## Leidingen naar binnen en isolatie

- **Doorvoer.** Eén 110 mm mantelbuis past net voor twee flexslangen en de kabels, zonder
  isolatie. Met isolatie hebt u meer ruimte nodig. Twee 32 mm buizen met 20 mm isolatie
  passen elk door een 100 mm pvc-buis met bochten van 45°. Zo loopt er geen regenwater naar
  de kruipruimte.
- **Muur.** Vul de doorvoer met waterdicht PUR. Een muurdoorvoerplaat voor aircoleidingen
  maakt het netjes en weerbestendig.
- **Buiten.** Gebruik Armaflex zonder plaknaad; een plaknaad laat na een paar jaar los. Een
  gespleten mantelbuis eromheen beschermt de isolatie. Leg de naad naar onder, zodat er geen
  water in blijft staan.
- **Koppelingen buiten** hoeft u niet te isoleren. Het verlies is klein naast de
  ongeïsoleerde binnenkant van de unit.
- **Kruipruimte.** Gewone schuimisolatie van 15 mm volstaat voor verwarming. Wilt u koelen,
  dan worden de leidingen nat van condens. Kies dan geen staal.

### Bronnen

- [blb4, 2023-02-04](https://gathering.tweakers.net/forum/list_message/74362114#74362114): 110 mm mantelbuis past zonder isolatie
- [Erwin94, 2023-01-22](https://gathering.tweakers.net/forum/list_message/74222506#74222506): 32 mm met 20 mm isolatie door 100 mm pvc met bochten van 45°
- [flippy, 2022-02-14](https://gathering.tweakers.net/forum/list_message/70598382#70598382): PUR in de muur, doorvoerplaat, Armaflex zonder naad, mantelbuis met naad onder
- [FransvWoerkom, 2022-11-26](https://gathering.tweakers.net/forum/list_message/73601350#73601350): Armaflex buiten; koppelingen buiten isoleren overbodig
- [FransvWoerkom, 2022-07-26](https://gathering.tweakers.net/forum/list_message/72251000#72251000): 15 mm schuim in de kruipruimte, geen druppels
- [natural colour, 2022-07-26](https://gathering.tweakers.net/forum/list_message/72247878#72247878): bij koelen worden leidingen nat; geen staal
