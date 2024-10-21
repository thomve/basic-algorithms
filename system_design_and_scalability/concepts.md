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

* In-memory cache is a simple key-value pairing and typically sits between the application layer

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
