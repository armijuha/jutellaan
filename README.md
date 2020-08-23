# jutellaan
Keskustelusovellus

    Keskustelut on jaettu alueisiin, joilla on viestejä sisältäviä viestiketjuja
    Käyttäjä voi olla peruskäyttäjä tai ylläpitäjä
    Käyttäjä voi luoda tunnuksen, lähettää viestejä ja luoda uusia ketjuja
    Käyttäjä pystyy muokkaamaan viestiä ja poistamaan sen myöhemmin
    Viestejä voi etsiä hakutoiminnolla
    Keskusteluun voi luoda salaisen alueen, jolle on pääsy vain tietyillä käyttäjillä

Tilanne 9.8.
Alustavia web-sivuja voi testata osoitteessa https://keskustelusovellus.herokuapp.com/ .
Tietokantoja on tehty vasta 1 (users) joten toistaiseksi on mahdollista vain käydä eri sivuilla ja lisätä käyttäjiä sovellukseen.
En ole ponnisteluista huolimatta vieläkään saanut tietokantaa toimimaan yhteen muun koodin kanssa omalla koneella (kumpikin toimii kyllä erikseen) mutta onneksi Herokussa tämä näyttääkin yllättäen toimivan ihan hienosti joten jatkan kehitystä siltä pohjalta.

Tilanne 23.8.
Sovellusta voi testata uudessa osoitteessa: https://jutellaan.herokuapp.com/ .
Aloitettu kokonaan alusta ja tehty sovellus uuteen hakemistoon, uusi git repositio ja uusi heroku. Nyt homma toimii melko hyvin ja kaikki tarvittavat tietokannat on olemassa. Sovellukseen voi kirjautua, aloittaa uusia ketjuja ja kirjoittaa viestejä. Omalla koneella onnistuu nyt myös viestien poisto ja editointi, mutta jostain syystä se ei näytä näyttäisi toimivan herokussa. Tämän lisäksi viiemisen viikon aikana pitäisi vielä lisätä toiminnallisuus adminien ja salaiselle alueelle pääsevien käyttäjien erottelemiseksi normaalikäyttäjistä sekä parantaa ulkoasua ja käytettävyyttä jos vain aika antaa myöden.


