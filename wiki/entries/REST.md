REST stands for "**Re**presentative **S**tate **T**ransfer", a software architectural style that defines a set of constraints to be used for creating **Web services**. Web services that conform to the REST architectural style, called **RESTful** Web services, provide interoperability between computer systems on the internet. RESTful Web services allow the requesting systems to access and manipulate textual representations of Web resources by using a uniform and predefined set of stateless operations. 

Six guiding architectural constraints defining a RESTful system
    
 - **Statelessness**: client context not stored on server between requests.  Example: cookies
	
 - **Client-server architecture**: seperation of client user interface from server functions
	
 - **Layered system**: Layers of Intermediary servers enhance system [scalability](https://en.wikipedia.org/wiki/Scalability "Scalability") by enabling load balancing, and  providing shared caches. Security can abstracted by layering on top of web services to clearly separate business functions from security.
	
 - **Cacheability**: Caching is absolutely essential for practical scalability, and performance of client-server interactions.

 - **Uniform interface**: decouples the architecture, which enables system components  to be designed, and evolve independently.  Example: [JSON](JSON)

 - **Code on demand**:  Customizing the functionality of clients by retrýeving client-side code from the server.