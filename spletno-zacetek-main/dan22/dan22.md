# Dan 22

## Kaj je HTML?

HTML (HyperText Markup Language) je označevalni jezik za izdelavo spletnih strani. Določa strukturo vsebine.

[HTML living standard](https://html.spec.whatwg.org/multipage/)

HTML uporablja elemente (tags) za označevanje vsebine.

Primer osnovnega elementa:

```html
<p>To je odstavek.</p>
```

Struktura elementa:

```html
<imeElementa atribut="vrednost">Vsebina</imeElementa>
```

Primer z atributom:

```html
<a href="https://example.com">Povezava</a>
```

Kratek vzorec dokumenta s katerim bomo delali.

```html
<!doctype html>
<html lang=sl>
<head>
<meta charset=utf-8>
<title>Naslov</title>
</head>

<body>

</body>
</html>
```

## Validacija

Najbolj poznan [w3 validator](https://validator.w3.org/)

## Najpogostejši HTML elementi

Priporočam, da pogledete podrobneje elemente na [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)

## Primeri

### Primer 001: a

Element `<a>` ustvari hiperpovezavo. Lahko povezuje na zunanje strani, notranje strani, e-pošto ali omogoča prenos datotek. Atributi vključujejo `href` (URL ali e-pošta), `download` (za prenos), `target` (kjer odpreti povezavo, npr. `_blank`), `rel` (odnos do povezane strani, npr. `noopener`).

```html
<p><a href="https://example.com">Zunanja povezava</a></p>
<p><a href="notranja.html">Notranja povezava</a></p>
<p><a href="mailto:test@example.com">E-pošta</a></p>
<p><a href="datoteka.pdf" download>Prenos datoteke</a></p>
```

### Primer 002: abbr

Element `<abbr>` označuje kratico ali okrajšavo. Atribut `title` vsebuje polno obliko kratico, ki se prikaže ob hoverju. Nima drugih specifičnih atributov.

```html
<p><abbr title="Akademsko in raziskovalno mrežo Slovenije">ARNES</abbr> sodeluje z nacionalnimi izobraževalnimi in raziskovalnimi omrežji drugih držav.</p>
```

### Primer 003: b

Element `<b>` poudari besedilo brez posebnega pomena, npr. ključne besede. Ne doda pomena, samo vizualno poudarjanje. Nima specifičnih atributov.

```html
<p>To je <b>podebljan tekst</b> brez posebnega pomena.</p>
```

### Primer 004: bdi

Element `<bdi>` izolira besedilo z drugačno smerjo pisanja (npr. arabsko). Preprečuje, da bi drugačna smer pisanja vplivala na okolico. Nima specifičnih atributov.

```html
<p>Uporabnik <bdi>إيان</bdi> je prispeval k projektu.</p>
```

### Primer 005: bdo

Element `<bdo>` preglasi smer pisanja besedila. Atribut `dir` je obvezen in določa smer: `ltr` (levo-desno) ali `rtl` (desno-levo).

```html
<p><bdo dir="rtl">Ta besedilo je obrnjen</bdo></p>
```

### Primer 006: br

Element `<br>` ustvari prelom vrstice v besedilu. Uporablja se za naslove ali naslove. Nima atributov ali vsebine.

```html
<p>Naslov:<br>Glavna ulica 123<br>Mesto, Država</p>
```

### Primer 007: cite

Element `<cite>` označuje naslov dela, kot knjiga ali film. Uporablja se za citiranje virov. Nima specifičnih atributov.

```html
<p>Kot pravi <cite>Veliki Gatsby</cite> ...</p>
```

### Primer 008: code

Element `<code>` označuje del kode v besedilu. Uporablja se za prikaz kode v stavkih. Nima specifičnih atributov.

```html
<p>Uporabi <code>console.log()</code> za odpravljanje napak.</p>
```

### Primer 009: data

Element `<data>` povezuje človeško berljivo besedilo z strojno berljivimi podatki. Atribut `value` vsebuje strojno berljivo vrednost (npr. številko).

```html
<p>Vrednost je <data value="123">sto triindvajset</data>.</p>
```

### Primer 010: dfn

Element `<dfn>` označuje definicijo termina. Prvi pojav termina v dokumentu. Nima specifičnih atributov.

```html
<p><dfn>HTML</dfn> je jezik za označevanje vsebine.</p>
```

### Primer 011: em

Element `<em>` poudari besedilo z naglasom. Uporablja se za poudarjanje pomena. Nima specifičnih atributov.

```html
<p>Res <em>pomembno</em> mislim to.</p>
```

### Primer 012: i

Element `<i>` označuje besedilo z drugačnim glasom ali razpoloženjem, npr. tuje besede. Nima specifičnih atributov.

```html
<p>Izraz <i>homo sapiens</i> je latinski.</p>
```

### Primer 013: kbd

Element `<kbd>` označuje uporabniški vnos, npr. tipke na tipkovnici. Nima specifičnih atributov.

```html
<p>Pritisni <kbd>Ctrl+C</kbd> za kopiranje.</p>
```

### Primer 014: mark

Element `<mark>` označuje označeno ali poudarjeno besedilo. Nima specifičnih atributov.

```html
<p>To je <mark>označen</mark> tekst.</p>
```

### Primer 015: q

Element `<q>` označuje kratko citat. Brskalniki dodajo narekovaje. Atribut `cite` lahko vsebuje URL vira.

```html
<p>Kot je rekla: <q>živjo</q>.</p>
```

### Primer 016: rp

Element `<rp>` zagotavlja nadomestno besedilo za brskalnike, ki ne podpirajo ruby anotacij. Uporablja se z `<ruby>` in `<rt>`.

```html
<p><ruby>漢<rt>kan</rt><rp>(</rp>漢<rp>)</rp></ruby></p>
```

### Primer 017: rt

Element `<rt>` zagotavlja ruby tekst (izgovorjava) za vzhodnoazijske znake. Uporablja se z `<ruby>`.

```html
<p><ruby>漢<rt>kan</rt></ruby></p>
```

### Primer 018: ruby

Element `<ruby>` omogoča ruby anotacije za prikaz izgovorjave. Vsebuje besedilo in `<rt>` za anotacijo.

```html
<p><ruby>漢<rt>kan</rt></ruby></p>
```

### Primer 019: s

Element `<s>` označuje prečrtano besedilo, npr. nepravilne informacije. Nima specifičnih atributov.

```html
<p>Cena: <s>10€</s> 8€</p>
```

### Primer 020: samp

Element `<samp>` označuje vzorec izhoda programa. Nima specifičnih atributov.

```html
<p>Izhod: <samp>Pozdravljen svet</samp></p>
```

### Primer 021: small

Element `<small>` označuje stranski komentar ali opombo. Nima specifičnih atributov.

```html
<p>Pogoji <small>veljajo</small></p>
```

### Primer 022: span

Element `<span>` je generični vsebnik za besedilo. Uporablja se za stiliziranje. Nima specifičnih atributov.

```html
<p>To je <span>span</span> element.</p>
```

### Primer 023: strong

Element `<strong>` označuje pomembno besedilo. Nima specifičnih atributov.

```html
<p><strong>POMEMBNO:</strong> Preberi to.</p>
```

### Primer 024: sub

Element `<sub>` označuje indeksirano besedilo. Nima specifičnih atributov.

```html
<p>Voda H<sub>2</sub>O</p>
```

### Primer 025: sup

Element `<sup>` označuje eksponentno besedilo. Nima specifičnih atributov.

```html
<p>E=mc<sup>2</sup></p>
```

### Primer 026: time

Element `<time>` označuje datum ali čas. Atribut `datetime` vsebuje strojno berljivo obliko (npr. ISO 8601).

```html
<p>Objavljeno: <time datetime="2023-01-01">1. januar 2023</time></p>
```

### Primer 027: u

Element `<u>` označuje podčrtano besedilo. Nima specifičnih atributov.

```html
<p>To je <u>podčrtano</u> besedilo.</p>
```

### Primer 028: var

Element `<var>` označuje spremenljivko v matematičnem izrazu. Nima specifičnih atributov.

```html
<p>Spremenljivka <var>x</var> ni definirana.</p>
```

### Primer 029: wbr

Element `<wbr>` predlaga mesto za prelom besede. Nima atributov ali vsebine.

```html
<p>DolgaBeseda<wbr>Prelom</p>
```

### Primer 030: address

Element `<address>` označuje kontaktne informacije. Nima specifičnih atributov.

```html
<address>Glavna ulica 123<br>Mesto, Država</address>
```

### Primer 031: article

Element `<article>` označuje samostojno vsebino, kot članek. Nima specifičnih atributov.

```html
<article><h2>Naslov članka</h2><p>Vsebina članka</p></article>
```

### Primer 032: aside

Element `<aside>` označuje stransko vsebino. Nima specifičnih atributov.

```html
<aside><p>Povezana informacija</p></aside>
```

### Primer 033: footer

Element `<footer>` označuje nogo strani ali sekcije. Nima specifičnih atributov.

```html
<footer><p>&copy; 2026 Vse pravice pridržane</p></footer>
```

### Primer 034: header

Element `<header>` označuje glavo strani ali sekcije. Nima specifičnih atributov.

```html
<header><h1>Naslov spletne strani</h1></header>
```

### Primer 035: h1

Element `<h1>` označuje glavni naslov. Nima specifičnih atributov.

```html
<h1>Glavni naslov</h1>
```

### Primer 036: h2

Element `<h2>` označuje naslov druge ravni. Nima specifičnih atributov.

```html
<h2>Podnaslov</h2>
```

### Primer 037: h3

Element `<h3>` označuje naslov tretje ravni. Nima specifičnih atributov.

```html
<h3>Manjši podnaslov</h3>
```

### Primer 038: h4

Element `<h4>` označuje naslov četrte ravni. Nima specifičnih atributov.

```html
<h4>Nivo 4</h4>
```

### Primer 039: h5

Element `<h5>` označuje naslov pete ravni. Nima specifičnih atributov.

```html
<h5>Nivo 5</h5>
```

### Primer 040: h6

Element `<h6>` označuje naslov šeste ravni. Nima specifičnih atributov.

```html
<h6>Nivo 6</h6>
```

### Primer 041: hgroup

Element `<hgroup>` združuje naslove. Nima specifičnih atributov.

```html
<hgroup><h1>Naslov</h1><p>Podnaslov</p></hgroup>
```

### Primer 042: main

Element `<main>` označuje glavno vsebino strani. Nima specifičnih atributov.

```html
<main><p>Glavna vsebina</p></main>
```

### Primer 043: nav

Element `<nav>` označuje navigacijsko sekcijo. Nima specifičnih atributov.

```html
<nav><ul><li><a href="#">Domov</a></li></ul></nav>
```

### Primer 044: section

Element `<section>` označuje sekcijo dokumenta. Nima specifičnih atributov.

```html
<section><h2>Sekcija</h2><p>Vsebina</p></section>
```

### Primer 045: search

Element `<search>` označuje iskalno sekcijo. Nima specifičnih atributov.

```html
<form role="search"><input type="search" placeholder="Išči..."></form>
```

### Primer 046: blockquote

Element `<blockquote>` označuje dolg citat. Atribut `cite` lahko vsebuje URL vira.

```html
<blockquote cite="https://example.com">Citiran tekst</blockquote>
```

### Primer 047: dd

Element `<dd>` označuje opis v definicijskem seznamu. Nima specifičnih atributov.

```html
<dl><dt>Pojem</dt><dd>Definicija</dd></dl>
```

### Primer 048: div

Element `<div>` je generični vsebnik. Nima specifičnih atributov.

```html
<div><p>Vsebina</p></div>
```

### Primer 049: dl

Element `<dl>` označuje definicijski seznam. Nima specifičnih atributov.

```html
<dl><dt>Pojem</dt><dd>Definicija</dd></dl>
```

### Primer 050: dt

Element `<dt>` označuje termin v definicijskem seznamu. Nima specifičnih atributov.

```html
<dl><dt>Pojem</dt><dd>Definicija</dd></dl>
```

### Primer 051: figcaption

Element `<figcaption>` označuje napis pod sliko ali figuro. Nima specifičnih atributov.

```html
<figure><img src="slika.jpg" alt="Opis"><figcaption>Napis slike</figcaption></figure>
```

### Primer 052: figure

Element `<figure>` označuje sliko ali figuro z napisom. Nima specifičnih atributov.

```html
<figure><img src="slika.jpg" alt="Opis"><figcaption>Napis slike</figcaption></figure>
```

### Primer 053: hr

Element `<hr>` ustvari horizontalno črto. Nima atributov ali vsebine.

```html
<p>Pred</p><hr><p>Po</p>
```

### Primer 054: li

Element `<li>` označuje element seznama. Atribut `value` za urejene sezname.

```html
<ul><li>Element</li></ul>
```

### Primer 055: menu

Element `<menu>` označuje seznam ukazov. Nima specifičnih atributov.

```html
<menu><li>Element</li></menu>
```

### Primer 056: ol

Element `<ol>` označuje urejen seznam. Atributi: `type` (tip oštevilčevanja, npr. `1`, `a`), `start` (začetna številka), `reversed` (obrnjeno).

```html
<ol><li>Prvi</li><li>Drugi</li></ol>
```

### Primer 057: p

Element `<p>` označuje odstavek. Nima specifičnih atributov.

```html
<p>Odstavek besedila</p>
```

### Primer 058: pre

Element `<pre>` ohranja presledke in prelome vrstic. Nima specifičnih atributov.

```html
<pre>Oblikovan tekst</pre>
```

### Primer 059: ul

Element `<ul>` označuje neurejen seznam. Nima specifičnih atributov.

```html
<ul><li>Element</li></ul>
```

### Primer 060: area

Element `<area>` definira območje v slikovnem zemljevidu. Atributi: `shape` (oblika, npr. `rect`, `circle`), `coords` (koordinate), `href` (povezava), `alt` (nadomestno besedilo).

```html
<map name="mapa"><area shape="rect" coords="0,0,100,100" href="#"></map><img usemap="#mapa" src="slika.jpg">
```

### Primer 061: audio

Element `<audio>` vgradi zvočno datoteko. Atributi: `src` (vir), `controls` (prikaže kontrole), `autoplay`, `loop`, `muted`.

```html
<audio controls><source src="zvok.mp3"></audio>
```

### Primer 062: img

Element `<img>` vgradi sliko. Atributi: `src` (vir), `alt` (nadomestno besedilo), `width`, `height`, `loading` (npr. `lazy`).

```html
<img src="slika.jpg" alt="Opis slike">
```

### Primer 063: map

Element `<map>` definira slikovni zemljevid. Atribut `name` poveže z `<img>`.

```html
<map name="mapa"><area shape="rect" coords="0,0,100,100" href="#"></map><img usemap="#mapa" src="slika.jpg">
```

### Primer 064: track

Element `<track>` doda podnapise ali opise za video/avdio. Atributi: `src` (vir), `kind` (vrsta, npr. `subtitles`), `srclang` (jezik), `label`.

```html
<video><track kind="subtitles" src="napisi.vtt"></video>
```

### Primer 065: video

Element `<video>` vgradi video datoteko. Atributi: `src`, `controls`, `autoplay`, `loop`, `muted`, `width`, `height`, `poster` (sličica).

```html
<video controls><source src="video.mp4"></video>
```

### Primer 066: embed

Element `<embed>` vgradi zunanje vsebine. Atributi: `src`, `type`, `width`, `height`.

```html
<embed src="datoteka.swf" type="application/x-shockwave-flash">
```

### Primer 067: iframe

Element `<iframe>` vgradi drugo HTML stran. Atributi: `src`, `width`, `height`, `name`, `sandbox` (varnost).

### Primer 068: object

Element `<object>` vgradi zunanje vire. Atributi: `data` (vir), `type`, `width`, `height`.

### Primer 069: picture

Element `<picture>` omogoča odzivne slike. Vsebuje `<source>` in `<img>`.

### Primer 070: source

Element `<source>` določa vire za `<picture>`, `<audio>`, `<video>`. Atributi: `src`, `type`, `media` (za odzivnost).

### Primer 071: svg

Element `<svg>` vgradi SVG grafiko. Atributi: `width`, `height`, `viewBox`.

### Primer 072: math

Element `<math>` vgradi matematične izraze. Uporablja MathML.

### Primer 073: canvas

Element `<canvas>` omogoča risanje z JavaScript. Atributi: `width`, `height`.

### Primer 074: noscript

Element `<noscript>` prikaže vsebino, če JavaScript ni omogočen. Nima specifičnih atributov.

### Primer 075: script

Element `<script>` vključi JavaScript. Atributi: `src` (vir), `type` (npr. `module`), `async`, `defer`.

### Primer 076: del

Element `<del>` označuje izbrisano besedilo. Atributi: `datetime` (kdaj izbrisano), `cite` (zakaj).

### Primer 077: ins

Element `<ins>` označuje vstavljeno besedilo. Atributi: `datetime`, `cite`.

### Primer 078: caption

Element `<caption>` doda napis tabeli. Nima specifičnih atributov.

### Primer 079: col

Element `<col>` definira stolpec v tabeli. Atributi: `span` (število stolpcev).

### Primer 080: colgroup

Element `<colgroup>` združuje stolpce. Atribut `span`.

### Primer 081: table

Element `<table>` ustvari tabelo. Nima specifičnih atributov.

### Primer 082: tbody

Element `<tbody>` združuje telo tabele. Nima specifičnih atributov.

### Primer 083: td

Element `<td>` označuje celico tabele. Atributi: `colspan`, `rowspan`.

### Primer 084: tfoot

Element `<tfoot>` združuje nogo tabele. Nima specifičnih atributov.

### Primer 085: th

Element `<th>` označuje glavo celice. Atributi: `colspan`, `rowspan`, `scope` (npr. `col`, `row`).

### Primer 086: thead

Element `<thead>` združuje glavo tabele. Nima specifičnih atributov.

### Primer 087: tr

Element `<tr>` označuje vrstico tabele. Nima specifičnih atributov.

### Primer 088: button

Element `<button>` ustvari gumb. Atributi: `type` (`submit`, `reset`, `button`), `name`, `value`, `disabled`.

### Primer 089: datalist

Element `<datalist>` zagotavlja seznam možnosti za `<input>`. Atribut `id` poveže z `<input>`.

### Primer 090: fieldset

Element `<fieldset>` združuje povezane elemente obrazca. Nima specifičnih atributov.

### Primer 091: form

Element `<form>` ustvari obrazec. Atributi: `action` (URL za pošiljanje), `method` (`get`, `post`), `enctype`.

### Primer 092: input

Element `<input>` ustvari vnosno polje. Atributi: `type` (npr. `text`, `password`, `email`), `name`, `value`, `placeholder`, `required`, `disabled`.

### Primer 093: label

Element `<label>` označuje oznako za element obrazca. Atribut `for` poveže z `id` elementa.

### Primer 094: legend

Element `<legend>` doda napis za `<fieldset>`. Nima specifičnih atributov.

### Primer 095: meter

Element `<meter>` prikaže merilo. Atributi: `value`, `min`, `max`, `low`, `high`, `optimum`.

### Primer 096: optgroup

Element `<optgroup>` združuje možnosti v `<select>`. Atribut `label`.

### Primer 097: option

Element `<option>` označuje možnost v `<select>`. Atributi: `value`, `selected`.

### Primer 098: output

Element `<output>` prikaže rezultat izračuna. Atribut `for` poveže z elementi.

### Primer 099: progress

Element `<progress>` prikaže napredek. Atributi: `value`, `max`.

### Primer 100: select

Element `<select>` ustvari spustni seznam. Atributi: `name`, `multiple`, `size`.

### Primer 101: textarea

Element `<textarea>` ustvari večvrstično vnosno polje. Atributi: `name`, `rows`, `cols`, `placeholder`, `required`.

### Primer 102: details

Element `<details>` ustvari razširljivo sekcijo. Atribut `open` (začetno odprto).

### Primer 103: dialog

Ta primer prikazuje uporabo najsodobnejših HTML atributov `command` in `commandfor`. Ti omogočajo interakcijo z elementi (kot je `<dialog>`) popolnoma brez uporabe JavaScripta.

commandfor: Predstavlja povezavo do ciljnega elementa. Vrednost mora biti enaka atributu id elementa, ki ga želimo upravljati (v našem primeru moje-okno).

command: Določa dejanje, ki naj se izvede. Ukaz show-modal odpre dialog kot modalno okno, ukaz close pa ga varno zapre.

id: Edinstven identifikator na elementu `<dialog>`, ki služi kot naslov, da ga gumb sploh lahko najde v kodi.

### Primer 104: summary

Element `<summary>` zagotavlja vidno oznako za `<details>`. Nima specifičnih atributov.

## Kaj je CSS?

CSS (Cascading Style Sheets) je jezik za opisovanje predstavitve spletnih strani. Določa, kako elementi HTML izgledajo, vključno z barvami, fonti, postavitvijo in animacijami.

[CSS specifications](https://www.w3.org/Style/CSS/)

CSS uporablja pravila za stiliziranje elementov. Vsako pravilo vsebuje selektor in deklaracije.

[CSS popularnost pravil](https://chromestatus.com/metrics/css/popularity)

Primer osnovnega pravila:

```css
p {
  color: blue;
}
```

Sintaksa pravila:

```css
selektor {
  lastnost: vrednost;
}
```

Primer z več lastnostmi:

```css
h1 {
  color: red;
  font-size: 24px;
}
```

Kratek vzorec dokumenta s CSS:

```html
<!doctype html>
<html>
<head>
  <style>
    body { background-color: lightblue; }
  </style>
</head>
<body>
  <p>To je odstavek.</p>
</body>
</html>
```

## Validacija CSS

Najbolj poznan [CSS validator](https://jigsaw.w3.org/css-validator/)

## Najpogostejše CSS lastnosti

Priporočam, da pogledate podrobneje lastnosti na [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)

## Primeri CSS

### Primer 001: background

Lastnost `background` nastavi ozadje elementa.

```css
body {
  background: url('image.jpg') no-repeat center center;
}
```

### Primer 002: background-color

Lastnost `background-color` nastavi barvo ozadja.

```css
div {
  background-color: yellow;
}
```

### Primer 003: border

Lastnost `border` nastavi obrobo.

```css
img {
  border: 1px solid black;
}
```

### Primer 004: border-radius

Lastnost `border-radius` zaokroži robove.

```css
.button {
  border-radius: 5px;
}
```

### Primer 005: box-shadow

Lastnost `box-shadow` doda senco elementu.

```css
.card {
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
```

### Primer 006: box-sizing

Lastnost `box-sizing` določa, kako se izračuna velikost elementa.

```css
* {
  box-sizing: border-box;
}
```

### Primer 007: color

Lastnost `color` nastavi barvo besedila.

```css
p {
  color: #ff0000;
}
```

### Primer 008: cursor

Lastnost `cursor` nastavi obliko kazalca miške.

```css
button {
  cursor: pointer;
}
```

### Primer 009: display

Lastnost `display` določa, kako se element prikaže.

```css
.inline {
  display: inline;
}
```

### Primer 010: float

Lastnost `float` omogoča obtekanje elementov.

```css
.left {
  float: left;
}
```

### Primer 011: font-family

Lastnost `font-family` nastavi družino pisave.

```css
body {
  font-family: Arial, sans-serif;
}
```

### Primer 012: font-size

Lastnost `font-size` nastavi velikost pisave.

```css
h1 {
  font-size: 2em;
}
```

### Primer 013: font-weight

Lastnost `font-weight` nastavi debelino pisave.

```css
strong {
  font-weight: bold;
}
```

### Primer 014: height

Lastnost `height` nastavi višino elementa.

```css
.box {
  height: 200px;
}
```

### Primer 015: left

Lastnost `left` nastavi levi položaj pozicioniranega elementa.

```css
.absolute {
  position: absolute;
  left: 20px;
}
```

### Primer 016: line-height

Lastnost `line-height` nastavi višino vrstice.

```css
p {
  line-height: 1.5;
}
```

### Primer 017: margin

Lastnost `margin` nastavi zunanji odmik.

```css
p {
  margin: 10px;
}
```

### Primer 018: margin-bottom

Lastnost `margin-bottom` nastavi spodnji zunanji odmik.

```css
p {
  margin-bottom: 10px;
}
```

### Primer 019: margin-top

Lastnost `margin-top` nastavi zgornji zunanji odmik.

```css
p {
  margin-top: 15px;
}
```

### Primer 020: opacity

Lastnost `opacity` nastavi prosojnost.

```css
.overlay {
  opacity: 0.5;
}
```

### Primer 021: overflow

Lastnost `overflow` določa, kaj se zgodi z vsebino, ki preseže meje elementa.

```css
.container {
  overflow: hidden;
}
```

### Primer 022: padding

Lastnost `padding` nastavi notranji odmik.

```css
div {
  padding: 20px;
}
```

### Primer 023: position

Lastnost `position` določa metodo pozicioniranja.

```css
.absolute {
  position: absolute;
}
```

### Primer 024: right

Lastnost `right` nastavi desni položaj pozicioniranega elementa.

```css
.absolute {
  position: absolute;
  right: 10px;
}
```

### Primer 025: text-align

Lastnost `text-align` poravna besedilo.

```css
.center {
  text-align: center;
}
```

### Primer 026: text-decoration

Lastnost `text-decoration` doda dekoracijo besedilu.

```css
a {
  text-decoration: none;
}
```

### Primer 027: top

Lastnost `top` nastavi zgornji položaj pozicioniranega elementa.

```css
.absolute {
  position: absolute;
  top: 10px;
}
```

### Primer 028: transform

Lastnost `transform` transformira element.

```css
.rotate {
  transform: rotate(45deg);
}
```

### Primer 029: transition

Lastnost `transition` omogoča prehode.

```css
.button:hover {
  transition: background-color 0.3s;
}
```

### Primer 030: width

Lastnost `width` nastavi širino elementa.

```css
.container {
  width: 100%;
}
```

### Primer 031: z-index

Lastnost `z-index` določa vrstni red plasti.

```css
.modal {
  z-index: 1000;
}
```

### Primer 032: flexbox

Uporaba Flexbox za postavitev.

```css
.container {
  display: flex;
  justify-content: center;
}
```

### Primer 033: grid

Uporaba CSS Grid za postavitev.

```css
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
```

### Primer 034: media queries

Media queries za odzivni dizajn.

```css
@media (max-width: 600px) {
  .responsive {
    width: 100%;
  }
}
```

### Primer 035: selectors

Različni selektorji.

```css
/* ID selektor */
#id { color: red; }

/* Class selektor */
.class { color: blue; }

/* Element selektor */
p { color: green; }

/* Pseudo-class
https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes
*/
a:hover { color: purple; }
```

### Primer 036: animations

CSS animacije.

```css
@keyframes slide {
  from { transform: translateX(0); }
  to { transform: translateX(100px); }
}

.animate {
  animation: slide 2s infinite;
}
```

### Primer 037: variables

CSS spremenljivke.

```css
:root {
  --primary-color: blue;
}

p {
  color: var(--primary-color);
}
```

### Primer 038: calc

Funkcija calc za izračune.

```css
.container {
  width: calc(100% - 20px);
}
```

### Primer 039: gradients

Linearni gradienti.

```css
.gradient {
  background: linear-gradient(to right, red, yellow);
}
```

### Primer 040: filters

CSS filtri.

```css
.blur {
  filter: blur(5px);
}
```
