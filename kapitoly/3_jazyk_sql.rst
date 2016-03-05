=========
Jazyk SQL
=========

Jazyk **SQL** je nástroj pro komunikaci uživatele s relační databází. Oproti 
programovacím jazykům je jednodušší a bližší gramatice mluvené řeči. 
Je standardizován jako :wikipedia:`SQL ANSI <SQL>`. V jazyce SQL vytváříme tzv.
`dotazy`.

SQL dotazy dělíme na dva základní typy: dotazy pro manipulaci s 
daty **DML** (:wikipedia-en:`data manipulation language <Data_manipulation_language>`) a
**DDL** (:wikipedia-en:`data definition language <Data_definition_language>`)
tedy dotazy pro definici dat. DML slouží pro manipulaci se 
záznamy v tabulkách, tedy pro vyptání dat, mazání záznamů, 
vyprazdňování tabulek, vkládání a aktualizování záznamů. DDL naopak slouží 
pro definici databázových struktur. Pro tvorbu databází, tabulek, indexů, 
pohledů, funkcí, triggerů atd. Dále rozlišujeme **DCL** a **TCL**, tedy
:wikipedia-en:`data control language <Data_control_language>` a
:wikipedia-en:`transaction control language <Transaction_Control_Language>`.
První z nich slouží k nastavení přístupových práv (příkazy :sqlcmd:`GRANT` a
:sqlcmd:`REVOKE`), druhý pak k práci s transakcemi.

.. noteadvanced:: Kromě jazyka SQL můžeme psát v PostgreSQL funkce i v
   dalších jazycích. Mimo jiné se jedná o :wikipedia:`Perl`,
   :wikipedia:`Python`, R, :wikipedia:`JavaScript` a další. Zejména
   však :pgsqlcmd:`PL/PgSQL <plpgsql>`, procedurální jazyk PostgreSQL svou syntaxí
   podobný jazyku používanému v databázích :wikipedia:`Oracle`.

Syntax
------

Základní kostra jazyka SQL vypadá zhruba následovně:
::

   PROVEĎ
   S ČÍM
   ZA JAKÝCH PODMÍNEK

Pro výběr dat z tabulky tedy:
::

   VYBER
   seznam položek
   Z tabulky
   PRO KTERÉ PLATÍ
   podmínka;

.. note:: SQL dotazy v PostgreSQL zakončujeme středníkem.

DML
---

SELECT
^^^^^^

Dotaz, kterým vybíráme data z databáze, uvozuje příkaz :pgsqlcmd:`SELECT <sql-select>` následovaný
výčtem sloupců požadovaného výstupu. Výčet sloupců může být nahrazen ``*`` pro výběr všech sloupců.
Pokud předřadíme výčtu sloupců :sqlcmd:`DISTINCT` bude dotaz vracet pouze unikátní kombinace
hodnot.  Klauzule :sqlcmd:`FROM` uvozuje výčet tabulek,
ze kterých budeme vybírat a které mohou (ale nemusí) být propojeny klauzulí :sqlcmd:`JOIN`.
Následovat může výčet podmínek uvedený klauzulí :sqlcmd:`WHERE`. Podmínky můžeme řetězit
booleovskou logikou pomocí :sqlcmd:`AND`, :sqlcmd:`OR`, případně vylučovat pomocí
:sqlcmd:`NOT`.

Nakonec můžeme použít :sqlcmd:`GROUP BY` pro sdružování při
agregacích, :sqlcmd:`ORDER BY` pro sezaření záznamů či
případně :sqlcmd:`LIMIT` a :sqlcmd:`OFFSET` pro omezení řádků výstupu,
eventuálně další, méně obvyklé klauzule.

Jak to funguje v praxi?
~~~~~~~~~~~~~~~~~~~~~~~

Dejme tomu, že chcete zjistit, které muchomůrky jsou vhodné k jídlu. 
Přijdete do knihovny a zeptáte se:
::

   Dobrý den, slečno, prosím Vás, 
   podívala byste se mi do Smotlachova atlasu hub a
   zjistila,
   které muchomůrky jsou jedlé?

Slečna půjde, vytáhne z regálu "Smotlachu", podívá se do rejstříku a 
najde všechny muchomůrky, každou nalistuje a zjistí, které jsou jedlé. Ty 
pro Vás vypíše.

V relační databázi by to vypadalo nějak takto.

Máme **tabulku** nazvanou *smotlacha_atlas_hub*. Vypadá nějak takto:

.. table::
   :class: border

   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+
   | rod        | druh    |  rod_lat | druh_lat  | popis | foto        | jedla | vyskyt_lokalita    | vyskyt_od | vyskyt_do |
   +============+=========+==========+===========+=======+=============+=======+====================+===========+===========+
   | muchomůrka | růžovka | amanita  | rubescens | ...   | ruzovka.jpg | true  | MULTIPOLYGON(((... | 1.6.      | 31.10.    |
   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+
   |            |         |          |           |       |             |       |                    |           |           |
   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+
   |            |         |          |           |       |             |       |                    |           |           |
   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+
   |            |         |          |           |       |             |       |                    |           |           |
   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+

SQL dotaz potom bude vypadat následovně:

.. code-block:: sql

   SELECT 
      rod
      , druh
      , foto
   FROM smotlacha_atlas_hub
   WHERE
      rod = 'muchomůrka'
      AND jedla = true;
      
V překladu do češtiny by dotaz mohl znít:
::

   VYBER
      seznam požadovaných údajů 
   Z tabulky
   [PRO KTERÉ PLATÍ 
      podmínka]

JOIN
^^^^

Rozlišujeme dva typy příkazu :pgsqlcmd:`JOIN
<queries-table-expressions>`, tj. spojení tabulek: :sqlcmd:`INNER
JOIN` a :sqlcmd:`OUTER JOIN`.

:sqlcmd:`INNER JOIN` vrátí pouze takové záznamy, 
kde došlo k nalezení potřebné hodnoty v obou tabulkách. Naproti tomu 
:sqlcmd:`OUTER JOIN` vrací pro jednu, případně obě tabulky všechny záznamy.
:sqlcmd:`OUTER JOIN` dělíme na :sqlcmd:`LEFT JOIN`, :sqlcmd:`RIGHT JOIN` a
:sqlcmd:`FULL JOIN`. :sqlcmd:`LEFT` a :sqlcmd:`RIGHT JOIN` vrací všechny záznamy z levé nebo
pravé tabulky. :sqlcmd:`FULL JOIN` vrátí všechny záznamy z obou tabulek.
Speciální situací je :sqlcmd:`CROSS JOIN`, který vrací kartézský součin
záznamů v obou tabulkách.

Záznamy obvykle párujeme pomocí klauzule :sqlcmd:`ON`, za kterou následují
podmínky propojení podobně jako za klauzulí :sqlcmd:`WHERE`. Alternativou
je použití klauzule :sqlcmd:`USING`, kde je uveden název sloupce, který
musí být v obou tabulkách. Další možností je :sqlcmd:`NATURAL JOIN`,
který použije stejně pojmenované sloupce. Ten však nedoporučeme příliš
používat, zvláště v databázích s proměnlivou strukturou.

.. code-block:: sql

   SELECT houby.rod || ' ' || houby.druh, lokalita.nazev, houby.vyskyt  -- vyber "rod druh", "lokalita", "vyskyt"
   FROM houby                                                           -- z tabulky houby
   JOIN lokalita ON houby.id = lokalita.houby_id                        -- spoj podle sloupečků s id houby
   WHERE ST_Intersects(                                                 -- ale pouze tam, kde lokalita je v oblasti "Vysočina"
      (
         SELECT geom FROM oblasti WHERE nazev = 'Vysočina'
      )
      , lokalita.geom)
   AND houby.vyskyt @> '2015-07-15'::timestamp;                         -- a pouze tam, kde výsky je "od"

   SELECT houby.rod || ' ' || houby.druh                    
   FROM houby
   JOIN r_recept ON r_recept.houby_id = houby.id
   JOIN recept ON recept.id = r_recept.recept_id
   WHERE recept.nazev = 'smaženice';

UPDATE
^^^^^^

:pgsqlcmd:`UPDATE <sql-update>` slouží k aktualizování hodnot vybraných
sloupců. Používá se klauzule :sqlcmd:`WHERE` a výrazy. Také je možno použít
klauzuli :sqlcmd:`FROM` a aktualizovat tabulku hodnotami z jiných tabulek.

Příklad nastavení výskýtu od 1.června pro všechny houhy z rodu "amanita":

.. code-block:: sql

   UPDATE smotlacha_atlas_hub SET vyskyt_od = '1.6.' WHERE rod_lat = 'amanita';

DELETE
^^^^^^

:pgsqlcmd:`DELETE <sql-delete>` slouží k mazání vybraných záznamů z tabulek.

Příklad odstranění všech jedlých hub z tabulky:

.. code-block:: sql

   DELETE smotlacha_atlas_hub WHERE jedla = true;

TRUNCATE
^^^^^^^^

:pgsqlcmd:`TRUNCATE <sql-truncate>` slouží k okamžitému vyprázdnění celé
tabulky. Je rychlejší, než použití :sqlcmd:`DELETE` bez podmínek.

.. code-block:: sql

   TRUNCATE smotlacha_atlas_hub;

Množinové operace
^^^^^^^^^^^^^^^^^

Množinové operace pracují s výsledky více poddotazů. Jedná se o :sqlcmd:`UNION`,
:sqlcmd:`UNION ALL`, :sqlcmd:`EXCEPT` a :sqlcmd:`INTERSECT`.

:sqlcmd:`UNION` vrací sjednocení záznamů z obou dotazů. Záznamy, které jsou výsledkem (tvz. *recordset*) obou
dotazů, jsou po sjednocení obsaženy pouze jednou. Naproti tomu :sqlcmd:`UNION ALL`
vrátí všechny záznamy, výsledkem sjednocení je tedy součet záznamů z obou recordsetů.

.. noteadvanced:: Pokud víme, že záznamy se mezi dotazy neduplikují, je lepší použít
   :sqlcmd:`UNION ALL`. Provádění pak bude efektivnější, protože si ušetříme porovnávání
   obou výstupních recordsetů.

:sqlcmd:`EXCEPT` vrací rozdíl, tedy pouze takové záznamy, které se vyskytují pouze v prvním
recordsetu. :sqlcmd:`INTERSECT` vrací průnik. Tedy záznamy, které se vyskytují v obou
recordsetech.

Poddotazy
^^^^^^^^^

V rámci dotazu můžeme dotazovat další *vnořené* dotazy uzavřené do závorek.

.. code-block:: sql

   SELECT recepty.* FROM
   (
   SELECT DISTINCT recept_id FROM r_recept WHERE houby_id IN
      (
         SELECT * FROM houby WHERE rod = 'bedla'
      )
   ) recepty_na_bedly
   JOIN recepty ON recepty.id = recepty_na_bedly.recept_id;

DDL
---

:sqlcmd:`CREATE` a :sqlcmd:`DROP` jsou základní příkazy z *Data Definition Language*.
Pomocí nich vytváříme tabulky, pohledy, omezení, funkce, typy a další.

   :pgsqlcmd:`CREATE TABLE <sql-createtable>`

   :pgsqlcmd:`CREATE VIEW <sql-createview>`

   :pgsqlcmd:`CREATE FUNCTION <sql-createfunction>`

   :pgsqlcmd:`CREATE LANGUAGE <sql-createlanguage>`

   ...



A co prostorová databáze?
-------------------------

Dejme tomu, že nás zajímají jen ty houby, které rostou v okruhu třiceti 
kilometrů od Pece pod Sněžkou, kde hodláme strávit dovolenou.

V takovém případě slečna musí porovnat místo výskytu s vámi zadanou 
lokalitou.

.. noteadvanced:: Je zjevné, že k požadovanému výsledku se může slečna
   dobrat různými, různě efektivními způsoby. Postup, kterým bude
   pracovat se nazývá `prováděcí plán` (:wikipedia-en:`query plan`). K
   volbě ideálního způsobu slouží statistiky, které si databáze ukládá
   a které jsou aktualizovány po každém dotazu.

Dotaz do SQL může potom vypadat následovně:

.. code-block:: sql

   SELECT 
      rod
      , druh
      , foto
   FROM smotlacha_atlas_hub
   WHERE
      rod = 'muchomůrka'
      AND jedla = true
      AND ST_Distance(vyskyt_lokalita,
      '5514;POINT(-641455 -987918)'::geometry) < 3e4;
