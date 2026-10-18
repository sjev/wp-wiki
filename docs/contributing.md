# Bijdragen

1. Zoek de forumberichten die uw wijziging onderbouwen.
2. Schrijf of wijzig een pagina in `docs/`:
    - `docs/general/` als het voor elke warmtepomp geldt.
    - `docs/<merk>/` als het afhangt van merk, model of firmware.
3. Geef bij elke bewering een voetnoot met een link naar het bericht:

    ```markdown
    <bewering uit het bericht>.[^<bericht-id>]

    [^<bericht-id>]: [<auteur>, <JJJJ-MM-DD>](https://gathering.tweakers.net/forum/list_message/<bericht-id>#<bericht-id>)
    ```

4. Voer `inv build` uit. Dit moet slagen zonder waarschuwingen.
5. Open een pull request.

Regels:

- Schrijf in het Nederlands. Gebruik korte zinnen en de actieve vorm.
- Laat namen van MQTT-topics, parameters en foutcodes ongewijzigd (bijv. `SetZ1HeatRequestTemperature`, `H62`).
- Eén voetnoot per bronbericht. Gebruik het bericht-ID als label.
- Zijn berichten het oneens? Toon beide standpunten en citeer beide.
- Hangt een bewering af van model, firmware of HeishaMon-versie? Vermeld welke.
- Voeg geen beweringen toe die geen bericht onderbouwt.
