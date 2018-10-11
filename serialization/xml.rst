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

