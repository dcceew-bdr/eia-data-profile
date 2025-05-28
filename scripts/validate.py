import sys
from pyshacl import validate
from rdflib import Graph


# shapes_graph = Graph().parse("../loci-data-profile/validator.ttl")
shapes_graph = Graph()
shapes_graph += Graph().parse("validator.ttl")

data_graph = Graph().parse("../vocabs/envthes-concepts.ttl")
data_graph += Graph().parse(sys.argv[1])

v = validate(data_graph, shacl_graph=shapes_graph)

print(v[2])
