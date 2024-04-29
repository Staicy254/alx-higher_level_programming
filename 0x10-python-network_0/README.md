# Understanding URLs and HTTP

## URL Basics

- **What a URL is:** Uniform Resource Locator, a reference to a web resource that specifies its location and how to retrieve it.
- **How to read a URL:** Break down into components like scheme, domain, path, query string, etc.
- **The scheme for a HTTP URL:** Typically "http://" or "https://", specifying the protocol for retrieving the resource.
- **What a domain name is:** The human-readable name corresponding to the IP address of a server hosting the resource.
- **What a sub-domain is:** A subdivision of a domain, indicating a specific branch or section within the larger domain hierarchy.
- **How to define a port number in a URL:** Appending `:port_number` after the domain, specifying the port to use for the connection.

## HTTP Fundamentals

- **What HTTP is:** Hypertext Transfer Protocol, a protocol for transferring hypermedia documents (like HTML) on the web.
- **What an HTTP request is:** Communication from a client to a server, specifying an action to be performed.
- **What an HTTP response is:** Communication from a server to a client, containing the requested resource or an error message.
- **What HTTP headers are:** Additional information sent with an HTTP request or response, specifying metadata about the communication.
- **What the HTTP message body is:** Optional data sent with an HTTP request or response, containing the actual content being transferred.
- **What an HTTP request method is:** Verb specifying the desired action for an HTTP request, like GET, POST, PUT, DELETE, etc.
- **What an HTTP response status code is:** Numeric code indicating the outcome of an HTTP request, such as success, failure, redirection, etc.
- **What an HTTP Cookie is:** Small piece of data sent from a website and stored on the user's device, often used for user authentication, session management, etc.

## Making Requests

- **How to make a request with cURL:** Command-line tool for making HTTP requests directly from the terminal, useful for testing APIs, debugging, etc.

## Browser Behavior

- **What happens when you type google.com in your browser (Application level):** The browser sends an HTTP GET request to the server hosting google.com, which responds with the HTML content of the Google homepage. The browser then renders this HTML content, fetching additional resources (like CSS, JavaScript, images) as needed to fully display the page.

