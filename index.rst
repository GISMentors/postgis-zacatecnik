.. Force build, can be deleted any time

.. only:: latex

   #####
   Obsah
   #####

.. only:: html

   `GISMentors <http://gismentors.cz>`_ | Školení `GRASS GIS
   <http://gismentors.cz/skoleni/grass-gis>`_ | `QGIS
   <http://gismentors.cz/skoleni/qgis>`_ | `PostGIS
   <http://gismentors.cz/skoleni/postgis>`_ | `GeoPython
   <http://gismentors.cz/skoleni/geopython>`_
   
   ****
   Úvod
   ****

.. only:: html
          
   .. image:: images/postgis-logo.png
              :width: 140px
              :align: left
                 
**PostGIS** je rozšíření objektově-relačního open source databázového
systému :wikipedia:`PostgreSQL` umožňující uložení, správu a analýzu
geografických dat. PostGIS implementuje v prostředí PostgreSQL
specifikaci `Simple Features
<http://www.opengeospatial.org/standards/sfa>`_ konsorcia
:wikipedia:`Open Geospatial Consortium`.

.. only:: latex

   .. figure:: images/postgis-logo.png
      :scale-latex: 20

      Logo projektu PostGIS

PostGIS lze použít jako databázové uložiště dat společně s oblíbeným
desktopovým open source GISem `QGIS <http://www.qgis.org>`_.
           
PostGIS je podobně jako QGIS multiplatformní a plně funkční na
platformách jako GNU/Linux, MS Windows či Mac OSX.

.. only:: html

   .. tip::

      Text školení je dostupný i v tisknutelné formě `PDF
      <./skoleni-postgis-zacatecnik.pdf>`_.

.. index::
   pair: datové sady; ke stažení

.. notedata::

   Datová sada je stažitelná pro PostgreSQL ve `formátu dump
   <http://training.gismentors.eu/geodata/postgis/gismentors.dump>`_
   (525 MB). Další informace v kapitole :doc:`kapitoly/7_instalace`.

.. warning:: :red:`Toto je pracovní verze školení, která je aktuálně
             ve vývoji!`

**Vstupní znalost**

* Uživatel má základní znalosti GIS

**Výstupní dovednost**

* Uživatel získá základní znalost jazyka :wikipedia:`SQL`
* Uživatel je schopen data z databáze v prostředí QGIS vizualizovat a
  editovat
* Uživatel je schopen z prostředí QGIS provádět v databázi jednodušší
  prostorové dotazy a další základní operace
* Uživatel zvládne naimportovat do databáze vlastní data a data z
  databáze exportovat do ostatních GIS formátů

**Požadavky**

* `PostgreSQL <http://www.postgresql.org>`_, volitelně `pgAdmin
  <http://www.pgadmin.org/>`_, `LibreOffice
  <http://www.libreoffice.org/>`_
* `QGIS <http://www.qgis.org>`_ 2.14 a vyšší
* `PostGIS <http://www.postgis.net>`_ 2.0 a vyšší

.. only:: html

   Obsah
   =====

.. toctree::
   :maxdepth: 3

   kapitoly/1_uvod
   kapitoly/2_zaciname
   kapitoly/3_jazyk_sql
   kapitoly/4_prostorove_dotazy
   kapitoly/5_import_export
   kapitoly/6_procvicovani_a_prakticke_ukazky
   kapitoly/7_instalace
              
*******
Dodatky
*******

O dokumentu
===========

Text dokumentu je licencován pod `Creative Commons
Attribution-ShareAlike 4.0 International License
<http://creativecommons.org/licenses/by-sa/4.0/>`_.

.. figure:: images/cc-by-sa.png 
	    :width: 130px
	    :scale-latex: 20
              
*Verze textu dokumentu:* |release| (sestaveno |today|)

Autoři
------

Za `GISMentors <http://www.gismentors.cz/>`_:

* `Jan Michálek <http://www.gismentors.cz/mentors/michalek>`_ ``<godzilalalala gmail.com>``
* `Martin Landa <http://www.gismentors.cz/mentors/landa>`_ ``<martin.landa opengeolabs.cz>``

Text dokumentu
--------------

.. only:: latex

   Online HTML verze textu školení je dostupná na adrese:

   * http://training.gismentors.eu/postgis-zacatecnik

Zdrojové texty školení jsou dostupné na adrese:

* https://github.com/GISMentors/postgis-zacatecnik

