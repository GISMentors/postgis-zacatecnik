Začínáme
========

Na úvod si ukážeme přístup k datům uložených v databázi z prostředí
:program:`QGIS`.

Zobrazujeme data v QGIS
-----------------------

.. _qgis-add-pg-layer:

Vektorová data uložená v geodatabázi PostGIS je možné načíst buď z *menu*

.. figure:: ../images/qgis-add-pg-vector-menu.png

anebo z *nástrojové lišty* aplikace QGIS. Další možností je použít
:ref:`datový katalog <DataCatalog>`.

.. figure:: ../images/qgis-add-pg-vector-toolbar.png
	    :width: 150px

V dialogu nejprve nadefinujeme parametry připojení k databázi.

.. figure:: ../images/qgis-postgis-new.png

Nastavíme:

* název spojení :fignote:`(1)`
* hostitel (adresa serveru, pokud je to localhost, nemusíme vyplňovat) :fignote:`(2)`
* databáze, ke které se chceme připojit :fignote:`(3)`
* uživatelské jméno a heslo pro připojení k databázi :fignote:`(4)`

.. figure:: ../images/qgis-postgis-new-settings.png
           :width: 350px

Pro opětovné připojení je vhodné si uživatelské jméno a popřípadě i
heslo (v tomto případě bude heslo uloženo na lokálním disku v textovém
souboru!) uložit :fignote:`(5)`

.. figure:: ../images/qgis-pg-conn-warning.png
	    :class: small

Nastavení připojení k databázi nejprve otestujeme :fignote:`(6)` a
poté potvrdíme.

.. figure:: ../images/qgis-pg-conn-test.png
            :class: small

Následně se již můžeme k databázi připojit

.. figure:: ../images/qgis-postgis-connect.png
           :width: 600px

a vybrat vektorové vrstvy :fignote:`(1)`, které chceme z geodatabáze
načíst :fignote:`(2)`.

.. figure:: ../images/qgis-postgis-layers.png
           :width: 700px

.. _DataCatalog:

Alternativní postup (datový katalog)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Připojení k databázi PostGIS je možné definovat i v rámci *datového
katalogu (prohlížeče)*.

.. figure:: ../images/../images/qgis-catalog-new.png
            :width: 300px

.. figure:: ../images/../images/qgis-postgis-new-settings.png
           :width: 350px

Vektorovou vrstvu z geodatabáze PostGIS přetáhneme z datového katalogu
do okna *Vrstvy*.

.. figure:: ../images/../images/qgis-catalog-layer.png
	    :class: small

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

            Uživatel ``skoleni`` má pro vrstvu :map:`obce_polygon` ve
            schématu *ruian* veškerá práva a data může případně
            modifikovat.


Otevíráme tabulku
-----------------

.. todo::

Nahráváme vlastní data do databáze
==================================

Postup pro QGIS
---------------

Předpokládáme, že každý uživatel pracuje ve vlastní databázovém
schématu. Toto schéma vytvoříme pomocí zásuvného modulu :ref:`DB
Manageru <db-manager>`.

Vytvoření databázového schématu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

V našem případě uložíme vektorová data do *vlastního schématu*,
nejprve toto schéma vytvoříme.

.. figure:: ../images/qgis-db-manager-new-schema.png
            :width: 300px

.. figure:: ../images/qgis-db-manager-create-schema.png
            :width: 225px

.. figure:: ../images/qgis-db-manager-new-schema-prop.png
            :width: 700px

            V nově vytvořeném schématu již má uživatel ``landa``
            právo zápisu.

Import Esri Shapefile do PostGISu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Import vektorových dat ve formátu Esri Shapefile umožňuje zásuvný
modul *Spit (Shapefile import)* dostupný z menu aplikace QGIS.

.. figure:: ../images/qgis-spit-menu.png
            :width: 350px

.. note:: Pokud není nástroj dostupný je nutné ho aktivovat z menu
          :menuselection:`Zásuvné moduly --> Spravovat a instalovat
          zásuvné moduly`.

	  .. figure:: ../images/qgis-spit-plugin.png

.. note:: Použijeme otevřená data poskytovaná IPR, konkrétně
          `občanskou vybavenost - toalety
          <http://opendata.iprpraha.cz/CUR/FSV/FSV_VerejnaWC_b/S_JTSK/FSV_VerejnaWC_b_shp.zip>`_.

V dialogu zvolíme databázi :fignote:`(1)`, ke které se
připojíme :fignote:`(2)`. Přidáme soubor ve formátu Esri Shapefile
:fignote:`(3)` určený k importu, definujeme název pro výstupní
databázovou tabulku a schéma :fignote:`(4)`. Jako poslední určíme kód
souřadnicového systému (v tomto případě S-JTSK, tj. :epsg:`5514`)
vektorových dat :fignote:`(5)`.

.. figure:: ../images/qgis-spit-dialog.png
            :class: middle

.. figure:: ../images/qgis-spit-progress.png
	    :width: 200px

Naimportovaná vrstva z geodatabáze PostGIS se nezobrazí automaticky,
musíme ji :ref:`přidat manuálně <qgis-add-pg-layer>`.

.. figure:: ../images/qgis-add-pg-so.png
            :class: large

Další možnosti
--------------

DB Manager
^^^^^^^^^^

Nahrání dat ve formátu Esri Shapefile do geodatabáze PostGIS umožňuje
v QGISu i zásuvný modul :program:`DB Manager`. Soubor ve formátu Esri
Shapefile naimportujeme z menu

.. figure:: ../images/shp-import-menu.png
           :width: 200px

anebo z nástrojové lišty DB Manageru.

.. figure:: ../images/shp-import.png
           :width: 250px

V dialogu vybereme soubor pro import do geodatabáze
:fignote:`(1)`. Dále můžeme změnit cílové schéma a název výsledné
tabulky v databázi :fignote:`(2)`. Dialog nabízí další možnosti včetně
transformace do jiného souřadnicového systému :fignote:`(3)`.

.. figure:: ../images/qgis-db-manager-create-table.png
	    :width: 400px
	    
.. figure:: ../images/qgis-db-manager-finish.png
            :width: 200px


pgAdmin
^^^^^^^

Vektorová data ve formátu Esri Shapefile lze do databáze PostGIS
naimportovat pomocí zásuvného modulu :program:`PostGIS Shapefile and DBF loader`
aplikace `pgAdmin <http://www.pgadmin.org/>`_.

.. figure:: ../images/pgadmin-import.png
            :width: 350px

Nejprve definujeme soubor ve formátu Esri Shapefile :fignote:`(1)`,
cílové databázové schéma :fignote:`(2)` a souřadnicový systém
:fignote:`(3)`.

.. figure:: ../images/pgadmin-create.png

.. figure:: ../images/pgadmin-new-layer.png
            :width: 700px

shp2pgsql
^^^^^^^^^

`shp2pgsql
<http://postgis.net/docs/manual-2.1/using_postgis_dbmanagement.html#shp2pgsql_usage>`_
je konzolový nástroj, který umožňuje import vektorových dat ve formátu Esri
Shapefile do geodatabáze PostGIS. Tento nástroj je součástí instalace
PostGIS.

Nejprve vytvoříme SQL dávku

.. code-block:: bash

               shp2pgsql -s 5514 stavebniobjekty.shp landa.stavebniobjekty > so.sql

* ``-s`` definuje souřadnicový systém,
* ``stavebniobjekty.shp`` je název vstupního souboru ve formátu Esri Shapefile,
* ``landa.stavebniobjekty`` je název výstupního databázového schématu a tabulky,
* ``> so.sql`` dávka je uložena do souboru ``so.sql``.

Vytvořenou SQL dávku nahrajeme do databáze *gismentors_vugtk*:

.. code-block:: bash

                psql gismentors_vugtk -U gismentors -W -h geo102.fsv.cvut.cz -f so.sql

ogr2ogr
^^^^^^^

`ogr2ogr <http://www.gdal.org/ogr2ogr.html>`_ je konzolový nástroj
knihovny `GDAL <http://gdal.org>`_ umožňující konverzi mezi datovými
formáty podporovanými touto knihovnou.

.. code-block:: bash

   ogr2ogr -f PostgreSQL \
   PG:"dbname=gismentors_vugtk host=geo102.fsv.cvut.cz user=gismentors password=XXX active_schema=landa" \
   stavebniobjekty.shp \
   -lco FID=gid

.. rubric:: :secnotoc:`Poznámky`

.. [#f1] Předpokládáme, že již máme definovány v QGISu parametry
         připojení k databázi, viz :doc:`návod <qgis>`.
