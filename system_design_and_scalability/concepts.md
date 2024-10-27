# Key concepts

## Horizontal scaling vs Vertical Scaling

* vertical: increase the resources of a specific node
* horizontal: increase the number of nodes.

## Load balancer

* allows the system to distribute the load evenly

## Database denormalization and nosql

Joins operation in relational database does not scale well. To mitigate this:
* denormalization: adding redundant information into a database to speed up reads
* opt for a NoSQL database as it is designed to scale better

## Database partitioning (sharding)

* splits the data across multiple machines while ensuring there is a way of figuring out which data is on which machine
* vertical partitioning = partitioning by feature
* key-based partitioning: this uses some part of the data (ID for instance) to partition it. For instance: put data on mod(key, n)
* directory-based partitioning: maintains a lookup table for where the data can be found

## Caching

### In-memory caching 

* a simple key-value pairing and typically sits between the application layer
* stores data in the system's main memory (RAM)
* Example Technologies: Redis, Memcached

### Distributed caching

* involves caching data across multiple nodes or servers in a network
* Ideal for applications with high scalability and fault tolerance requirements, such as large-scale web applications and microservices architectures

## Asynchronous processing & queues

* slow operations should ideally be done asynchronously
* sometimes, we can preprocess (for instance, a queue of jobs to be done that update some parts of a website)

## Network metrics

* bandwith: maximum amount of data that can be transferred in a unit of time (bits per sec)
* throughput: actual data that is transferred
* latency: delay between the sender and receiver

## MapReduce

* map takes in some data and emits a key-value pair
* reduce takes a key and a set of associated values and reduces them in some way, emitting a new key-value

Here below an example of a map-reduce pseudocode:

```
// Map function (executed on each data chunk)
function Map(key, value):
    // key: document name or line number
    // value: text content of the document or line
    
    // Split value into words
    words = split(value)
    
    // Emit each word with a count of 1
    for each word in words:
        Emit(word, 1)  // Output key-value pair (word, 1)

// Intermediate output after Map stage and before Reduce stage
// Example: (word1, [1, 1, 1]), (word2, [1, 1]), ...

// Reduce function (executed on each group of intermediate data)
function Reduce(key, values):
    // key: word
    // values: list of counts for this word (e.g., [1, 1, 1])
    
    // Sum all values to get the total count for this word
    total = 0
    for each count in values:
        total = total + count
    
    // Emit the word and its total count
    Emit(key, total)  // Output key-value pair (word, total)

// Final output example
// (word1, 3), (word2, 2), ...
```