import sys

# path to RDFLib dir
sys.path.append('lib/rdflib-3.0.0/')

from rdflib import Graph
from rdflib import URIRef, Literal, BNode
from rdflib import Namespace, RDF

# create a graph
store = Graph()

# create a namespace object for the Friend Of A Friend namespace
FOAF = Namespace("http://xmlns.com/foaf/0.1/")

# create an identifier to use as the subject for Alice
alice = BNode()

# add triples for Alice using store's add method
store.add((alice, RDF.type, FOAF["Person"]))
store.add((alice, FOAF["givenName"], Literal("Alice", lang="en")))
store.add((alice, FOAF["familyName"], Literal("Smith", lang="en")))

# create an identifier to use as the subject for Bob
bob = BNode()

# add triples using store's add method.
store.add((bob, RDF.type, FOAF["Person"]))
store.add((bob, FOAF["givenName"], Literal("Bob", lang="en")))
store.add((bob, FOAF["familyName"], Literal("Jones", lang="en")))
store.add((alice, FOAF["knows"], bob))

# iterate over all triples in store and print them out.
print "--- printing raw triples ---"
for s, p, o in store:
   print s, p, o
