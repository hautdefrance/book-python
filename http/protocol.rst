*************
HTTP Protocol
*************

* Request vs Response
* URI vs URL
* HTTP vs HTTPS
* HTTP/1.1 vs HTTP/2.0
* Methods
* Statuses
* Headers


HTTP Methods
============
.. csv-table:: HTTP Methods
    :header-rows: 1
    :widths: 15, 25, 60

    "Method", "Function", "Description"
    "GET", "Read", "Requests using GET should only retrieve data and should have no other effect."
    "POST", "Create", "The POST method requests that the server accept the entity enclosed in the request as a new subordinate of the web resource identified by the URI."
    "PUT", "Update/Replace", "The PUT method requests that the enclosed entity be stored under the supplied URI."
    "PATCH", "Partial Update/Modify", "The PATCH method applies partial modifications to a resource."
    "DELETE", "Delete", "The DELETE method deletes the specified resource."
    "HEAD", "Show Headers", "The HEAD method asks for a response identical to that of a GET request, but without the response body."
    "CONNECT", "Connect", "The CONNECT method converts the request connection to a transparent TCP/IP tunnel, usually to facilitate SSL-encrypted communication (HTTPS) through an unencrypted HTTP proxy."
    "OPTIONS", "Show HTTP Methods", "The OPTIONS method returns the HTTP methods that the server supports for the specified URL."
    "TRACE", "Show Trace", "The TRACE method echoes the received request so that a client can see what (if any) changes or additions have been made by intermediate servers."


HTTP Statuses
=============
.. csv-table:: HTTP Status Families
    :header-rows: 1
    :widths: 15, 85

    "Code", "Description"
    "1XX", "Informational"
    "2XX", "Successful"
    "3XX", "Redirection"
    "4XX", "Client Error"
    "5XX", "Server Error"

``1xx`` Informational response
------------------------------
.. csv-table:: HTTP Statuses ``1xx`` Informational response
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "100", "Continue", ""
    "101", "Switching Protocols", ""
    "102", "Processing (WebDAV)", ""
    "103", "Early Hints", ""

``2xx`` Success
---------------
.. csv-table:: HTTP Statuses ``2xx`` Success
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "200", "OK", ""
    "201", "Created", ""
    "202", "Accepted", ""
    "203", "Non-Authoritative Information", ""
    "204", "No Content", ""
    "205", "Reset Content", ""
    "206", "Partial Content", ""
    "207", "Multi-Status (WebDAV)", ""
    "208", "Already Reported (WebDAV)", ""
    "209", "IM Used", ""

``3xx`` Redirection
-------------------
.. csv-table:: HTTP Statuses ``3xx`` Redirection
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "300", "Multiple Choices", ""
    "301", "Moved Permanently", ""
    "302", "Found (Previously 'Moved temporarily')", ""
    "303", "See Other", ""
    "304", "Not Modified", ""
    "305", "Use Proxy", ""
    "306", "Switch Proxy", ""
    "307", "Temporary Redirect", ""
    "308", "Permanent Redirect", ""

``4xx`` Client errors
---------------------
.. csv-table:: HTTP Statuses ``4xx`` Client errors
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "400", "Bad Request", ""
    "401", "Unauthorized", ""
    "402", "Payment Required", ""
    "403", "Forbidden", ""
    "404", "Not Found", ""
    "405", "Method Not Allowed", ""
    "406", "Not Acceptable", ""
    "407", "Proxy Authentication Required", ""
    "408", "Request Timeout", ""
    "409", "Conflict", ""
    "410", "Gone", ""
    "411", "Length Required", ""
    "412", "Precondition Failed", ""
    "413", "Payload Too Large", ""
    "414", "URI Too Long", ""
    "415", "Unsupported Media Type", ""
    "416", "Range Not Satisfiable", ""
    "417", "Expectation Failed", ""
    "418", "I'm a teapot", "This code was defined in 1998 as one of the traditional IETF April Fools' jokes, in RFC 2324"
    "421", "Misdirected Request", ""
    "422", "Unprocessable Entity (WebDAV)", ""
    "423", "Locked (WebDAV)", ""
    "424", "Failed Dependency (WebDAV)", ""
    "426", "Upgrade Required", ""
    "428", "Precondition Required", ""
    "429", "Too Many Requests", ""
    "431", "Request Header Fields Too Large", ""
    "451", "Unavailable For Legal Reasons", ""

``5xx`` Server errors
---------------------
.. csv-table:: HTTP Statuses ``5xx`` Server errors
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "500", "Internal Server Error", ""
    "501", "Not Implemented", ""
    "502", "Bad Gateway", ""
    "503", "Service Unavailable", ""
    "504", "Gateway Timeout", ""
    "505", "HTTP Version Not Supported", ""
    "506", "Variant Also Negotiates", ""
    "507", "Insufficient Storage (WebDAV)", ""
    "508", "Loop Detected (WebDAV)", ""
    "510", "Not Extended", ""
    "511", "Network Authentication Required", ""


HTTP Headers
============

HTTP Request Headers
--------------------
.. csv-table:: HTTP Request Headers
    :header-rows: 1
    :widths: 25, 75

    "Header", "Description"
    "Accept", ""
    "Accept-Charset", ""
    "Accept-Encoding", ""
    "Accept-Language", ""
    "Authorization", ""
    "Cache-Control", ""
    "Content-Length", ""
    "Content-Type", ""
    "Cookie", ""
    "Date", ""
    "Host", ""
    "Origin", ""
    "Pragma", ""
    "Referer", ""
    "User-Agent", ""
    "DNT", ""
    "X-Forwarded-For", ""
    "X-Csrf-Token", ""

HTTP Response Headers
---------------------
.. csv-table:: HTTP Response Headers
    :header-rows: 1
    :widths: 25, 75

    "Header", "Description"
    "Access-Control-Allow-Origin", ""
    "Access-Control-Allow-Methods", ""
    "Allow", ""
    "Cache-Control", ""
    "Content-Disposition", ""
    "Content-Encoding", ""
    "Content-Language", ""
    "Content-Length", ""
    "Content-Type", ""
    "Date", ""
    "ETag", ""
    "Expires", ""
    "Last-Modified", ""
    "Location", ""
    "Pragma", ""
    "Server", ""
    "Set-Cookie", ""
    "WWW-Authenticate", ""
    "X-Frame-Options", ""
    "Refresh", ""
    "Status", ""

