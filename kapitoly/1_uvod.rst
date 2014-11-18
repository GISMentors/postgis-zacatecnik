ÚVOD
====

Databáze
--------

Kdy ukládat data do databáze?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Základním účelem databáze

Co je databáze?
^^^^^^^^^^^^^^^

Databázi, ať už relační, nebo objektovou, si můžeme představit jako knihovnu. V knihách (tabulkách) máme nějaké informace. Informace pro nás vyhledávají knihovnice (obslužné programy). K tomu používají katalogy a rejstříky (indexy). Organizace knihovny je plně pod naší kontrolou, ovlivňujeme hardware (kolik bude mít budova pater (disků), kolik bude volných regálů a manipulačního prostoru atd.), kolik bude mít knihovna fyzických zaměstnanců (počet jader procesoru). Dále ovlivňujeme organizaci, budou knihy řazeny podle abecedy podle názvů, podle klíčových slov, podle jména autora? Jak často budeme aktualizovat katalogy a rejstříky (aktualizovat indexy)? Kolik místa vlastně na katalogy/indexy vyhradíme? Jak budeme nakládat s místem po vyřazených svazcích (porces VACUUM)? A tak dále. Se svými zaměstnanci komunikujeme v jazyce SQL (pokud tedy hovoříme o relační databázi).

A co prostorová databáze?
^^^^^^^^^^^^^^^^^^^^^^^^^

Prostorová databáze, se podobá takové knihovně, ve které kromě knih jsou také mapy, atlasy, globusy... Zkrátka nosiče informací, které zaznamenávají také umístění jednotlivých údajů.

Jazyk SQL
---------


Indexy
------

Indexy v databázi slouží k co možná nejrychlejšímu dohledání záznamů. Fungují na podobném principu jako rejstřík v knize. Jedná se o jakýsi utříděný seznam klíčů spojených s odkazem na konkrétní datovou stránku, na místo na pevném disku, kde je uložena požadovaná informace. Smyslem indexu je provést při dohledání záznamu minimum porovnání hodnot v indexu s požadovanou hodnotou. U neindexované tabulky bychom museli porovnat požadovanou hodnotu se všemi záznamy.

.. noteadvanced:: Nejčastějším typem indexu je `b-tree`, zde jsou hodnoty uloženy ve stromovité struktuře založené na dichotmickém větvení. Na každém uzlu porovnáme požadovanou hodnotu s hodnotou na uzlu a zjistíme, jestli je větší, nebo menší. S každým patrem je síto jemější. To je velice efektivní, když si uvědomíme, že při zdvojnásobení objemu dat přibude jen jedno porovnání navíc.
