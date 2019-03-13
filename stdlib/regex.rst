*******************
Regular Expressions
*******************


Constructing Regular Expressions
================================

Visualizing RegExps
-------------------
* https://regexper.com/
* https://regex101.com/
* ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'``

.. figure:: img/regexp-vizualization.png
    :scale: 100%
    :align: center

    Visualization for pattern ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'``

Regular Expression Syntax
-------------------------
.. csv-table:: Regular Expression Syntax
    :header-rows: 1
    :widths: 25, 75

    "Syntax", "Description"
    "``.``", "(Dot.) In the default mode, this matches any character except a newline"
    "``^``", "(Caret.) Matches the start of the string, and in ``MULTILINE`` mode also matches immediately after each newline"
    "``$``", "Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline"
    "``*``", "Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible"
    "``+``", "Causes the resulting RE to match 1 or more repetitions of the preceding RE"
    "``?``", "Causes the resulting RE to match 0 or 1 repetitions of the preceding RE"
    "``*?``, ``+?``, ``??``", " Adding ``?`` after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched"
    "``{m}``", "Specifies that exactly m copies of the previous RE should be matched; fewer matches cause the entire RE not to match."
    "``{m,n}``", "Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible."
    "``{m,n}?``", "Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible."
    "``\``", "Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence"
    "``[a-z]``", "any character from ``a`` to ``z``"
    "``[A-Z]``", "any character from ``A`` to ``Z``"
    "``[0-9]``", "any digit from ``0`` to ``9``"
    "``[abc]``", "will match ``a``, ``b`` or ``c``"
    "``|``", "``A|B``, where A and B can be arbitrary REs, creates a regular expression that will match either A or B."
    "``(...)``", "Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group"
    "``(?P<name>...)``", "substring matched by the group is accessible via the symbolic group name name"
    "``(?P=name)``", "A backreference to a named group; it matches whatever text was matched by the earlier group named name. ``(?P<tag><.*?>)text(?P=tag)`` or ``(?P<tag><.*?>)text\1``"
    "``\number``", "Matches the contents of the group of the same number. Groups are numbered starting from 1. For example, ``(.+) \1`` matches ``the the`` or ``55 55``, but not ``thethe`` (note the space after the group)."
    "``\d``", "Unicode decimal digit ``[0-9]``, and many other digit characters"
    "``\s``", "Unicode whitespace characters ``[\t\n\r\f\v]`` and non-breaking spaces"
    "``\w``", "Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore"

Regex Flags
-----------
.. csv-table:: Regular Expression Flags
    :header-rows: 1
    :widths: 25, 75

    "Flag", "Description"
    "``re.IGNORECASE``", "Case-insensitive (Unicode support i.e. Ü and ü)"
    "``re.MULTILINE``", "``^`` matches beginning of the string and each line"
    "``re.MULTILINE``", "``$`` matches end of the string and each line"
    "``re.DOTALL``", "``.`` matches newlines"


Most frequent used functions in ``re`` module
=============================================

``re.match()``
--------------
.. literalinclude:: src/re-match.py
    :language: python
    :caption: Usage of ``re.match()``

``re.search()``
---------------
.. literalinclude:: src/re-search.py
    :language: python
    :caption: Usage of ``re.search()``

``re.findall()`` and ``re.finditer()``
--------------------------------------
.. literalinclude:: src/re-find.py
    :language: python
    :caption: Usage of ``re.findall()`` and ``re.finditer()``

``re.compile()``
----------------
.. literalinclude:: src/re-compile-no.py
    :language: python
    :caption: Compiles at every loop iteration, and then matches

.. literalinclude:: src/re-compile-yes.py
    :language: python
    :caption: Compiling before loop, hence matching only inside

``re.sub()``
------------
.. literalinclude:: src/re-sub.py
    :language: python
    :caption: Usage of ``re.sub()``

``re.split()``
--------------
.. literalinclude:: src/re-split.py
    :language: python
    :caption: Usage of ``re.split()``

Comparision between ``re.match()``, ``re.search()`` and ``re.findall()``
------------------------------------------------------------------------
.. literalinclude:: src/re-comparision.py
    :language: python
    :caption: Comparision between ``re.match()``, ``re.search()`` and ``re.findall()``


RegEx parameters (variables)
============================
.. literalinclude:: src/re-group.py
    :language: python
    :caption: Usage of group in ``re.match()``


Multi line searches
===================
.. literalinclude:: src/re-multiline.py
    :language: python
    :caption: Usage of regexp


Greedy and non-greedy search
============================
* greedy qualifiers: ``*``, ``+``, ``?``
* they match as much text as possible
* Adding ``?`` after the qualifier makes it non-greedy

.. literalinclude:: src/re-greedy.py
    :language: python
    :caption: Usage of greedy and non-greedy search in ``re.findall()``


Practical example of Regex usage
================================

Finding all Adverbs
-------------------
.. literalinclude:: src/re-example-2.py
    :language: python
    :caption: Finding all Adverbs

Making a Phonebook
------------------
.. literalinclude:: src/re-example-1.py
    :language: python
    :caption: Practical example of Regex usage

National Identification Numbers (Worldwide)
-------------------------------------------
* https://github.com/arthurdejong/python-stdnum/tree/master/stdnum/pl

Writing a Tokenizer
-------------------
.. literalinclude:: src/re-example-3.py
    :language: python
    :caption: Writing a Tokenizer.


Standards
=========

W3C HTML5 Standard regexp for email field
-----------------------------------------
.. code-block:: text

    /^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/

W3C standard for URL understanding
----------------------------------
.. code-block:: text

    ^(?=[^&])(?:(?<scheme>[^:/?#]+):)?(?://(?<authority>[^/?#]*))?(?<path>[^?#]*)(?:\?(?<query>[^#]*))?(?:#(?<fragment>.*))?

W3C standard for URL parsing
----------------------------
.. code-block:: text

    /^\s*[a-z](?:[-a-z0-9\+\.])*:(?:\/\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:])*@)?(?:\[(?:(?:(?:[0-9a-f]{1,4}:){6}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|::(?:[0-9a-f]{1,4}:){5}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){4}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:[0-9a-f]{1,4}:[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){3}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,2}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){2}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,3}[0-9a-f]{1,4})?::[0-9a-f]{1,4}:(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,4}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,5}[0-9a-f]{1,4})?::[0-9a-f]{1,4}|(?:(?:[0-9a-f]{1,4}:){0,6}[0-9a-f]{1,4})?::)|v[0-9a-f]+[-a-z0-9\._~!\$&\'\(\)\*\+,;=:]+)\]|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}|(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=@])*)(?::[0-9]*)?(?:\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))*)*|\/(?:(?:(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))+)(?:\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))*)*)?|(?:(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))+)(?:\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))*)*|(?!(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@])))(?:\?(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@])|[\uE000-\uF8FF\uF0000-\uFFFFD|\u100000-\u10FFFD\/\?])*)?(?:\#(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@])|[\/\?])*)?\s*$/i

Parsing URLs
------------
* Source :cite:`W3CParsingURLs`

To parse a *URL* url into its component parts, the user agent must use the following steps:

    #. Strip leading and trailing space characters from url.
    #. Parse url in the manner defined by :RFC:`3986`, with the following exceptions:

        * Add all characters with code points less than or equal to ``U+0020`` or greater than or equal to ``U+007F`` to the ``<unreserved>`` production.

        * Add the characters ``U+0022``, ``U+003C``, ``U+003E``, ``U+005B`` ... ``U+005E``, ``U+0060``, and ``U+007B`` ... ``U+007D`` to the ``<unreserved>`` production

        * Add a single ``U+0025`` *PERCENT SIGN* character as a second alternative way of matching the ``<pct-encoded>`` production, except when the ``<pct-encoded>`` is used in the ``<reg-name>`` production.

        * Add the ``U+0023`` *NUMBER SIGN* character to the characters allowed in the ``<fragment>`` production.

    #. If url doesn't match the ``<URI-reference>`` production, even after the above changes are made to the *ABNF* definitions, then parsing the *URL* fails with an error. [:RFC:`3986`] Otherwise, parsing url was successful; the components of the *URL* are substrings of url defined as follows:

    .. glossary::

        <scheme>
            The substring matched by the ``<scheme>`` production, if any.

        <host>
            The substring matched by the ``<host>`` production, if any.

        <port>
            The substring matched by the ``<port>`` production, if any.

        <hostport>
            If there is a ``<scheme>`` component and a ``<port>`` component and the port given by the ``<port>`` component is different than the default port defined for the protocol given by the ``<scheme>`` component, then ``<hostport>`` is the substring that starts with the substring matched by the ``<host>`` production and ends with the substring matched by the ``<port>`` production, and includes the colon in between the two. Otherwise, it is the same as the ``<host>`` component.

        <path>
            The substring matched by one of the following productions, if one of them was matched:

        <path-abempty>
        <path-absolute>
        <path-noscheme>
        <path-rootless>
        <path-empty>
        <query>
            The substring matched by the ``<query>`` production, if any.

        <fragment>
            The substring matched by the ``<fragment>`` production, if any.

        <host-specific>
            The substring that follows the substring matched by the <authority> production, or the whole string if the ``<authority>`` production wasn't matched.




Assignments
===========

Parsing text from webpage
-------------------------
* Filename: ``regex_html.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Input data: :numref:`listing-regex-moon-speech`

#. Skopiuj zawartość listingu do pliku ``moon-speech.html``
#. Za pomocą regexpów wytnij tekst fragmentu przemówienia JFK
#. Zwróć pierwszy paragraf tekstu przemówienia zaczynający się od słów "We choose to go to the moon"

.. code-block:: text
    :name: listing-regex-moon-speech
    :caption: "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12 :cite:`Kennedy1962`

    <html><body><bgsound src="jfktalk.wav" loop="2"><p></p><center><h3>John F. Kennedy Moon Speech - Rice Stadium</h3><img src="jfkrice.jpg"><h3>September 12, 1962</h3></center><p></p><hr><p></p><center>Movie clips of JFK speaking at Rice University: <a href="JFKatRice.mov">(.mov)</a> or <a href="jfkrice.avi">(.avi)</a> (833K)</center><p><a href="jfkru56k.asf">See and hear</a> the entire speech for 56K modem download [8.7 megabytes in a .asf movie format which requires Windows Media Player 7 (speech lasts about 33 minutes)].<br><a href="jfkru100.asf">See and hear</a> the entire speech for higher speed access [25.3 megabytes in .asf movie format which requires Windows Media Player 7].<br><a href="jfkslide.asf">See and hear</a> a five minute audio version of the speech with accompanying slides and music. This is a most inspirational presentation of, perhaps, the most famous space speech ever given. The file is a streaming video Windows Media Player 7 format. [11 megabytes in .asf movie format which requires Windows Media Player 7]. <br><a href="jfk_rice_speech.mpg">See and hear</a> the 17 minute 48 second speech in the .mpg format. This is a very large file of 189 megabytes and only suggested for those with DSL, ASDL, or cable modem access as the download time on a 28.8K or 56K modem would be many hours duration. </p><p></p><hr><p></p><center><h4>TEXT OF PRESIDENT JOHN KENNEDY'S RICE STADIUM MOON SPEECH</h4></center><p>President Pitzer, Mr. Vice President, Governor, CongressmanThomas, Senator Wiley, and Congressman Miller, Mr. Webb, Mr.Bell, scientists, distinguished guests, and ladies and gentlemen:</p><p>We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organize and measure the best of our energies and skills,because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win,and the others, too. </p><p>It is for these reasons that I regard the decision last year to shift our efforts in space from low to high gear as among the most important decisions that will be made during my incumbency in the office of the Presidency. </p><p>In the last 24 hours we have seen facilities now being created for the greatest and most complex exploration in man's history.We have felt the ground shake and the air shattered by the testing of a Saturn C-1 booster rocket, many times as powerful as the Atlas which launched John Glenn, generating power equivalent to 10,000 automobiles with their accelerators on the floor.We have seen the site where the F-1 rocket engines, each one as powerful as all eight engines of the Saturn combined, will be clustered together to make the advanced Saturn missile, assembled in a new building to be built at Cape Canaveral as tall as a48 story structure, as wide as a city block, and as long as two lengths of this field.</p><p></p><hr><p></p><center><a href="movies.html">Return to Space Movies Cinema</a></center></body></html>

PESEL Validation
----------------
* Lines of code to write: 0 lines
* Estimated time of completion: 10 min

#. Przeprowadź eksperyment myślowy (nie pisz kodu tylko pomyśl)
#. Jak sprawdzić za pomocą wyrażeń regularnych czy:

    * czy pesel jest poprawny
    * jaka jest data urodzenia? (podaj obiekt ``datetime.date``
    * płeć użytkownika który podał PESEL

#. Mając PESEL "69072101234"

    #. Jakie wyrażenie może być na pierwszym miejscu w PESEL?
    #. Jakie wyrażenie może być na drugim miejscu w PESEL?
    #. Jakie wyrażenie może być na trzecim miejscu w PESEL?
    #. Jakie wyrażenie może być na czwartym miejscu w PESEL?
    #. Jakie wyrażenie może być na piątym miejscu w PESEL?
    #. Jakie wyrażenie może być na szóstym miejscu w PESEL?

#. Mając PESEL "18220801234"

    #. Jakie wyrażenie może być na pierwszym miejscu w PESEL?
    #. Jakie wyrażenie może być na drugim miejscu w PESEL?
    #. Jakie wyrażenie może być na trzecim miejscu w PESEL?
    #. Jakie wyrażenie może być na czwartym miejscu w PESEL?
    #. Jakie wyrażenie może być na piątym miejscu w PESEL?
    #. Jakie wyrażenie może być na szóstym miejscu w PESEL?

:Z gwiazdką:
    * sprawdź walidację numerów PESEL dla osób urodzonych po 2000 roku.
    * sprawdź sumę kontrolną
