from __future__ import print_function
from flask import Flask, render_template, request,jsonify, Response, json
from elasticsearch import Elasticsearch
from ordered_set import OrderedSet
from kafka import KafkaProducer, KafkaConsumer,SimpleProducer,KafkaClient
import json
import simplejson

app = Flask(__name__)

def producer():
    producer = KafkaProducer(bootstrap_servers=['kafkaBroker:9092'])
    return producer

def consumer():
    consumer = KafkaConsumer(bootstrap_servers=['kafkaBroker:9092'],
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=1000,
                             group_id=1,
                             enable_auto_commit=True,
                             auto_commit_interval_ms=1000)
    return consumer

@app.route('/index', methods=['POST'])
def index():
    data = {}
    data["docId"] = request.form['docId']
    data["name"] = request.form['name']
    link = request.form['link']
    link = "<a href=\"" + link + "\"" + ">" + data["name"] + "</a>" + "<br/>" + link
    data["link"] = link
    data["keyword"] = request.form['keyword']
    prod = producer()
    dataJson = json.dumps(data)
    prod.send("search", value=dataJson)
    cons = consumer()
    cons.subscribe(["search"])
    for message in cons:
        print(message.value)
        val = json.loads(message.value)
    print(val)
    es = Elasticsearch([{'host': 'ElasticSearcIP', 'port': 9200}])
    res = es.index(index="qa_kb", doc_type="link", id=val["docId"], body={"name": val["name"], "link": val["link"],
                                                                       "keyword": val["keyword"]})
    return res['result']

@app.route('/search', methods=['POST'])
def search():
    searchTearm = request.form['searchbox']
    es = Elasticsearch([{'host':'ElasticsearchIP','port':9200}])
    res = es.search(index="qa_kb", doc_type="link", body={"query": {"match": {"keyword": searchTearm}}})
    if res["hits"]["hits"]:
        a = []
        for i in res["hits"]["hits"]:
            a.append(i['_source']['link'])
        list_set = OrderedSet(a)
        str1 = '<br/><br/>'.join(map(str, list_set))
        return  str1
    else:
        return "No search found"

@app.route('/name', methods=['POST'])
def name():
    searchTearm = request.form['namesearchbox']
    es = Elasticsearch([{'host':'ElasticsearchIP','port':9200}])
    res = es.search(index="qa_kb", doc_type="link", body={"query": {"match": {"name": searchTearm}}})
    if res["hits"]["hits"]:
        a = []
        for i in res["hits"]["hits"]:
            a.append(i['_source']['link'])
        list_set = OrderedSet(a)
        str1 = '<br/>'.join(map(str, list_set))
        return  str1
    else:
        return "No search found"

if __name__ == '__main__':
   app.run(debug = True)

