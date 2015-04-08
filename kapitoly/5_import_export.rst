==============================
Import a export dat z databáze
==============================

Nahráváme vlastní data do databáze
----------------------------------

Import dat ve formátu Esri Shapefile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Předpokládáme, že každý uživatel pracuje ve vlastní databázovém
schématu. Toto schéma vytvoříme pomocí zásuvného modulu :ref:`DB
Manageru <db-manager>`.

Vytvoření databázového schématu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Import dat
~~~~~~~~~~

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
^^^^^^^^^^^^^^

DB Manager
~~~~~~~~~~

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
~~~~~~~

Vektorová data ve formátu Esri Shapefile lze do databáze PostGIS
naimportovat pomocí zásuvného modulu :program:`PostGIS Shapefile and DBF loader`
aplikace `pgAdmin <http://www.pgadmin.org/>`_.

.. figure:: ../images/pgadmin-import.png
            :width: 350px

Nejprve definujeme soubor ve formátu Esri Shapefile :fignote:`(1)`,
cílové databázové schéma a cílovou tabulku :fignote:`(2)` a případně i
souřadnicový systém :fignote:`(3)`.

.. figure:: ../images/pgadmin-create.png

.. figure:: ../images/pgadmin-new-layer.png
            :class: large

Pro pokročilé uživatele
^^^^^^^^^^^^^^^^^^^^^^^

.. tip:: Více k tomuto tématu ve školení `PostGIS pro pokročilé
         <http://www.gismentors.cz/skoleni/postgis/#pokrocily>`_.

shp2pgsql
~~~~~~~~~

`shp2pgsql
<http://postgis.net/docs/using_postgis_dbmanagement.html#shp2pgsql_usage>`_
je konzolový nástroj, který umožňuje import vektorových dat ve formátu
Esri Shapefile do geodatabáze PostGIS. Tento nástroj je součástí
instalace PostGIS.

Nejprve vytvoříme SQL dávku

.. code-block:: bash

               shp2pgsql -s 5514 FSV_VerejnaWC_b.shp landa.toalety > wc.sql

* ``-s`` definuje souřadnicový systém,
* ``FSV_VerejnaWC_b.shp`` je název vstupního souboru ve formátu Esri Shapefile,
* ``landa.toalety`` je název výstupního databázového schématu a tabulky,
* ``> wc.sql`` dávka je uložena do souboru ``wc.sql``.

Vytvořenou SQL dávku nahrajeme do databáze *gismentors*:

.. code-block:: bash

                psql gismentors -U skoleni -W -h training.gismentors.eu -f wc.sql

ogr2ogr
~~~~~~~

`ogr2ogr <http://www.gdal.org/ogr2ogr.html>`_ je konzolový nástroj
knihovny `GDAL <http://gdal.org>`_ umožňující konverzi mezi datovými
formáty podporovanými touto knihovnou.

.. code-block:: bash

   ogr2ogr -f PostgreSQL \
   PG:"dbname=gismentors host=training.gismentors.eu user=skoleni password=XXX active_schema=landa" \
   FSV_VerejnaWC_b.shp \
   -a_srs EPSG:5514
