"# PythonKafkaElasticSearch"

Internal Search Engine using Kafka Messaging and Elastic Search
=================================================================

Description
=================================================
This is internal search Engine, which is accomplished using "Kafka Server" and "ElasticSearch" tool for 
Indexing document. Python Flask as middle ware interface between UI and ElasticSearch


Prerequisites
================
Python 64bit 2.7
Using Python pip install following packages:
1. pip install flask
2. pip install json
3. pip install elasticsearch
4. pip install kafka-python

Installation
===========
1. CentOS7
2. Download and untar elasticSearch - https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html
2. Install ElasticSearch - https://dzone.com/articles/elasticsearch-setup-and-configuration
3. Following Getting started with Elastic Search - https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html
4. Download and configure kafka server on centos - https://kafka.apache.org/downloads
5. Start elastic search server and kafka server (Configure both with proper instruction available on internet)


Getting Started
=================
1. Using non-root user, start elastic search
2. Using non-root/root user, start zookeper and kafka server
3. Start "searchFlaskElasticSearchKafka.py"
4. Open "searchIndex.html"
5. Enter the following:
    - Name of the Document or Link in "Name" field
    - Link of webpage in "Link" field
    - Keywords using we want to search this document in "Keyword" field
    - Incremental value of DocId in "DocId" field
    - Click on "Submit"
6. Will get response from elastic search, where response will be either "created" or "updated"
7. Verify newly indexed document using either, search by "Name" or "Keyword"
8. On response of above, you will get hyperlink of indexed document with description

Created by
===========
- Virendra Ukey
- Email : viruukey@gmail.com 
