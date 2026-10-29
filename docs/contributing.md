---
title: Bijdragen
weight: 50
---

1. Zoek de forumberichten die uw wijziging onderbouwen.
2. Schrijf of wijzig een pagina in `docs/`:
    - `docs/general/` als het voor elke warmtepomp geldt.
    - `docs/<merk>/` als het afhangt van merk, model of firmware.
3. Schrijf de kennis in uw eigen woorden. Vat samen wat de berichten leren; herhaal de berichten niet.
4. Zet de bronnen onderaan de pagina of onderaan een sectie, onder `## Bronnen`:

    ```markdown
    ## Bronnen

    - [<auteur>, <JJJJ-MM-DD>](https://gathering.tweakers.net/forum/list_message/<id>#<id>): <wat het bericht onderbouwt>
    ```

5. Zet `title` en `weight` in de front matter. `weight` bepaalt de volgorde (10, 20, …).
   Voeg alleen tags toe uit `TAGS` in `src/wp_wiki/__init__.py`.
6. Voer `inv ci` uit. Dit moet slagen.
7. Open een pull request.

Regels:

- Schrijf in het Nederlands. Gebruik korte zinnen en de actieve vorm.
- Laat namen van MQTT-topics, parameters en foutcodes ongewijzigd (bijv. `SetZ1HeatRequestTemperature`, `H62`).
- Zijn berichten het oneens? Toon beide standpunten en noem beide bronnen.
- Hangt iets af van model, firmware of HeishaMon-versie? Vermeld welke.
- Voeg niets toe dat geen bericht onderbouwt.
