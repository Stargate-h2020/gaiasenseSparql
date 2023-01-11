# Access Gaiasense service as Linked Data

Gaiasense API has been exposed as Linked Data, adding a layer on top of the REST API that allows to access API data as Linked Data on the fly. Data on the service is not duplicated, and its only translated on the fly. 

The translation is done by the Ephedra component of Metaphactory application. Metaphactory exposes a SPARQL endpoint which can be used to access the linked data as any other semantic data source in a triplestore. Hence, this SPARQL endpoint can be used, for example, from different applications/systems or from the command line.

To play with this Linked Data use the Metaphactory [Sparql GUI](http://metaphactory.foodie-cloud.org/sparql). Note: You need to select repository "ephedra"

Some example queries to access the three main endpoints are provide in this repository.

## querying the data from command line

You can query the data from the command line passing the query directly in the command or passing a query file as parameter as below.

### send query in command

```
curl -i -X POST -H "Accept:application/sparql-results+json" -H "Content-Type:application/sparql-query" -d "\
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
PREFIX gs-api: <https://w3id.org/demeter/agri/ext/gaiasense#>\
PREFIX sosa: <http://www.w3.org/ns/sosa/>\
PREFIX fiware: <https://uri.fiware.org/ns/data-models#>\
SELECT * WHERE { \
  BIND(\"2022-08-25\"^^xsd:date as ?inputfromdate) . \
  BIND(\"2022-08-26\"^^xsd:date as ?inputtodate) . \
  SERVICE <http://www.metaphacts.com/ontologies/platform/repository/federation#gaiasenseMeasurements> { \
     ?results fiware:validFrom ?inputfromdate . \
     ?results fiware:validTo ?inputtodate . \
     ?results sosa:resultTime ?m_date . \
     ?results gs-api:nplwrh1 ?nplwrh1 . \
     ?results gs-api:nplwrh2 ?nplwrh2 . \
     ?results gs-api:wsht30_rh ?wsht30_rh . \
     ?results gs-api:uv ?uv . \
  }} LIMIT 100" 'http://metaphactory.foodie-cloud.org/sparql?repository=ephedra'
```

### send query in file

```
curl -i -X POST  -H "Accept:application/sparql-results+json" -H "Content-Type:application/sparql-query"  --data-binary "@/path/to/file.sparql" 'http://metaphactory.foodie-cloud.org/sparql?repository=ephedra'
```
