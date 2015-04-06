====
ÚVOD
====

Databáze
========

Kdy ukládat data do databáze?
-----------------------------

V geoinformatické praxi pracujeme se třemi typy zdrojů dat. Jednak se
jedná o data uložená v souborovém systému. Typicky může jít o data v
zastaralém, leč stále nejpoužívanějším formátu :wikipedia-en:`Esri
Shapefile`, případně :wikipedia-en:`GML <Geography Markup Language>`,
hovoříme-li o vektorových datech. Dalším typem jsou webové služby,
jmenovitě :wikipedia-en:`WFS <Web Feature Service>` (Web Feature
Service). V případě WFS si aplikace vyžádá pomocí souboru ve
značkovacím jazyce :wikipedia-en:`XML` data na vzdáleném serveru po
síti. Posledním typem uložení dat, kterému je věnováno toto školení,
je uložení dat v databázi. Většina současných databází, ať již `Open
Source` nebo ryze proprietárních podporuje v nějaké míře ukládání a
dotazování prostorových prvků.  Ať už :wikipedia:`MySQL`,
:wikipedia:`Oracle`, nebo :wikipedia:`MSSQL` a v neposlední řadě
:wikipedia:`PostgreSQL`, kterému je věnován tento kurz.

.. noteadvanced:: Hranice nemusí být vždy jednoznačná, například
   existují takzvané `souborové databáze`, tedy soubory, které se
   chovají podobným způsobem jako databázový server, ovšem bez řady
   výhod, které poskytuje plnohodnotná databáze. Na druhou stranu se s
   nimi o poznání snáze manipuluje. Příkladem může být :wikipedia:`MS
   Access` nebo :wikipedia:`SQLite` (a jeho prostorové nadstavby `OGC
   GeoPackage <http://www.geopackage.org>`_ a
   :wikipedia-en:`SpatiaLite`).

Provoz databáze přináší určité požadavky na režii, ve srovnání s 
daty v souborech. O její správu a nastavení se musí starat kvalifikovaný 
specialista, má určité nároky na hardware apod. Co nám tedy přináší a 
kdy je pro nás nezastupitelná?

V první řadě je třeba vzít v potaz objem dat. Od jistého objemu není 
možné efektivně pracovat s daty uloženými v souborech. Naproti tomu v
databázi můžeme pomocí indexů přistupovat přímo k jednotlivým záznamům
tak, jak jsou uloženy na datových stránkách.


Integrita
^^^^^^^^^

Další benefit, který nám databáze může přinést je "hlídání" `referenční
integrity`.

Referenční integrita znamená, že tabulky jsou mezi sebou provázány cizími
klíči. Tedy pokud podřízená (slave) tabulka obsahuje položku s odkazy do
jiné `nadřízené` tabulky, není možné do podřízené tabulky přidat záznam,
pokud v nadřízené tabulce neexistuje hodnota, na kterou odkazuje cizí klíč.
Nemůžeme tedy například do tabulky jednotlivých vozidel přidat vozidlo s
odkazem na typ `tříkolka`, pokud nemáme v tabulce typů vozidel typ `tříkolka`.
Nebo, jiný příklad, pokud máme tabulku staveb a parcel, při správně
nastavené referenční integritě nám databáze nedovolí vložit budovu na
neexistující parcele.

Další užitečnou vlastnosti je možnost nastavit chování podřízeného
záznamu při smazání souvisejícího záznamu v nadřízené tabulce. Můžeme
zvolit :sqlcmd:`RESTRICT` nebo :sqlcmd:`CASCADE`. V případě :sqlcmd:`CASCADE` se
související záznamy mažou, v případě :sqlcmd:`RESTRICT` není možné nadřízený
záznam smazat, dokud jsou na něj navázány záznamy v podřízených
tabulkách.

Spolupráce
^^^^^^^^^^

Není obvyklé, aby k jednomu souboru přistupovalo více klientských aplikací
zároveň, protože by si ho přepisovaly "pod rukama". Databáze je v tomhle daleko
pokročilejší a umožňuje, aby nad jednou datovou sadou mohlo pracovat množství klientů
najednou. V databázi je navíc možné nastavovat práva na zápis, čtení a manipulaci
s tabulkami, schématy, funkcemi... Podobně jako v souborovém systému.

Transakce
^^^^^^^^^

Transakčnost databáze znamená, že se série změn provede buď celá nebo vůbec.
Typický (a tím pádem pěkně otřepaný případ) je situace, kdy převádíme peníze z
účtu na účet. Tedy, nebylo by dobré, aby byly z jednoho účtu peníze odečteny, aniž by na
cílový účet byly přidány.

Seznam požadavků na transakční databázi bývá označován zkratkou `ACID`. Znamená to
`Atomic, Consistent, Isolated, Durable`. Znamená to, že transakce je nedělitelná,
před i po jejím proběhnutí musí být platná referenční integrita, transakce se navzájem
neovlivňují a změny jsou trvalé i po případné havárii databázového serveru.

Co je databáze?
================

Databázi, ať už relační nebo dokumentovou, si můžeme představit jako 
knihovnu. V knihách (tabulkách) máme nějaké informace. Informace pro nás 
vyhledávají knihovnice (obslužné programy). K tomu používají katalogy a 
rejstříky (indexy). Organizace knihovny je plně pod naší kontrolou, 
ovlivňujeme hardware (kolik bude mít budova pater (disků), kolik bude 
volných regálů a manipulačního prostoru atd.), kolik bude mít knihovna 
fyzických zaměstnanců (počet jader procesoru). Dále ovlivňujeme 
organizaci, budou knihy řazeny podle abecedy podle názvů, podle klíčových 
slov, podle jména autora? Jak často budeme aktualizovat katalogy a 
rejstříky (aktualizovat indexy)? Kolik místa vlastně na katalogy/indexy 
vyhradíme? Jak budeme nakládat s místem po vyřazených svazcích (proces 
:sqlcmd:`VACUUM`)? A tak dále. Se svými zaměstnanci komunikujeme v jazyce :doc:`SQL <2_jazyk_sql>` (pokud 
tedy hovoříme o relační databázi).

Tabulky
--------

V relační databázi ukládáme data do tabulek. Tabulka je svisle dělena na
jednotlivé sloupce (často označovány jako atributy nebo položky) a vodorovně do řádky (záznamy).
Data v jednom sloupci musí mít stejný `datový typ` (datum, celé číslo, textový řetězec).

Schémata
--------

.. todo::

Typy
----

Datové typy odpovídají typům z programovacích jazyků, základem jsou celočíselné
typy (`integer`, `bigint` apod.) a řetězce (`varchar`, `char`, `text` ...), tím ovšem výčet
zdaleka nekončí. Pro prostorovou reprezentaci používáme datový typ `geometry` nebo
`geography`. Záznamu v tabulce odpovídají kompozitní typy, celé datové struktury je
možné ukládat do `nerelačních datových typů` jako je :wikipedia:`JSON`, `hstore <http://www.postgresql.org/docs/current/static/hstore.html>`_ nebo :wikipedia:`XML`
a dalo by se dále pokračovat.

Indexy
------

Indexy v databázi slouží k co možná nejrychlejšímu dohledání 
záznamů v tabulce. Fungují na podobném principu jako rejstřík v knize. Jedná se o 
jakýsi utříděný seznam klíčů spojených s odkazem na konkrétní 
datovou stránku, na místo na pevném disku, kde je uložena požadovaná 
informace. Smyslem indexu je provést při dohledání záznamu minimum 
porovnání hodnot v indexu s požadovanou hodnotou. U neindexované tabulky 
bychom museli porovnat požadovanou hodnotu se všemi záznamy.

.. noteadvanced:: Nejčastějším typem indexu je :wikipedia-en:`B-tree`, zde jsou hodnoty 
   uloženy ve stromovité struktuře založené na dichotomickém větvení. Na 
   každém uzlu porovnáme požadovanou hodnotu s hodnotou na uzlu a zjistíme, 
   jestli je větší nebo menší. S každým patrem je síto jemější. To je 
   velice efektivní, když si uvědomíme, že při zdvojnásobení objemu dat 
   přibude jen jedno porovnání navíc. B-tree index je možné sestavit jen nad
   položkami s takovým typem dat, který je možné porovnávat pomocí operátorů
   ``<`` a ``>``. Nehodí se tedy pro data vícedimenzionální, např. prostorová data.

Omezení-constrainty
-------------------

.. todo::

Triggery
--------

.. todo::

Funkce
------

.. todo::


A co prostorová databáze?
=========================

Prostorová databáze, se podobá takové knihovně, ve které jsou kromě knih
také mapy, atlasy, globusy... Zkrátka nosiče informací, které 
zaznamenávají také umístění jednotlivých údajů.


Simple feature
==============

.. todo:: To bych klidně doplnil zítra z přednašek co mám ve škole.
