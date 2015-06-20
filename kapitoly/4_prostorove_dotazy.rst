=================
Prostorové dotazy
=================

Připojujeme se do databáze z QGIS
---------------------------------

Přístup do databáze umožnuje zásuvný modul QGISu :program:`DB
Manager` (Správce databází).

.. note:: Tento zásuvný modul je součástí základní instalace a je
	  dostupný automaticky.

.. _db-manager:

DB Manager spustíme z menu aplikace QGIS.

.. figure:: ../images/qgis-db-manager-menu.png
            :width: 350px

V dialogu vybereme testovací databázi *gismentors*.

.. figure:: ../images/qgis-db-manager-priv.png
            :width: 700px

            Uživatel ``skoleni`` má právo v databázi vytvářet vlastní schémata.

Můžeme procházet metadata jednotlivých vrstev uložených v geodatabázi.

.. figure:: ../images/qgis-db-manager-layer.png
            :width: 700px

            Uživatel ``skoleni`` má pro vrstvu `obce_polygon` ve
            schématu *ruian* veškerá práva a data může případně
            modifikovat.

Provádíme SQL dotazy
--------------------

Otevřeme dialog pro :doc:`SQL dotazy <3_jazyk_sql>`.

.. figure:: ../images/qgis-db-manager-sql-toolbar.png
   :width: 200px

Tento dialog umožnuje provádět jednoduché SQL dotazy.

.. figure:: ../images/qgis-db-manager-sql-window.png
   :class: middle
   :scale-latex: 60
              
   Příklad určení počtu obcí v ČR

.. tip:: Pokročilejší uživatele ocení spíše konzolový nástroj
         :program:`psql`. Více k tomuto tématu ve školení
         :skoleni:`PostGIS pro pokročilé <postgis-pokrocily>`.

Vytváříme novou vrstvu jako výsledek prostorového dotazu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Na základě prostorového dotazu můžeme pomocí dialogu :program:`správce
databází` vytvářet nové datové vrstvy.

V nasledujícím příkladě vybereme :fignote:`(1)` obce
(:dbtable:`ruian.obce_polygon`), které obsahují alespoň jednu pořární
stanici (:dbtable:`osm.pozarni_stanice`). Výsledek zobrazíme v QGISu
jako novou vrstvu :map:`obce_pozarni_stanice` :fignote:`(2)`.

.. note:: 

   .. code-block:: sql
                   
      SELECT o.* FROM ruian.obce_polygon AS o JOIN osm.pozarni_stanice AS p
       ON ST_Within(p.geom, o.geom);

   Dotaz vracím obce, ve kterých je více než jedna požární stanice,
   jako duplicitní. Správně by tento dotaz mohl vypadat
   např. následovně:

   .. code-block:: sql

      SELECT row_number() over() id, o.* FROM ruian.obce_polygon AS o WHERE EXISTS
      (
       SELECT 1 FROM osm.pozarni_stanice AS p WHERE ST_Within(p.geom, o.geom)
      );

   Kvůli QGISu přidáme ještě nově vytvořený sloupec :dbcolumn:`id` s
   jednoznačným číselným identifikátorem.

.. figure:: ../images/qgis-query-new-layer.png

.. note:: Alternativně můžete novou vrsvu vytvořit v databázi rovnou
          jako novou tabulku anebo pohled a zobrazit v QGISu standardní cestou.

          .. code-block:: sql

             -- nejprve vytvoříme vlastní schéma
             CREATE SCHEMA uzivatel;
             
             CREATE VIEW uzivatel.obce_pozarni_stanice AS
             SELECT o.* FROM ruian.obce_polygon AS o WHERE EXISTS
             (
              SELECT 1 FROM osm.pozarni_stanice AS p WHERE ST_Within(p.geom, o.geom)
             );
          
.. figure:: ../images/qgis-query-new-layer-disp.png
   :class: large
   :scale-latex: 70
              
   Výsledek prostorového dotazu

Alternativní přístup z PgAdmin
------------------------------

Přidáme nové spojení.

.. figure:: ../images/pgadmin-new-conn-toolbar.png
   :class: small
	    
V následujícím dialogu vyplníme parametry připojení k databázi.

.. figure:: ../images/pgadmin-new-conn-dialog.png
   :width: 400px
   :scale-latex: 40

.. raw:: latex

   \newpage
                          
Připojení se přidá do seznamu.

.. figure:: ../images/pgadmin-new-conn.png
   :class: small

Otevřeme SQL okno, do kterého budeme moci posléze psát SQL dotazy.

.. figure:: ../images/pgadmin-sql-window-toolbar.png

.. figure:: ../images/pgadmin-sql-window.png
   :class: middle

   Příklad určení počtu obcí v ČR
