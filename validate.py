import sys
from pyshacl import validate
from rdflib import Graph


shapes_graph = Graph().parse("../loci-data-profile/validator.ttl")
shapes_graph += Graph().parse("validator.ttl")

v = validate(sys.argv[1], shapes_graph=shapes_graph)

print(v)
