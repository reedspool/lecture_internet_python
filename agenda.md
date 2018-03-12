# The Internet: How It Works, How To Use It
## Lecture Notes for NYU Python Class

The __Internet__ is the coolest communication invention since semaphore. With only a Python interpreter and an Internet connection, you can use this network to **send messages** and **connected applications**.

The **World Wide Web** is a piece of the Internet. The Web's killer app is **web pages**, and most people view them with **web browsers**. Python is often used as a **web server** to deliver those pages to users.

### Agenda

1. Who I am. What I do.
1. Quick survey: Who uses these services?
    1. Online Shopping
    2. Facebook, reddit, StackOverflow
    3. Online Banking
    4. Skype, Hangouts, or other realtime applications
    5. Online gaming
    6. E-mail
    7. Texting
1. What is the Internet, what is the World Wide Web?
1. Which of the survey options use the Internet? Which use the Web?
1. Share Google Doc version of the agenda. Read through the rest of the agenda.
1. "A quick connection" Python exercise.
    1. On two connected computers, develop this app:
        1. Connects to hardcoded IP address and socket for TCP
        2. Reads in characters from STDIN
        3. Sends characters across socket
        4. Prints any characters it receives
1. What we've used so far:
    1. **TCP/IP**  - "TCP over IP" Transmission protocol
    2. Packets - We don't ever see them, but they're flying.
    3. Python  - Normal Python! It's built for this!
    4. Address - We hardcoded these, how else could we find them?
    5. IO Loop - Common pattern, wait while the world catches up to the code.
    6. Internet connection - Once we're connected, anything's possible.
1. Brainstorm: What could you make with these tools alone?
1. Good time for an intermission
1. The World Wide Web
    1. HTTP over TCP/IP. [Spec](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html)
    2. Programs need only speak HTTP
    3. Services run on servers
    4. Users connect via clients
    5. Users might be autonomous, called "agents" or "bots"
1. "A simple server"
    1. Listen for HTTP on Port 8080 (Use 80 to publish to WWW)
    2. For every Request, send a Response with the String "Hello"
    3. Access it with a browser
1. What we've used here.
    1. HTTP works on top of TCP/IP, so somewhere the code looks the same as "A quick connection" above.
    2. The browser is the client. When you type something in the address bar, the URL is parsed, and eventually an HTTP GET Request is sent.
    3. Our server uses an I/O loop, and for every GET Request, calls our function to create the Response.
    4. The response we create is just text. It could be HTML, or CSS, or JavaScript, or ASCII art.
    5. Browsers interpret the text and URL to decide what to do with the response.
    6. We didn't use a domain name; we used an IP address. Domain names, e.g. `www.google.com`, are handled by DNS.

### Relevant, Brief History

|   Year   | Facts |
|  1940's  | Electronic, digital computers start being useful |
|  1960's  | Computers become small, fast, cheap, reliable |
|  1980's  | DARPA implements TCP/IP on ARPANET, becomes Internet, ISPs begin |
|  1990's  | PC's and the World Wide Web change the economy |
|  2000's  | Dot-com bubble pops, Twitter and Facebook create Web 2.0 |
|  2010's  | World increasingly reliant on World Wide Web, Net Neutrality |


