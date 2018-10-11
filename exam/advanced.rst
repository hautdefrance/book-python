*************************
Exam from advanced topics
*************************

Mini Botnet
===========
#. Do pliku ``botnet-commands.xml`` skopiuj zawartość :numref:`listing-botnet-commands`.
#. Stwórz mini botnet o architekturz podanej :numref:`figure-botnet`. Mini botnet składa się z trzech części:

    - Heartbeat Server - server przyjmujący informacje o ofiarach (czy wciąż żyją),
    - Victim - ofiara,
    - Attacket - atakujący.

.. figure:: img/botnet.png
    :name: figure-botnet
    :scale: 75%
    :align: center

    Architektura botnet

:Hints:
    - Do weryfikacji czy port jest otwarty możesz użyć ``telnet`` albo ``netcat``

Heartbeat
---------
#. Skrypt serwera heartbeat nazwij ``botnet_heartbeat_server.py``
#. Server ma przyjmować komunikaty UDP na porcie 1337
#. Datę UTC przyjścia pakietu, IP i port backdoora zapisuje do bazy danych ``sqlite3`` jako pola:

    - datetime DATETIME,
    - ip TEXT,
    - port INTEGER

:Hints:
    * ``socketserver.UDPServer``
    * ``sqlite3``

Victim
------
#. Skrypt ofiary nazwij ``botnet_victim.py``
#. Po zainfekowaniu otwiera randomowy port TCP (backdoor) z przedziału 1025-65535 na którym nasłuchuje komunikatów. Dlaczego taki zakres portów?
#. Co 5 sekund wysyła informację ze swoim numerem portu backdoor oraz swoim adresem IP do serwera Heartbeat
#. Po otrzymaniu komunikatu XML na port backdoora wykonuje operację w nim zawarte
#. Ofiara ma przesyłać dane atakującemu w formacie JSON w formacie zawierającym datę, ip, port, stdout, stderror
#. Stwórz dekorator ``is_valid_xml``, który sprawdzi czy XML się waliduje (czy ma poprawną strukturę) i tylko wtedy wykona polecenia
#. Stwórz dekorator ``log_incoming_requests``, który zapisze do pliku ``botnet.log`` logi w formacie ``Request from IP:PORT to execute COMMAND ARGUMENTS`` dla każdego polecenia wykonywanego na systemie ofiary

:Hints:
    * ``random``
    * ``logging``
    * ``socket``
    * ``socketserver.TCPServer``
    * ``subprocess.run()``
    * ``json.dumps()``, ``json.loads()``
    * ``xml.etree.ElementTree``

Attacker
--------
#. Skopiuj zawartość :numref:`listing-botnet-commands` do pliku ``botnet-commands.xml``
#. Skrypt atakującego nazwij ``botnet_attacker.py``
#. Skrypt można wywoływać z parametrami linii poleceń:

    - ``--xml FILENAME``, domyślnie ``botnet-commands.xml``, opcjonalny (jeżeli podano inne parametry),
    - ``--exec COMMAND`` - opcjonalny,
    - ``--cat FILENAME`` - opcjonalny,
    - ``--ls PATH`` - opcjonalny,
    - ``--eval CODE`` - opcjonalny.

#. Skrypt ma do wszystkich botów (ofiar), które pingnęły serwer heartbeat w ciągu godziny wysyłać (IP ofiary, port backdoor) polecenia do wykonania.
#. Polecenia są:

    - w pliku XML podanym jako parametr (jeżeli podano flagę ``--xml``),
    - podane jako parametr do ``--exec``,
    - wyświetlanie zawartości pliku podanego jako parametr ``--cat``,
    - listowanie zawartości katalogu podanego jako parametr ``--ls``,
    - wykonywanie kodu Python i zwracanie wyników, jeżeli podano ``--eval``.

#. Polecenia do wykonania bez względu na flagę muszą być przesłane za pomocą komunikatów XML.
#. Datę, komunikat XML, oraz listę hostów do których poszło zapytanie zapisuj w bazie ``sqlite3`` w charakterze logów
#. Wyniki, które przyjdą od ofiar zapisuj w bazie danych ``sqlite3`` wraz z datą otrzymania, adresem IP ofiary, portem (backdoor), stdout i stderr

:About:
    #. Do obsługi parametrów z linii poleceń wykorzystaj ``argparse``
    #. Przetwarzanie requestów jest nieblokujące, tzn. otwieraj wątek dla każdego zapytania
    #. Wykorzystaj ``os.path.join`` (łączenie ścieżki) oraz ``os.walk`` (wyświetlanie zawartości).

.. literalinclude:: src/botnet-commands.xml
    :name: listing-botnet-commands
    :language: python
    :caption: Komunikat XML z listą poleceń do wykonania na komputerze ofiary

:Hints:
    * ``argparse``
    * ``socket``
    * ``json.dumps()``, ``json.loads()``

:Zadanie z gwiazdką:
    Za pomocą ``Django`` stwórz panel administracyjny dla botnetu:

    * Wyszukiwanie aktywnych hostów
    * ``command``
