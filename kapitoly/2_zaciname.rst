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

.. _db-connection:

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

.. notecmd:: Připojení k databázi

   .. code-block:: bash
      
      psql gismentors -U skoleni -W -h training.gismentors.eu

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

Editujeme vektorová data
------------------------

:program:`QGIS` umožňuje editaci různých formátů vektorových dat
včetně dat uložených v geodatabázi PostGIS. Přepnout danou vektorovou
vrstvu do *editačního módu* je možné z kontextového menu

.. figure:: ../images/qgis-edit-menu.png
            :width: 350px

anebo *nástrojové lišty* QGISu.

.. figure:: ../images/qgis-edit-toolbar.png
            :width: 300px

Po přepnutí do editačního módu se vektorová vrstva zobrazí včetně
lomových bodů (červené křížky).

.. figure:: ../images/qgis-edit-mode.png
            :width: 800px

**Editační nástrojová lišta** QGISu umožňuje

.. figure:: ../images/qgis-edit-toolbar.png
            :width: 350px

.. table::
   :class: toc

   +-----+-------------------------------------------------+
   | |A| |  přidávat nové prvky                            |
   +-----+-------------------------------------------------+
   | |M| |  přesunovat existující prvky                    |
   +-----+-------------------------------------------------+
   | |N| |  modifikovat uzly (přidávat, mazat a přesunovat)|
   +-----+-------------------------------------------------+
   | |D| |  smazat vybrané prvky                           |
   +-----+-------------------------------------------------+
   | |C| |  vyjmout vybrané prvky                          |
   +-----+-------------------------------------------------+
   | |O| |  kopírovat vybrané prvky                        |
   +-----+-------------------------------------------------+
   | |P| |  vložit prvky                                   |
   +-----+-------------------------------------------------+

.. |A| image:: ../images/qgis-edit-add.png
               :width: 32px
               :align: middle

.. |M| image:: ../images/qgis-edit-move.png
               :width: 32px
               :align: middle

.. |N| image:: ../images/qgis-edit-node.png
               :width: 32px
               :align: middle

.. |D| image:: ../images/qgis-edit-delete.png
               :width: 32px
               :align: middle

.. |C| image:: ../images/qgis-edit-cut.png
               :width: 32px
               :align: middle

.. |O| image:: ../images/qgis-edit-copy.png
               :width: 32px
               :align: middle

.. |P| image:: ../images/qgis-edit-paste.png
               :width: 32px
               :align: middle

Příklad přidání nového prvku
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Z nástrojové lišty vybereme nástroj pro *přidávání nového prvku*.

Lomové body nového prvku volíme stisknutím levého tlačítka
myši. Poslední uložený lomový bod můžeme vrátit zpět pomocí klávesy
:kbd:`Backspace`.

.. figure:: ../images/qgis-edit-new-feature.png
            :width: 800px

Editaci prvku ukončíme stisknutím pravého tlačítka myši. V posledním
kroku můžeme vyplnit atributy nově přidaného prvku.

.. figure:: ../images/qgis-edit-new-feature-attr.png
            :width: 800px

.. note:: Více k editace v `manuálu
          <http://docs.qgis.org/2.2/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html>`_
          QGISu.

