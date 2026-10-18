---
tags: [Optimalisatie, Installatie]
---

# Koelen

Een lucht-waterwarmtepomp kan in de zomer ook koud water maken. Dat water loopt door
hetzelfde afgiftesysteem als in de winter: vloerverwarming, radiatoren, convectoren of
fancoils. De grens is het dauwpunt. Onder het dauwpunt condenseert vocht uit de lucht op
koude leidingen, vloeren en radiatoren.

**Zie ook:** [Hydrauliek](hydraulics.md) · [Pendelen](cycling.md) ·
[Panasonic: instellingen](../panasonic/settings.md) · [COP en meten](cop.md)

## Dauwpunt en condensatie

- **Regel:** een oppervlak dat kouder is dan het dauwpunt wordt nat. Dat geldt voor leidingen,
  verdelers, radiatoren en de vloer.
- **Dauwpunt bepalen.** Reken het uit met de kamertemperatuur en de relatieve vochtigheid (RV),
  bijv. met de [dauwpuntcalculator van weerschip.nl](https://www.weerschip.nl/calc_Td.php).
  Voorbeeld: 24 °C en 80 % RV geeft een dauwpunt van ongeveer 20,3 °C.
- **Binnen ≈ buiten.** Bij gewone ventilatie is het dauwpunt binnen gelijk aan dat buiten.
  U vindt het bij het dichtstbijzijnde weerstation of via een weersensor in uw domotica.
- **Het dauwpunt wisselt sterk.** In de zomer zijn binnen dauwpunten van 14–16 °C gemeld, maar
  ook 19,5 en 22 °C na een regenbui. Dan is koelen via vloer of radiatoren bijna niet meer mogelijk.
- **Vuistregel 18 °C.** Daarom koelt men met een gewoon verwarmingssysteem meestal niet onder
  18 °C aanvoer. Bij warm en vochtig weer is ook dat soms al te koud.

### Bronnen

- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart, *Koelen met de warmtepomp*: condensatie, niet onder 18 °C
- [Bra-Jo, 2022-09-13](https://gathering.tweakers.net/forum/list_message/72761502#72761502): dauwpunt berekenen, voorbeeld 24 °C en 80 %
- [FransvWoerkom, 2026-06-20](https://gathering.tweakers.net/forum/list_message/85528544#85528544): dauwpunt binnen = buiten, 22 °C na wolkbreuk
- [vandermark, 2026-06-20](https://gathering.tweakers.net/forum/list_message/85527224#85527224): dauwpunt binnen 19,5 °C, koelen niet meer mogelijk
- [Draakje5, 2026-06-21](https://gathering.tweakers.net/forum/list_message/85532790#85532790): dauwpunt vaak rond 16 °C
- [martijn v o, 2023-06-11](https://gathering.tweakers.net/forum/list_message/75606274#75606274): dauwpunt 14,9 °C bij 22,3 °C binnen

## Koelen per afgiftesysteem

| Afgifte | Aanvoer onder dauwpunt? | Let op |
|---|---|---|
| Radiatoren, convectoren | Nee | Condens ontstaat hier het eerst. Werkt alleen met ventilatoren. |
| Vloerverwarming | Kort, als de vloer zelf boven het dauwpunt blijft | Volg retour- en vloertemperatuur |
| Fancoils met condensafvoer | Ja | Ontvochtigen de lucht; alle leidingen dampdicht isoleren |

### Vloer

- De aanvoer mag iets onder het dauwpunt liggen. Het gaat om de temperatuur van het
  vloeroppervlak. Voorbeeld: dauwpunt 16 °C, water 14 °C in en 18 °C uit, gemiddeld 16 °C.
- Houd de retourtemperatuur en de vloertemperatuur in de gaten. Is de vloer even koud als het
  dauwpunt, dan bent u te laat en staan er plassen.
- Condens komt traag: na enkele uren tot pas na één of twee dagen, eerst boven de
  aanvoerleidingen.
- Een koele vloer haalt geen vocht uit de lucht. Bij een lange warme periode stijgt de RV in huis.
  Het dauwpunt stijgt mee en de vloer wordt steeds eerder nat.
- Een ventilator die over de vloer blaast, helpt.
- Sluit de badkamergroep af tijdens koelen. Een betegelde badkamer is vochtig en de vloer droogt
  slecht. Dit kan met een klep die bij koelen sluit.
- Wees voorzichtig met een houten vloer. Onweer of extra gasten verhogen de RV snel. Een natte
  betonvloer drogen kan een dag duren.

### Radiatoren en convectoren

- Een radiator geeft af door luchtstroming. Die stroming komt van het temperatuurverschil met de
  kamer. Bij koelen is dat verschil klein. Koude lucht blijft onderaan hangen.
- Zonder ventilatoren koelen ze bijna niet. Gebruik grote typen (T33, T22, dubbele convectoren) en
  veel luchtstroom. Dit heet *light cooling*: koelen boven het dauwpunt.
- Stalen radiatoren en een RVS-verdeler condenseren snel. Sluit ze af of kies een kunststof verdeler.

### Fancoils

- Met condensafvoer mag het water onder het dauwpunt. Dat geeft veel meer koelvermogen.
- Een fancoil ontvochtigt ook. Een werkwijze: koel met de vloer; stijgt de RV, sluit dan de vloer
  en koel een tijd met de fancoils op zeer koud water (bijv. 7 °C). Daarna kan de vloer weer
  enkele dagen koelen.
- Condenserend koelen vraagt dat alle leidingen naar de fancoils dampdicht geïsoleerd zijn.

### Bronnen

- [FransvWoerkom, 2025-06-21](https://gathering.tweakers.net/forum/list_message/82739486#82739486): radiatoren boven dauwpunt, fancoils eronder, vloer boven dauwpunt houden
- [Draakje5, 2025-06-21](https://gathering.tweakers.net/forum/list_message/82739708#82739708): vloer na enkele uren nat bij 10 °C water
- [FransvWoerkom, 2026-06-20](https://gathering.tweakers.net/forum/list_message/85528742#85528742): vloertemperatuur gelijk aan dauwpunt is te laat
- [FransvWoerkom, 2026-07-15](https://gathering.tweakers.net/forum/list_message/85716272#85716272): condens eerst bij radiatoren; retour bewaken bij vloer
- [martijn v o, 2023-06-11](https://gathering.tweakers.net/forum/list_message/75606274#75606274): vloeroppervlak telt, voorbeeld 14/18 °C, ventilator over de vloer
- [martijn v o, 2026-06-21](https://gathering.tweakers.net/forum/list_message/85537056#85537056): condens na 1–2 dagen, RV stijgt, ontvochtigen met fancoils op 7 °C
- [vandermark, 2021-06-19](https://gathering.tweakers.net/forum/list_message/67756744#67756744): geen vloerkoeling in betegelde badkamer
- [FransvWoerkom, 2022-07-19](https://gathering.tweakers.net/forum/list_message/72179670#72179670): klep om badkamergroep uit te sluiten of fancoil in te schakelen
- [t.oswald, 2022-06-14](https://gathering.tweakers.net/forum/list_message/71829926#71829926): risico houten vloer, drogen duurt een dag
- [FransvWoerkom, 2021-06-06](https://gathering.tweakers.net/forum/list_message/67604510#67604510): radiator werkt op luchtstroom, ventilatoren helpen
- [FransvWoerkom, 2022-08-14](https://gathering.tweakers.net/forum/list_message/72431416#72431416): convectoren zonder ventilator: kou blijft onderaan
- [blb4, 2023-09-10](https://gathering.tweakers.net/forum/list_message/76474716#76474716): T33/T22 met ventilatoren, light cooling; onder dauwpunt alleen met condensafvoer en isolatie
- [Beekforel, 2023-06-10](https://gathering.tweakers.net/forum/list_message/75598278#75598278): RVS-verdeler condenseert snel
- [flippy, 2022-01-25](https://gathering.tweakers.net/forum/list_message/70364122#70364122): kunststof verdeler, radiator dicht, leidingen isoleren
- [Fr33z, 2022-09-07](https://gathering.tweakers.net/forum/list_message/72685282#72685282): stalen radiatoren afsluiten bij koelen

## Leidingen isoleren

- **Dampdicht.** Isoleer koude leidingen met Armaflex of een gelijkwaardig dampdicht materiaal.
  Gewone harde buisisolatie uit de bouwmarkt isoleert veel slechter.
- **Geen enkele kier.** Lijm of tape alle naden, ook bij de beugels. Door een kier komt vocht
  bij de koude leiding.
- **Koppelingen.** Platen Armaflex met de bijbehorende lijm passen ook om brede koppelingen.
  Zwachtel daarna af met tape.
- **In de grond.** Isoleer ook in een mantelbuis dampdicht. Er kan water in de buis staan.
  Alternatief: een kant-en-klare geïsoleerde grondleiding.

!!! note "Meningen verschillen"
    Volgens één gebruiker verkopen sommige winkels isolatie die op Armaflex lijkt, maar niet
    dampdicht is. Een ander wijst erop dat dit Tubolit is, ook van fabrikant Armacell.
    Controleer dus of het product dampdicht is.

### Bronnen

- [natural colour, 2023-09-15](https://gathering.tweakers.net/forum/list_message/76524414#76524414): dampdicht isoleren, geen kier, niet elke lookalike is dampdicht
- [FransvWoerkom, 2023-09-15](https://gathering.tweakers.net/forum/list_message/76526706#76526706): Armaflex en Tubolit zijn merken van Armacell
- [dof, 2023-07-05](https://gathering.tweakers.net/forum/list_message/75852800#75852800): platen Armaflex met lijm, koppelingen apart, afzwachtelen; harde isolatie slechter
- [The Lord, 2022-06-14](https://gathering.tweakers.net/forum/list_message/71833522#71833522): dampdicht bij koelen en in mantelbuis
- [twain4me, 2022-06-14](https://gathering.tweakers.net/forum/list_message/71829504#71829504): alle leidingen dampdicht isoleren

## Hoeveel koeling u kunt verwachten

- **Vloer:** ongeveer 20 W/m². Gemeld: 19 W/m² bij 120 m² en 3,1 kW bij 100 m²
  (water 14,2 °C in, 17,3 °C uit, EER 5,4). Bij verwarmen is dat veel meer.
- **Convectoren met ventilatoren:** zeven grote convectoren konden het minimale vermogen van de
  warmtepomp kwijt bij 14 °C. Door condens lukt in de praktijk maar 16–18 °C. De warmtepomp
  draait dan ongeveer één keer per uur 30 minuten.
- **Radiatoren met ventilatoren:** het water koelt snel af, de compressor stopt en daarna pompt
  hij lang rond. Reken op [pendelen](cycling.md).
- **Verbruik:** een 7 kW-warmtepomp verbruikte van juni tot september 170 kWh voor koelen.
  De woonkamer werd niet warmer dan 22 °C.
- **Afgifte is de grens, niet de buitenunit.** Het water moet warmte uit de kamer opnemen.
  Kijk naar de retourtemperatuur. Is die snel gelijk aan de aanvoer, dan neemt het water geen
  warmte meer op en stopt de compressor.

!!! note "Meningen verschillen"
    - **Weinig effect.** Vloerkoeling geeft hooguit ongeveer 2 °C onder de buitentemperatuur.
      Vloerverwarming werkt vooral met straling en "koudestraling bestaat niet".
      Een kamer met radiatoren krijgt u zonder fancoils niet koel.
    - **Wel comfort.** Op een koele vloer raakt uw lichaam zijn warmtestraling makkelijker kwijt.
      De vloer neemt ook warmte op van warmere vlakken. Wonderen zijn er niet, maar het is
      comfortabel. Na twee weken afwezigheid werd een huis snel leefbaar door de vloer te koelen.

### Bronnen

- [martijn v o, 2026-06-21](https://gathering.tweakers.net/forum/list_message/85537056#85537056): vloer ongeveer 20 W/m²
- [sailor_dg, 2022-08-15](https://gathering.tweakers.net/forum/list_message/72435780#72435780): 19 W/m² bij 120 m², huis snel leefbaar
- [martijn v o, 2023-06-11](https://gathering.tweakers.net/forum/list_message/75606274#75606274): 3,1 kW bij 100 m², EER 5,42
- [blb4, 2026-07-15](https://gathering.tweakers.net/forum/list_message/85717754#85717754): convectoren met ventilatoren, 14 °C haalbaar, praktijk 16–18 °C
- [wessy, 2023-06-11](https://gathering.tweakers.net/forum/list_message/75605076#75605076): radiatoren met ventilatoren pendelen
- [natural colour, 2022-09-24](https://gathering.tweakers.net/forum/list_message/72898084#72898084): 170 kWh koelen juni–september
- [FransvWoerkom, 2026-06-19](https://gathering.tweakers.net/forum/list_message/85523946#85523946): opname in de kamer is de grens, niet de buitenunit
- [FransvWoerkom, 2026-06-20](https://gathering.tweakers.net/forum/list_message/85532142#85532142): retourtemperatuur bekijken
- [t.oswald, 2021-05-17](https://gathering.tweakers.net/forum/list_message/67334420#67334420): vloer hooguit 2 °C onder buiten
- [FransvWoerkom, 2022-07-19](https://gathering.tweakers.net/forum/list_message/72179670#72179670): straling, geen koudestraling
- [bartvl, 2022-07-19](https://gathering.tweakers.net/forum/list_message/72182384#72182384): koele vloer geeft toch comfort
- [t.oswald, 2022-06-14](https://gathering.tweakers.net/forum/list_message/71829926#71829926): radiatoren zonder fancoils niet koel

## Instellen en bewaken

- **Vaste aanvoertemperatuur.** De meeste gebruikers koelen met een vaste watertemperatuur,
  niet met een stooklijn. Zij controleren zelf of er condens ontstaat.
- **Laag en lang.** Laat de warmtepomp lang op laag vermogen draaien, niet kort en hard.
  Meer flow geeft meer koelvermogen, maar kost pompenergie.
- **Koel overdag.** Geef koelen alleen vrij in de uren met de meeste warmte, bijv. 11:00–15:00.
- **Condensbewaking.** Een condensvoeler op de leiding of een zelfbouwschakeling
  (twee temperatuursensoren, een vochtsensor en een relais) kan de koelvraag onderbreken als
  de leiding kouder wordt dan het dauwpunt.

!!! note "Meningen verschillen"
    Over de ΔT tussen aanvoer en retour bij koelen:

    - **Kleine ΔT** (2–3 °C) en maximaal pompen.
    - **Grotere ΔT** (4–5 °C). Dan pompt de warmtepomp minder en kan hij langer op laag vermogen
      draaien.

### Bronnen

- [FransvWoerkom, 2026-07-15](https://gathering.tweakers.net/forum/list_message/85716272#85716272): vaste aanvoertemperatuur, condens zelf bewaken
- [martijn v o, 2026-06-21](https://gathering.tweakers.net/forum/list_message/85537056#85537056): laag en lang; ΔT 4; meer flow is minder efficiënt
- [ErikVers, 2026-05-27](https://gathering.tweakers.net/forum/list_message/85358314#85358314): ΔT 5, koelen alleen 11:00–15:00 vrijgeven
- [flippy, 2023-06-10](https://gathering.tweakers.net/forum/list_message/75599222#75599222): ΔT 2–3 en maximaal pompen
- [FransvWoerkom, 2022-04-13](https://gathering.tweakers.net/forum/list_message/71232116#71232116): kant-en-klare condensvoelers
- [Ep Woody, 2022-04-13](https://gathering.tweakers.net/forum/list_message/71230188#71230188): ESP met sensoren en relais

## Alternatieven

- **Nachtventilatie.** 's Nachts ramen open of de ventilatie hoog is effectiever en goedkoper dan
  koelen met de warmtepomp.
- **Airco of fancoil.** Een lucht-luchtwarmtepomp (airco) koelt sneller, ontvochtigt en kan in
  voor- en najaar snel bijverwarmen. Vooral op de bovenverdieping helpt dit: daar zit de warmte,
  terwijl de vloerverwarming beneden ligt.

### Bronnen

- [FransvWoerkom, 2026-07-15](https://gathering.tweakers.net/forum/list_message/85716272#85716272): nachtventilatie effectiever
- [FransvWoerkom, 2026-06-20](https://gathering.tweakers.net/forum/list_message/85528742#85528742): ramen open of aircoil met condensafvoer
- [t.oswald, 2022-06-14](https://gathering.tweakers.net/forum/list_message/71829926#71829926): verwarmen met water, koelen met lucht
- [ErikVers, 2026-05-27](https://gathering.tweakers.net/forum/list_message/85358314#85358314): airco op zolder, warmte zit boven
