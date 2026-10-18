---
tags: [Optimalisatie]
---

# Stooklijn

Een stooklijn (weersafhankelijke regeling, WAR) koppelt de buitentemperatuur aan de
aanvoertemperatuur van het cv-water. Hoe kouder het buiten is, hoe warmer het water.
Een afgiftesysteem geeft meer warmte af bij warmer water. Zo past de warmtepomp de
warmte aan het warmteverlies van de woning aan.

Voor de instellingen per merk, zie [Panasonic: instellingen](../panasonic/settings.md).

**Zie ook:** [Pendelen](cycling.md) · [Hydrauliek](hydraulics.md) · [Vermogen kiezen](sizing.md)

## Hoe een stooklijn werkt

Een stooklijn is een rechte lijn tussen twee punten:

| Punt | Buitentemperatuur | Aanvoertemperatuur |
|---|---|---|
| Koud punt | bijv. −10 °C | water voor de maximale warmtevraag |
| Warm punt | bijv. 8 °C | water voor de minimale warmtevraag |

Voorbeeld: de vloer geeft 1,5 kW af bij 25 °C water en 4,5 kW bij 35 °C. Het huis verliest
1,5 kW bij 8 °C buiten en 4,5 kW bij −10 °C. De stooklijn is dan 25 °C @ 8 °C en
35 °C @ −10 °C. Bij 0 °C buiten maakt de warmtepomp 29 °C water.

Met [vscope.at](https://vscope.at/) kunt u een stooklijn tekenen en de watertemperatuur bij
elke buitentemperatuur aflezen.

### Bronnen

- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart, hoofdstuk *Stoken met een stooklijn*

## Een eerste stooklijn bepalen

1. **Afgifte bepalen.** Zoek de laagste watertemperatuur waarbij uw afgiftesysteem het
   minimale vermogen van de warmtepomp kwijt kan. Zoek ook de temperatuur voor het
   maximale vermogen.
    - Vloerverwarming: deel het vermogen door het oppervlak (W/m²). Reken de afgifte uit met
      buisdiameter, hart-op-hartafstand en vloeropbouw, bijv. met de
      [WTH-afgifteberekening](https://www.wth.nl/support-en-service/afgifte-berekening).
    - Radiatoren: tel de afgifte van alle radiatoren op bij één temperatuur. Reken daarna
      uit wat die radiatoren afgeven bij lagere watertemperaturen.
2. **Warmteverlies per graad bepalen.** Gebruik het gasverbruik per graaddag
   (bijv. van mindergas.nl): m³ per graaddag × kWh per m³ ÷ 24 uur = W per graad.
3. **De punten uitrekenen.** Ga uit van een stookgrens van 18 °C.
    - Warm punt: 18 °C − (minimaal vermogen ÷ verlies per graad).
    - Koud punt: 18 °C − (maximaal vermogen ÷ verlies per graad).

Voorbeeld: 155 W per graad, minimaal 1400 W en maximaal 4500 W. Het warme punt is
18 − 9 = 9 °C en het koude punt is 18 − 29 = −11 °C. Met een afgifte van 26 en 42 °C wordt
de eerste stooklijn 26 °C @ 9 °C en 42 °C @ −11 °C.

Kan het afgiftesysteem het vermogen alleen kwijt bij hoge watertemperaturen? Vervang dan
radiatoren of zet ventilatoren (boosters) op de radiatoren.

### Bronnen

- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart, *Een basis stooklijn bepalen* en *Minimale en maximale afgifte bepalen*

## Controleren in de praktijk

Het afgegeven vermogen volgt uit de flow en het verschil tussen aanvoer en retour (ΔT):

> vermogen (kW) = flow (l/min) ÷ 60 × ΔT × 4,18

Vuistregel: vermogen (W) ≈ 70 × ΔT × flow (l/min).
Bij 15 l/min en ΔT 2 is dat ongeveer 2,1 kW.

Let op de nauwkeurigheid. Zijn de sensoren op 1 °C nauwkeurig, dan is de fout bij 15 l/min
ongeveer 1 kW. Een warmtemeter of twee betere thermometers geeft een beter beeld.
Wijkt de gemeten afgifte af van de berekening? Pas dan de stooklijn aan.

### Bronnen

- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart, *Controleren theorie met de praktijk*
- [blb4, 2026-01-07](https://gathering.tweakers.net/forum/list_message/84358560#84358560): ΔT × flow × 70 als vuistregel

## Bijstellen

- **Stel in kleine stappen bij**, bijv. één keer per week. Te koud: hoger. Ruimte over: lager.
  Dit proces duurt een hele herfst en winter.
- **Te warm binnen?** Dan moet de stooklijn omlaag. Een lagere stooklijn geeft wel meer
  pendelen.
- **Pendelen is niet te voorkomen** als het warmteverlies kleiner is dan het minimale vermogen
  van de warmtepomp. Een iets hogere stooklijn bij milde temperaturen geeft meer afgifte en
  langere runs. De COP daalt iets, maar het verbruik is dan toch laag.
- **Vorm "\_".** Maak het warme deel vlak, op de laagste aanvoertemperatuur waarbij de
  warmtepomp zijn minimale vermogen nog kwijt kan. Het huis warmt dan zo langzaam mogelijk
  op en de kamerthermostaat schakelt zo weinig mogelijk.
- **Niet te steil.** Bij een steile lijn verandert de doeltemperatuur bij elke graad
  buitentemperatuur sterk. Als het plots kouder wordt, moet de warmtepomp dan ook veel
  harder werken, juist in het gebied met ontdooicycli.

### Bronnen

- [sjimmie, 2022-09-21](https://gathering.tweakers.net/forum/list_message/72861918#72861918): praktisch bijstellen, één keer per week
- [Pejdref, 2024-02-13](https://gathering.tweakers.net/forum/list_message/78130264#78130264): pendelen bij te klein warmteverlies; "\_"-vorm
- [Thorsd, 2024-10-16](https://gathering.tweakers.net/forum/list_message/80411206#80411206): stooklijn omhoog voor langere runs
- [Thorsd, 2024-11-29](https://gathering.tweakers.net/forum/list_message/80878966#80878966): stooklijn niet te steil
- [ercolano, 2024-03-02](https://gathering.tweakers.net/forum/list_message/78318160#78318160): vlakkere lijn, minder wisselingen in doeltemperatuur

## Nachtverlaging

!!! note "Meningen verschillen"
    - **Geen of weinig nachtverlaging.** Een warmtepomp werkt het best als hij lang draait op
      een lage temperatuur. Een flinke nachtverlaging kost in de ochtend veel vermogen.
      Een verlaging van 21 naar 19 °C van 23:00 tot 10:00 maakte het opwarmen in de ochtend
      moeilijk.
    - **Kleine nachtverlaging.** Een verlaging van ongeveer 0,7 °C van 22:00 tot 05:00
      voorkomt stoken in de koudste uren, met de meeste ontdooicycli. Er blijft genoeg tijd
      om het huis voor de ochtend op te warmen.
    - **'s Nachts uit.** Dit geeft één lange run in de ochtend. Dit is niet het zuinigst,
      maar het past bij beperkte afgifte en persoonlijke wensen.

### Bronnen

- [bartvl, 2022-08-22](https://gathering.tweakers.net/forum/list_message/72503596#72503596): lang draaien op lage temperatuur, geen flinke nachtverlaging
- [Daffy1982, 2023-11-26](https://gathering.tweakers.net/forum/list_message/77302484#77302484): opwarmen na nachtverlaging moeilijk
- [ConQuestador, 2023-11-26](https://gathering.tweakers.net/forum/list_message/77303636#77303636): kleine nachtverlaging, koudste uren overslaan
- [flippy, 2023-10-28](https://gathering.tweakers.net/forum/list_message/76988104#76988104): 's nachts uit, lange run in de ochtend
- [Thorsd, 2023-10-28](https://gathering.tweakers.net/forum/list_message/76992164#76992164): geen nachtverlaging

## Automatische correctie

Een domoticasysteem kan de stooklijn verschuiven op basis van de kamertemperatuur.
Is het te warm, bijv. door zon, houtkachel of oven, dan verlaagt het systeem de stooklijn
met een paar graden. Is het te koud, dan verhoogt het de stooklijn. Dit regelt fijner dan een
aan/uit-kamerthermostaat. Het werkt alleen als de warmtepomp nog kan afregelen: op minimaal
vermogen kan hij niet minder leveren. Gebruik in die periode een kamerthermostaat.

### Bronnen

- [twain4me, 2023-03-13](https://gathering.tweakers.net/forum/list_message/74751460#74751460): topicstart, *Automagische stooklijncorrectie*
- [natural colour, 2022-08-22](https://gathering.tweakers.net/forum/list_message/72507176#72507176): handmatig verschuiven bij zoninstraling
