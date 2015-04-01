====
ÚVOD
====

Databáze
========

Kdy ukládat data do databáze?
-----------------------------

V geoinformatické praxi pracujeme se třemi typy zdrojů dat. Jednak se jedná 
o data uložená v souborovém systému. Typicky může jít o data v 
zastaralém, leč stále nejpoužívanějším formátu `ESRI shapefile`, 
případně `GML`, hovoříme-li o vektorových datech. Dalším typem jsou 
webové služby, jmenovitě `WFS`, tedy web feature service. V případě WFS 
si aplikace vyžádá pomocí souboru ve značkovacím jazyce `XML` vyžádá 
data na vzdáleném serveru po síti. Posledním typem uložení dat, kterému 
je věnováno následující školení, je uložení dat v databázi. Většina 
současných databází, ať již `Open Source`, nebo ryze komerčních 
podporuje v nějaké míře ukládání a dotazování prostorových prvků. 
Ať už zmíníme MySQL, Oracle, nebo MSSQL a v neposlední řadě PosgreSQL, 
kterému je věnován tento kurz.

.. noteadvanced:: Hranice nemusí být vždy jednoznačná, například 
   existují takzvané `souborové databáze`, tedy soubory, které se chovají 
   podobným způsobem jako databázový server, ovšem bez řady výhod, které 
   poskytuje plnohodnotná databáze. Na druhou stranu se s nimi o poznání 
   snáze manipuluje. Příkladem může být MS Acces *jak se to píše?*, nebo 
   SQLLite (a jeho prostorové nadstavby Geopackage a SpatialLite).

Provoz databáze přináší určité požadavky na režii, ve srovnání s 
daty v souborech. O její správu a nastavení se musí starat kvalifikovaný 
specialista, má určité nároky na hardware apod. Co nám tedy přináší a 
kdy je pro nás nezastupitelná?

Je třeba, v první řadě, vzít v potaz objem dat. Od jistého objemu není 
možné efektivně pracovat s daty uloženými v souborech.

Editace

Integrita

Spolupráce

Statická/dynamická data

Co je databáze?
^^^^^^^^^^^^^^^

Databázi, ať už relační, nebo objektovou, si můžeme představit jako 
knihovnu. V knihách (tabulkách) máme nějaké informace. Informace pro nás 
vyhledávají knihovnice (obslužné programy). K tomu používají katalogy a 
rejstříky (indexy). Organizace knihovny je plně pod naší kontrolou, 
ovlivňujeme hardware (kolik bude mít budova pater (disků), kolik bude 
volných regálů a manipulačního prostoru atd.), kolik bude mít knihovna 
fyzických zaměstnanců (počet jader procesoru). Dále ovlivňujeme 
organizaci, budou knihy řazeny podle abecedy podle názvů, podle klíčových 
slov, podle jména autora? Jak často budeme aktualizovat katalogy a 
rejstříky (aktualizovat indexy)? Kolik místa vlastně na katalogy/indexy 
vyhradíme? Jak budeme nakládat s místem po vyřazených svazcích (porces 
VACUUM)? A tak dále. Se svými zaměstnanci komunikujeme v jazyce SQL (pokud 
tedy hovoříme o relační databázi).

A co prostorová databáze?
^^^^^^^^^^^^^^^^^^^^^^^^^

Prostorová databáze, se podobá takové knihovně, ve které kromě knih jsou 
také mapy, atlasy, globusy... Zkrátka nosiče informací, které 
zaznamenávají také umístění jednotlivých údajů.

Indexy
------

Indexy v databázi slouží k co možná nejrychlejšímu dohledání 
záznamů. Fungují na podobném principu jako rejstřík v knize. Jedná se o 
jakýsi utříděný seznam klíčů spojených s odkazem na konkrétní 
datovou stránku, na místo na pevném disku, kde je uložena požadovaná 
informace. Smyslem indexu je provést při dohledání záznamu minimum 
porovnání hodnot v indexu s požadovanou hodnotou. U neindexované tabulky 
bychom museli porovnat požadovanou hodnotu se všemi záznamy.

.. noteadvanced:: Nejčastějším typem indexu je `b-tree`, zde jsou hodnoty 
uloženy ve stromovité struktuře založené na dichotmickém větvení. Na 
každém uzlu porovnáme požadovanou hodnotu s hodnotou na uzlu a zjistíme, 
jestli je větší, nebo menší. S každým patrem je síto jemější. To je 
velice efektivní, když si uvědomíme, že při zdvojnásobení objemu dat 
přibude jen jedno porovnání navíc.


Simple feature
--------------
