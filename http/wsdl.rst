****
WSDL
****


Main Structure
==============

.. code-block:: xml

    <definitions>

    <types>
      data type definitions........
    </types>

    <message>
      definition of the data being communicated....
    </message>

    <portType>
      set of operations......
    </portType>

    <binding>
      protocol and data format specification....
    </binding>

    </definitions>


Example
=======
* In this example the <portType> element defines "glossaryTerms" as the name of a port, and "getTerm" as the name of an operation.
* The "getTerm" operation has an input message called "getTermRequest" and an output message called "getTermResponse".
* The <message> elements define the parts of each message and the associated data types.

.. code-block:: xml

    <message name="getTermRequest">
      <part name="term" type="xs:string"/>
    </message>

    <message name="getTermResponse">
      <part name="value" type="xs:string"/>
    </message>

    <portType name="glossaryTerms">
      <operation name="getTerm">
        <input message="getTermRequest"/>
        <output message="getTermResponse"/>
      </operation>
    </portType>

The <portType> Element
----------------------
* The <portType> element defines a web service, the operations that can be performed, and the messages that are involved.
* The request-response type is the most common operation type, but WSDL defines four types:

.. csv-table::
    :header-rows: 1

    "Type", "Definition"
    "One-way", "The operation can receive a message but will not return a response"
    "Request-response", "The operation can receive a request and will return a response"
    "Solicit-response", "The operation can send a request and will wait for a response"
    "Notification", "The operation can send a message but will not wait for a response"

WSDL One-Way Operation
======================
.. code-block:: xml

    <message name="newTermValues">
      <part name="term" type="xs:string"/>
      <part name="value" type="xs:string"/>
    </message>

    <portType name="glossaryTerms">
      <operation name="setTerm">
        <input name="newTerm" message="newTermValues"/>
      </operation>
    </portType >


WSDL Request-Response Operation
===============================
.. code-block:: xml

    <message name="getTermRequest">
      <part name="term" type="xs:string"/>
    </message>

    <message name="getTermResponse">
      <part name="value" type="xs:string"/>
    </message>

    <portType name="glossaryTerms">
      <operation name="getTerm">
        <input message="getTermRequest"/>
        <output message="getTermResponse"/>
      </operation>
    </portType>


WSDL Binding to SOAP
====================
.. code-block:: xml

    <message name="getTermRequest">
      <part name="term" type="xs:string"/>
    </message>

    <message name="getTermResponse">
      <part name="value" type="xs:string"/>
    </message>

    <portType name="glossaryTerms">
      <operation name="getTerm">
        <input message="getTermRequest"/>
        <output message="getTermResponse"/>
      </operation>
    </portType>

    <binding type="glossaryTerms" name="b1">
       <soap:binding style="document"
       transport="http://schemas.xmlsoap.org/soap/http" />
       <operation>
         <soap:operation soapAction="http://example.com/getTerm"/>
         <input><soap:body use="literal"/></input>
         <output><soap:body use="literal"/></output>
      </operation>
    </binding>
