***
XML
***


xml
===

.. code-block:: xml

    <execute>
        <command timeout="2">/bin/ls -la /etc/</command>
        <command>/bin/ls -l /home/ /tmp/</command>
        <command timeout="1">/bin/sleep 2</command>
        <command timeout="2">/bin/echo 'juz wstalem'</command>
    </execute>

.. code-block:: python

    import logging
    import xml.etree.ElementTree
    import subprocess

    FILENAME = 'xml-execute-commands.xml'
    LOG_FORMAT = '[%(levelname)-5s] %(filename)s:%(lineno)s - %(msg).110s'


    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    log = logging.getLogger('code-execution')
    root = xml.etree.ElementTree.parse(FILENAME).getroot()


    def run(command, timeout=1):
        log.info('Executing command: %s' % command)

        with subprocess.Popen(command, stdout=subprocess.PIPE) as proc:

            try:
                output, errors = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                log.error('Timeout %s exceeded for command: %s' % (timeout, command))
                return proc.kill()

            if errors:
                log.error(errors)

            if output:
                # red = '\033[00;31m'
                # green = '\033[00;32m'
                # blue = '\033[00;36m'
                # white = '\033[00;39m'
                message = output.decode()

                log.debug('Output: {message}'.format(**locals()))
                return message


    for command in root.findall('./command'):
        cmd = command.text.split()
        timeout = float(command.get('timeout', 1))
        run(cmd, timeout)

``lxml``
========
.. code-block:: python

    from lxml import etree

    root = etree.Element("root")

    print(root.tag)  # root
    root.append(etree.Element("child1"))

    child2 = etree.SubElement(root, "child2")
    child3 = etree.SubElement(root, "child3")

    print(etree.tostring(root, pretty_print=True))

.. code-block:: xml

    <root>
      <child1/>
      <child2/>
      <child3/>
    </root>

Elements are lists
------------------
.. code-block:: python

    child = root[0]
    print(child.tag)     # child1
    print(len(root))     # 3
    root.index(root[1])  # 1

    children = list(root)

    for child in root:
        print(child.tag)
        # child1
        # child2
        # child3

    root.insert(0, etree.Element("child0"))
    start = root[:1]
    end = root[-1:]

    print(start[0].tag)  # child0
    print(end[0].tag)    # child3

Elements carry attributes as a dict
-----------------------------------
.. code-block:: python

    root = etree.Element("root", interesting="totally")
    etree.tostring(root)
    # b'<root interesting="totally"/>'

    print(root.get("interesting"))  # totally
    print(root.get("hello"))        # None

    root.set("hello", "Huhu")
    print(root.get("hello"))        # Huhu

    etree.tostring(root)
    b'<root interesting="totally" hello="Huhu"/>'

    sorted(root.keys())
    ['hello', 'interesting']

    for name, value in sorted(root.items()):
        print('%s = %r' % (name, value))
        # hello = 'Huhu'
        # interesting = 'totally'

.. code-block:: python

    attributes = root.attrib
    print(attributes["interesting"])            # totally
    print(attributes.get("no-such-attribute"))  # None

    attributes["hello"] = "Guten Tag"
    print(attributes["hello"])                  # Guten Tag

    d = dict(root.attrib)
    sorted(d.items())
    # [('hello', 'Guten Tag'), ('interesting', 'totally')]

Elements contain text
---------------------
.. code-block:: python

    >>> root = etree.Element("root")
    >>> root.text = "TEXT"

    >>> print(root.text)
    TEXT

    >>> etree.tostring(root)
    b'<root>TEXT</root>'

.. code-block:: html

    <html><body>Hello<br/>World</body></html>

.. code-block:: python

    >>> html = etree.Element("html")
    >>> body = etree.SubElement(html, "body")
    >>> body.text = "TEXT"

    >>> etree.tostring(html)
    b'<html><body>TEXT</body></html>'

    >>> br = etree.SubElement(body, "br")
    >>> etree.tostring(html)
    b'<html><body>TEXT<br/></body></html>'

    >>> br.tail = "TAIL"
    >>> etree.tostring(html)
    b'<html><body>TEXT<br/>TAIL</body></html>'

XPATH
-----
.. code-block:: python

    >>> print(html.xpath("string()")) # lxml.etree only!
    TEXTTAIL
    >>> print(html.xpath("//text()")) # lxml.etree only!
    ['TEXT', 'TAIL']

Tree iteration
--------------
.. code-block:: python

    >>> root = etree.Element("root")
    >>> etree.SubElement(root, "child").text = "Child 1"
    >>> etree.SubElement(root, "child").text = "Child 2"
    >>> etree.SubElement(root, "another").text = "Child 3"

    >>> print(etree.tostring(root, pretty_print=True))
    <root>
      <child>Child 1</child>
      <child>Child 2</child>
      <another>Child 3</another>
    </root>

    >>> for element in root.iter():
    ...     print("%s - %s" % (element.tag, element.text))
    root - None
    child - Child 1
    child - Child 2
    another - Child 3

.. code-block:: python

    >>> for element in root.iter("child"):
    ...     print("%s - %s" % (element.tag, element.text))
    child - Child 1
    child - Child 2

    >>> for element in root.iter("another", "child"):
    ...     print("%s - %s" % (element.tag, element.text))
    child - Child 1
    child - Child 2
    another - Child 3

.. code-block:: python

    >>> root.append(etree.Entity("#234"))
    >>> root.append(etree.Comment("some comment"))

    >>> for element in root.iter():
    ...     if isinstance(element.tag, basestring):  # or 'str' in Python 3
    ...         print("%s - %s" % (element.tag, element.text))
    ...     else:
    ...         print("SPECIAL: %s - %s" % (element, element.text))
    root - None
    child - Child 1
    child - Child 2
    another - Child 3
    SPECIAL: &#234; - &#234;
    SPECIAL: <!--some comment--> - some comment

    >>> for element in root.iter(tag=etree.Element):
    ...     print("%s - %s" % (element.tag, element.text))
    root - None
    child - Child 1
    child - Child 2
    another - Child 3

    >>> for element in root.iter(tag=etree.Entity):
    ...     print(element.text)
    &#234;

Serialization
-------------
.. code-block:: python

    >>> root = etree.XML('<root><a><b/></a></root>')

    >>> etree.tostring(root)
    b'<root><a><b/></a></root>'

    >>> print(etree.tostring(root, xml_declaration=True))
    <?xml version='1.0' encoding='ASCII'?>
    <root><a><b/></a></root>

    >>> print(etree.tostring(root, encoding='iso-8859-1'))
    <?xml version='1.0' encoding='iso-8859-1'?>
    <root><a><b/></a></root>

    >>> print(etree.tostring(root, pretty_print=True))
    <root>
      <a>
        <b/>
      </a>
    </root>

.. code-block:: python

    >>> root = etree.XML(
    ...    '<html><head/><body><p>Hello<br/>World</p></body></html>')

    >>> etree.tostring(root) # default: method = 'xml'
    b'<html><head/><body><p>Hello<br/>World</p></body></html>'

    >>> etree.tostring(root, method='xml') # same as above
    b'<html><head/><body><p>Hello<br/>World</p></body></html>'

    >>> etree.tostring(root, method='html')
    b'<html><head></head><body><p>Hello<br>World</p></body></html>'

    >>> print(etree.tostring(root, method='html', pretty_print=True))
    <html>
    <head></head>
    <body><p>Hello<br>World</p></body>
    </html>

    >>> etree.tostring(root, method='text')
    b'HelloWorld'

xslt
====

.. code-block:: python

    import io
    from lxml import etree


    XSLT = '''
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/">
        <foo><xsl:value-of select="/a/b/text()" /></foo>
        </xsl:template>
    </xsl:stylesheet>
    '''

    xslt_root = etree.XML(XSLT)
    transform = etree.XSLT(xslt_root)

    f = io.StringIO('<a><b>Text</b></a>')
    doc = etree.parse(f)
    result_tree = transform(doc)

    print(result_tree)

.. code-block:: xml

    <!--
    <?xml version="1.0" encoding="UTF-8"?>
    <CATALOG>
    <PLANT>
    <COMMON>Bloodroot</COMMON>
    <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$2.44</PRICE>
    <AVAILABILITY>031599</AVAILABILITY>
    </PLANT>
    </CATALOG>
    -->

    <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <style>
        body {font-family: Arial; font-size: 1em; background-color: #EEEEEE}
        div.title {background-color: teal; color: white; padding: 4px}
        div.description {margin-left:20px;margin-bottom:1em;font-size:10pt}
        span {font-weight: bold}

    </style>

    <body>

    <xsl:for-each select="CATALOG/PLANT">
      <div class="title">
            <span><xsl:value-of select="BOTANICAL"/></span>
            <xsl:value-of select="PRICE"/>
        </div>

      <div class="description">
        <p>
            <xsl:value-of select="description"/>
            <span> (<xsl:value-of select="AVAILABILITY"/> will be available)</span>
        </p>
      </div>

    </xsl:for-each>


Assignments
===========

XML Parsing
-----------
#. Mając do dyspozycji tekst z listingu poniżej
#. Przekonwertuj dane do struktur Pythonowych ``list`` of ``dict``

.. code-block:: xml


    <?xml version="1.0" encoding="UTF-8"?>
    <CATALOG>
    <PLANT>
    <COMMON>Bloodroot</COMMON>
    <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$2.44</PRICE>
    <AVAILABILITY>031599</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Columbine</COMMON>
    <BOTANICAL>Aquilegia canadensis</BOTANICAL>
    <ZONE>3</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$9.37</PRICE>
    <AVAILABILITY>030699</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Marsh Marigold</COMMON>
    <BOTANICAL>Caltha palustris</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Mostly Sunny</LIGHT>
    <PRICE>$6.81</PRICE>
    <AVAILABILITY>051799</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Cowslip</COMMON>
    <BOTANICAL>Caltha palustris</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$9.90</PRICE>
    <AVAILABILITY>030699</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Dutchman's-Breeches</COMMON>
    <BOTANICAL>Dicentra cucullaria</BOTANICAL>
    <ZONE>3</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$6.44</PRICE>
    <AVAILABILITY>012099</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Ginger, Wild</COMMON>
    <BOTANICAL>Asarum canadense</BOTANICAL>
    <ZONE>3</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$9.03</PRICE>
    <AVAILABILITY>041899</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Hepatica</COMMON>
    <BOTANICAL>Hepatica americana</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$4.45</PRICE>
    <AVAILABILITY>012699</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Liverleaf</COMMON>
    <BOTANICAL>Hepatica americana</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$3.99</PRICE>
    <AVAILABILITY>010299</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Jack-In-The-Pulpit</COMMON>
    <BOTANICAL>Arisaema triphyllum</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$3.23</PRICE>
    <AVAILABILITY>020199</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Mayapple</COMMON>
    <BOTANICAL>Podophyllum peltatum</BOTANICAL>
    <ZONE>3</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$2.98</PRICE>
    <AVAILABILITY>060599</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Phlox, Woodland</COMMON>
    <BOTANICAL>Phlox divaricata</BOTANICAL>
    <ZONE>3</ZONE>
    <LIGHT>Sun or Shade</LIGHT>
    <PRICE>$2.80</PRICE>
    <AVAILABILITY>012299</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Phlox, Blue</COMMON>
    <BOTANICAL>Phlox divaricata</BOTANICAL>
    <ZONE>3</ZONE>
    <LIGHT>Sun or Shade</LIGHT>
    <PRICE>$5.59</PRICE>
    <AVAILABILITY>021699</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Spring-Beauty</COMMON>
    <BOTANICAL>Claytonia Virginica</BOTANICAL>
    <ZONE>7</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$6.59</PRICE>
    <AVAILABILITY>020199</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Trillium</COMMON>
    <BOTANICAL>Trillium grandiflorum</BOTANICAL>
    <ZONE>5</ZONE>
    <LIGHT>Sun or Shade</LIGHT>
    <PRICE>$3.90</PRICE>
    <AVAILABILITY>042999</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Wake Robin</COMMON>
    <BOTANICAL>Trillium grandiflorum</BOTANICAL>
    <ZONE>5</ZONE>
    <LIGHT>Sun or Shade</LIGHT>
    <PRICE>$3.20</PRICE>
    <AVAILABILITY>022199</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Violet, Dog-Tooth</COMMON>
    <BOTANICAL>Erythronium americanum</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$9.04</PRICE>
    <AVAILABILITY>020199</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Trout Lily</COMMON>
    <BOTANICAL>Erythronium americanum</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$6.94</PRICE>
    <AVAILABILITY>032499</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Adder's-Tongue</COMMON>
    <BOTANICAL>Erythronium americanum</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$9.58</PRICE>
    <AVAILABILITY>041399</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Anemone</COMMON>
    <BOTANICAL>Anemone blanda</BOTANICAL>
    <ZONE>6</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$8.86</PRICE>
    <AVAILABILITY>122698</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Grecian Windflower</COMMON>
    <BOTANICAL>Anemone blanda</BOTANICAL>
    <ZONE>6</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$9.16</PRICE>
    <AVAILABILITY>071099</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Bee Balm</COMMON>
    <BOTANICAL>Monarda didyma</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$4.59</PRICE>
    <AVAILABILITY>050399</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Bergamot</COMMON>
    <BOTANICAL>Monarda didyma</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$7.16</PRICE>
    <AVAILABILITY>042799</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Black-Eyed Susan</COMMON>
    <BOTANICAL>Rudbeckia hirta</BOTANICAL>
    <ZONE>Annual</ZONE>
    <LIGHT>Sunny</LIGHT>
    <PRICE>$9.80</PRICE>
    <AVAILABILITY>061899</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Buttercup</COMMON>
    <BOTANICAL>Ranunculus</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$2.57</PRICE>
    <AVAILABILITY>061099</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Crowfoot</COMMON>
    <BOTANICAL>Ranunculus</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$9.34</PRICE>
    <AVAILABILITY>040399</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Butterfly Weed</COMMON>
    <BOTANICAL>Asclepias tuberosa</BOTANICAL>
    <ZONE>Annual</ZONE>
    <LIGHT>Sunny</LIGHT>
    <PRICE>$2.78</PRICE>
    <AVAILABILITY>063099</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Cinquefoil</COMMON>
    <BOTANICAL>Potentilla</BOTANICAL>
    <ZONE>Annual</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$7.06</PRICE>
    <AVAILABILITY>052599</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Primrose</COMMON>
    <BOTANICAL>Oenothera</BOTANICAL>
    <ZONE>3 - 5</ZONE>
    <LIGHT>Sunny</LIGHT>
    <PRICE>$6.56</PRICE>
    <AVAILABILITY>013099</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Gentian</COMMON>
    <BOTANICAL>Gentiana</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Sun or Shade</LIGHT>
    <PRICE>$7.81</PRICE>
    <AVAILABILITY>051899</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Blue Gentian</COMMON>
    <BOTANICAL>Gentiana</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Sun or Shade</LIGHT>
    <PRICE>$8.56</PRICE>
    <AVAILABILITY>050299</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Jacob's Ladder</COMMON>
    <BOTANICAL>Polemonium caeruleum</BOTANICAL>
    <ZONE>Annual</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$9.26</PRICE>
    <AVAILABILITY>022199</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Greek Valerian</COMMON>
    <BOTANICAL>Polemonium caeruleum</BOTANICAL>
    <ZONE>Annual</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$4.36</PRICE>
    <AVAILABILITY>071499</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>California Poppy</COMMON>
    <BOTANICAL>Eschscholzia californica</BOTANICAL>
    <ZONE>Annual</ZONE>
    <LIGHT>Sun</LIGHT>
    <PRICE>$7.89</PRICE>
    <AVAILABILITY>032799</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Shooting Star</COMMON>
    <BOTANICAL>Dodecatheon</BOTANICAL>
    <ZONE>Annual</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$8.60</PRICE>
    <AVAILABILITY>051399</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Snakeroot</COMMON>
    <BOTANICAL>Cimicifuga</BOTANICAL>
    <ZONE>Annual</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$5.63</PRICE>
    <AVAILABILITY>071199</AVAILABILITY>
    </PLANT>
    <PLANT>
    <COMMON>Cardinal Flower</COMMON>
    <BOTANICAL>Lobelia cardinalis</BOTANICAL>
    <ZONE>2</ZONE>
    <LIGHT>Shade</LIGHT>
    <PRICE>$3.02</PRICE>
    <AVAILABILITY>022299</AVAILABILITY>
    </PLANT>
    </CATALOG>



XSLT Transformation
-------------------
#. Mając do dyspozycji tekst z listingu poniżej
#. Przekonwertuj dane do struktur Pythonowych ``list`` of ``dict``

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <breakfast_menu>

    <food>
        <name>Belgian Waffles</name>
        <price>$5.95</price>
        <description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
        <calories>650</calories>
    </food>

    <food>
        <name>Strawberry Belgian Waffles</name>
        <price>$7.95</price>
        <description>Light Belgian waffles covered with strawberries and whipped cream</description>
        <calories>900</calories>
    </food>

    <food>
        <name>Berry-Berry Belgian Waffles</name>
        <price>$8.95</price>
        <description>Light Belgian waffles covered with an assortment of fresh berries and whipped cream</description>
        <calories>900</calories>
    </food>

    <food>
        <name>French Toast</name>
        <price>$4.50</price>
        <description>Thick slices made from our homemade sourdough bread</description>
        <calories>600</calories>
    </food>

    <food>
        <name>Homestyle Breakfast</name>
        <price>$6.95</price>
        <description>Two eggs, bacon or sausage, toast, and our ever-popular hash browns</description>
        <calories>950</calories>
    </food>

    </breakfast_menu>
