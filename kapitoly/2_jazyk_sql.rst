Jazyk SQL
=========

DML a DDL
---------

Jak to funguje v praxi?
-----------------------

Dejme tomu, že chcete zjistit, které muchomůrky jsou vhodné k jídlu. Přijdete do knihovny a zepáte se:
::

   Dobrý den, slečno, prosímvás, 
   podívala byste se mi do Smotlachova atlasu hub a
   zjistila,
   které muchomůrky jsou jedlé?

Slečna půjde, vytáhne z regálu smotlachu, podívá se do rejstříku a najde všechny muchomůrky, každou nalistuje a zjistí, které jsou jedlé. Ty pro Vás vypíše.

V relační databázi by to vypadalo nějak takto.

Máme **tabulku** nazvanou *smotlacha_atlas_hub*. Vypadá nějak takto.

.. table::
   :class: border

   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+
   | rod        | druh    |  rod_lat | druh_lat  | popis | foto        | jedla | vyskyt_lokalita    | vyskyt_od | vyskyt_do |
   +============+=========+==========+===========+=======+=============+=======+====================+===========+===========+
   | muchomůrka | růžovka | amanita  | rubescens | ...   | ruzovka.jpg | true  | MULTIPOLYGON(((... | 1.6       | 31.10     |
   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+
   |            |         |          |           |       |             |       |                    |           |           |
   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+
   |            |         |          |           |       |             |       |                    |           |           |
   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+
   |            |         |          |           |       |             |       |                    |           |           |
   +------------+---------+----------+-----------+-------+-------------+-------+--------------------+-----------+-----------+

Dotaz potom bude vypadat:

.. code-block:: sql

   SELECT 
      rod
      , druh
      , foto
   FROM smotlacha_atlas_hub
   WHERE
      rod = 'muchomůrka'
      AND jedla = true;
      
Tedy, v překladu do češtiny:
::

   VYBER
      seznam požadovaných údajů 
   Z tabulky
   [PRO KTERÉ PLATÍ 
      podmínka]

A co prostorová databáze?
^^^^^^^^^^^^^^^^^^^^^^^^^

Dejme tomu, že nás zajímají jen ty houby, které rostou v okruhu třiceti kilometrů od Pece pod Sněžkou, kde hodláme strávit dovolenou.

V takovém případě slečna musí porovnat místo výskytu s vámi zadanou lokalitou.

.. noteadvanced:: Je zjevné, že k požadovanému výsledku se může slečna dobrat různými, různě efektivními způsoby. Postup, kterým bude pracovat se nazývá `prováděcí plán`. K volbě ideálního způsobu slouží statistiky, které si databáze ukládá a které jsou aktualizovány po každém dotazu.

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
      AND ST_Distance(vyskyt_lokalita, '5514;POINT(-641455 -987918)'::geometry);
