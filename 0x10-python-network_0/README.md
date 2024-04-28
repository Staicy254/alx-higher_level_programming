# Understanding URLs and HTTP

## What is a URL?

A Uniform Resource Locator (URL) is a reference to a web resource that specifies its location on the internet and the protocol used to access it. It typically consists of several components, including the scheme, domain name, path, query string, and fragment identifier.

## What is HTTP?

Hypertext Transfer Protocol (HTTP) is an application protocol for distributed, collaborative, hypermedia information systems. It is the foundation of data communication on the World Wide Web, defining how messages are formatted and transmitted, and how web servers and browsers respond to various commands.

## Reading a URL

To understand a URL, one needs to break it down into its components:

- **Scheme**: Specifies the protocol used to access the resource (e.g., HTTP, HTTPS, FTP).
- **Domain Name**: Identifies the location of the resource on the internet.
- **Sub-domain**: An optional part of the domain name that precedes the main domain.
- **Port Number**: Specifies the port on the server to which the request is sent.
- **Path**: Specifies the specific resource within the server's directory structure.
- **Query String**: Contains additional parameters for the request.
- **Fragment Identifier**: Identifies a specific section of the resource.

## Scheme for HTTP URL

The scheme for a HTTP URL is typically "http://".

## What is a Domain Name?

A domain name is a human-readable address that represents an IP address on the internet. It is used to identify websites and other resources.

## What is a Sub-domain?

A sub-domain is a subdivision of a domain name. It is used to organize and navigate different sections or services within a larger domain.

## Defining a Port Number in a URL

A port number in a URL is specified after the domain name and is separated by a colon (e.g., `http://example.com:8080`). It indicates the specific communication endpoint on the server where the client should connect.

## What is a Query String?

A query string is a part of a URL that contains data to be passed to the server as parameters. It is typically used in GET requests to send additional information to the server.

## What is an HTTP Request?

An HTTP request is a message sent by a client to a server to initiate an action. It specifies the resource to be accessed and the desired action to be performed.

## What is an HTTP Response?

An HTTP response is a message sent by a server to a client in response to an HTTP request. It contains status information about the request and may also include the requested data.

## What are HTTP Headers?

HTTP headers are additional pieces of information sent along with HTTP requests or responses. They provide metadata about the message, such as the content type, length, and encoding.

## What is the HTTP Message Body?

The HTTP message body is the content of an HTTP request or response. It contains the data being sent from the client to the server or vice versa.

## What is an HTTP Request Method?

An HTTP request method is a verb that defines the action to be performed on the specified resource. Common methods include GET, POST, PUT, DELETE, etc.

## What is an HTTP Response Status Code?

An HTTP response status code is a three-digit number sent by a server to indicate the status of an HTTP request. It provides information about whether the request was successful, redirected, or encountered an error.

## What is an HTTP Cookie?

An HTTP cookie is a small piece of data sent from a website and stored on the user's computer by the web browser. Cookies are used to remember user-specific information and preferences across multiple requests and sessions.

## How to Make a Request with cURL?

cURL is a command-line tool for transferring data with URL syntax. To make a request with cURL, use the `-X` option to specify the HTTP method and provide the URL as an argument.

## What Happens When You Type google.com in Your Browser (Application Level)?

When you type "google.com" in your browser, the browser initiates a DNS (Domain Name System) lookup to resolve the domain name to an IP address. Once the IP address is obtained, the browser establishes a TCP (Transmission Control Protocol) connection to the server hosting the website on port 80 (HTTP) or port 443 (HTTPS). Then, the browser sends an HTTP request for the homepage ("/") to the server. The server processes the request, generates an HTTP response containing the HTML content of the Google homepage, and sends it back to the browser. Finally, the browser renders the HTML content and displays the Google homepage to the user.

---
This README.md file provides an overview of URLs, HTTP, and related concepts, along with explanations of their components and functionalities.

