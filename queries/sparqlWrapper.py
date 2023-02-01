import sys
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    "http://metaphactory.foodie-cloud.org/sparql"
)

sparql.addParameter("repository", "ephedra")
sparql.setReturnFormat(JSON)

def agronomy_query():
    sparql.setQuery("""
        #PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX osm: <http://www.metaphacts.com/ontologies/osm#>
        PREFIX gs-api: <https://w3id.org/demeter/agri/ext/gaiasense#>
        PREFIX sosa: <http://www.w3.org/ns/sosa/>
        PREFIX fiware: <https://uri.fiware.org/ns/data-models#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#>
        PREFIX geo84: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        SELECT * WHERE {
        BIND("en"^^xsd:string as ?inputlanguage)
        BIND("205"^^xsd:string as ?inputlocationid)
        BIND("100"^^xsd:integer as ?inputradius)
        BIND("1"^^xsd:integer as ?inputlimit)
        SERVICE <http://www.metaphacts.com/ontologies/platform/repository/federation#gaiasenseAgronomy> {
            ## inputs
                ?results gs-api:locationIdInput ?inputlocationid .
                ?results gs-api:radiusInput ?inputradius .
                ?results gs-api:limit  ?inputlimit .
                ?results gs-api:language ?inputlanguage .
            ## outputs    
                ?results gs-api:parcelId ?parcelId .
                #?results gs-api:locationId ?locationid .
                ?results gs-api:parcelToponym ?parcelToponym .
                ?results dc:identifier ?parcelIdentifier .
                ?results fiware:name ?parcelPrefecture .
                ?results geo:asWKT ?polygon .
                ?results geo84:long ?longitude .
                ?results geo84:lat ?latitude .
                ?results foaf:name ?adminLastname .
                ?results gs-api:phValue ?phValue .
                ?results gs-api:salinityValue ?salinityValue .
                ?results fiware:category ?rocrDescription .
                    
            }
        } LIMIT 100
        """)
    try:
       return sparql.queryAndConvert()
    except Exception as e:
        print(e)


def sprays_query():
    sparql.setQuery("""
        #PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX osm: <http://www.metaphacts.com/ontologies/osm#>
        PREFIX gs-api: <https://w3id.org/demeter/agri/ext/gaiasense#>
        PREFIX sosa: <http://www.w3.org/ns/sosa/>
        PREFIX fiware: <https://uri.fiware.org/ns/data-models#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#>
        PREFIX geo84: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        PREFIX foodie: <http://foodie-cloud.com/model/foodie#>
        PREFIX prov: <http://www.w3.org/ns/prov#>
        PREFIX unit: <http://qudt.org/vocab/unit/>
        SELECT * WHERE {
        BIND("sprays"^^xsd:string as ?inputevent)
        BIND("205"^^xsd:string as ?inputlocationid)
        BIND("2021-01-01"^^xsd:date as ?inputfromdate)
        BIND("2022-08-26"^^xsd:date as ?inputtodate)
        SERVICE <http://www.metaphacts.com/ontologies/platform/repository/federation#gaiasenseEvents> {
            ## inputs
                ?results gs-api:locationIdInput ?inputlocationid .
                ?results gs-api:eventType ?inputevent .
                ?results fiware:validFrom ?inputfromdate .
                ?results fiware:validTo ?inputtodate .
            
            ## outputs    
                ?results gs-api:parcelId ?parcelId .
                ?results sosa:resultTime ?date .
                ?results foodie:code ?osdeCode .
                ?results foodie:productName ?drugName .
                ?results gs-api:activeSubstance ?activeSubstance .
                ?results gs-api:dose ?dose .
                ?results gs-api:unit ?unit .
                ?results gs-api:target ?target .
                ?results fiware:description ?remarks .     
            }
        } LIMIT 100
        """)
    try:
       return sparql.queryAndConvert()
    except Exception as e:
        print(e)

def irrigations_query():
    sparql.setQuery("""
        #PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX osm: <http://www.metaphacts.com/ontologies/osm#>
        PREFIX gs-api: <https://w3id.org/demeter/agri/ext/gaiasense#>
        PREFIX sosa: <http://www.w3.org/ns/sosa/>
        PREFIX fiware: <https://uri.fiware.org/ns/data-models#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#>
        PREFIX geo84: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        PREFIX foodie: <http://foodie-cloud.com/model/foodie#>
        PREFIX prov: <http://www.w3.org/ns/prov#>
        SELECT * WHERE {
        BIND("irrigations"^^xsd:string as ?inputevent)
        BIND("205"^^xsd:string as ?inputlocationid)
        BIND("2021-01-01"^^xsd:date as ?inputfromdate)
        BIND("2022-08-26"^^xsd:date as ?inputtodate)
        SERVICE <http://www.metaphacts.com/ontologies/platform/repository/federation#gaiasenseEvents> {
            ## inputs
                ?results gs-api:locationIdInput ?inputlocationid .
                ?results gs-api:eventType ?inputevent .
                ?results fiware:validFrom ?inputfromdate .
                ?results fiware:validTo ?inputtodate .
            
            ## outputs    
                ?results gs-api:parcelId ?parcelId .
                ?results sosa:resultTime ?date .
                ?results prov:generatedAtTime ?startDateTime .
                ?results prov:invalidatedAtTime ?endDateTime .
                ?results foodie:code ?osdeCode .
                ?results gs-api:waterQuantity ?waterQuantity .
                ?results gs-api:irrigationSystem ?irrigationSystem .
                ?results fiware:description ?remarks .
                ?results gs-api:unit ?unit .
                ?results gs-api:irigHour ?irigHour .
                    
            }
        } LIMIT 100
        """)
    try:
       return sparql.queryAndConvert()
    except Exception as e:
        print(e)

def harvest_query():
    sparql.setQuery("""
        #PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX osm: <http://www.metaphacts.com/ontologies/osm#>
        PREFIX gs-api: <https://w3id.org/demeter/agri/ext/gaiasense#>
        PREFIX sosa: <http://www.w3.org/ns/sosa/>
        PREFIX fiware: <https://uri.fiware.org/ns/data-models#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#>
        PREFIX geo84: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        PREFIX foodie: <http://foodie-cloud.com/model/foodie#>
        SELECT * WHERE {
        BIND("harvest"^^xsd:string as ?inputevent)
        BIND("205"^^xsd:string as ?inputlocationid)
        BIND("2021-01-01"^^xsd:date as ?inputfromdate)
        BIND("2022-12-26"^^xsd:date as ?inputtodate)
        SERVICE <http://www.metaphacts.com/ontologies/platform/repository/federation#gaiasenseEvents> {
        ## inputs
            ?results gs-api:locationIdInput ?inputlocationid .
            ?results gs-api:eventType ?inputevent .
            ?results fiware:validFrom ?inputfromdate .
            ?results fiware:validTo ?inputtodate .
        
        ## outputs    
            ?results gs-api:parcelId ?parcelId .
            ?results sosa:resultTime ?date .
            ?results foodie:code ?osdeCode .
            ?results fiware:quantity ?quantity .
            ?results gs-api:magnSymbol ?magnSymbol .
            ?results fiware:description ?remarks .
            ?results gs-api:bucketCodes ?bucketCodes .
        }
    } LIMIT 100
    """)
    try:
       return sparql.queryAndConvert()
    except Exception as e:
        print(e)

def phaenological_stages_query():
    sparql.setQuery("""
        #PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX osm: <http://www.metaphacts.com/ontologies/osm#>
        PREFIX gs-api: <https://w3id.org/demeter/agri/ext/gaiasense#>
        PREFIX sosa: <http://www.w3.org/ns/sosa/>
        PREFIX fiware: <https://uri.fiware.org/ns/data-models#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#>
        PREFIX geo84: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        PREFIX foodie: <http://foodie-cloud.com/model/foodie#>
        SELECT * WHERE {
        BIND("phaenological_stages"^^xsd:string as ?inputevent)
        BIND("205"^^xsd:string as ?inputlocationid)
        BIND("2021-01-01"^^xsd:date as ?inputfromdate)
        BIND("2022-08-26"^^xsd:date as ?inputtodate)
        SERVICE <http://www.metaphacts.com/ontologies/platform/repository/federation#gaiasenseEvents> {
            ## inputs
                ?results gs-api:locationIdInput ?inputlocationid .
                ?results gs-api:eventType ?inputevent .
                #?results fiware:validFrom ?inputfromdate .
                #?results fiware:validTo ?inputtodate .    
            ## outputs    
                ?results gs-api:parcelId ?parcelId .
                ?results fiware:category ?crop .
                ?results foodie:variety ?variety .
                ?results gs-api:stage ?stage .
                ?results fiware:startedAt ?from .
                ?results fiware:endedAt ?to .
            }
        }
    """)
    try:
       return sparql.queryAndConvert()
    except Exception as e:
        print(e)


def sensor_measurements_query():
    sparql.setQuery("""
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX osm: <http://www.metaphacts.com/ontologies/osm#>
        PREFIX gs-api: <https://w3id.org/demeter/agri/ext/gaiasense#>
        PREFIX sosa: <http://www.w3.org/ns/sosa/>
        PREFIX fiware: <https://uri.fiware.org/ns/data-models#>
        PREFIX geo84: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        SELECT * WHERE {
        BIND("2022-08-25"^^xsd:date as ?inputfromdate)
        BIND("2022-08-26"^^xsd:date as ?inputtodate)
        #BIND("37.9157894"^^xsd:decimal as ?inputlong)
        #BIND("22.8124069"^^xsd:decimal as ?inputlat)
        ##default values for other inputs as below
        #BIND("nplwrh1, nplwrh2, wsht30_rh, uv, pyranometer, pressure, velocity, gust, vr_winddir, rain, nplwtemp1, nplwtemp2, wsht30_temp, nplwlw1, nplwlw"^^xsd:string as ?inputsensors)
        #BIND("10"^^xsd:integer as ?inputlimit)
        #BIND("205"^^xsd:integer as ?inputlocationid)
        #BIND("100"^^xsd:integer as ?inputradius)
        #BIND("0"^^xsd:integer as ?inputoffset)
        #BIND("asc"^^xsd:string as ?inputorder)
        SERVICE <http://www.metaphacts.com/ontologies/platform/repository/federation#gaiasenseMeasurements> {
            ## inputs
                ?results fiware:validFrom ?inputfromdate .
                ?results fiware:validTo ?inputtodate .
                #?results gs-api:longInput ?inputlong .
                #?results gs-api:latInput ?inputlat .
                ##default values
                #?results sosa:madeBySensor ?inputsensors .
                #?results gs-api:limit ?inputlimit .
                #?results gs-api:locationIdInput ?inputlocationid .
                #?results gs-api:radiusInput ?inputradius .
                #?results gs-api:offset ?inputoffset .
                #?results gs-api:orderBy ?inputorder .
                
            ## outputs    
                ?results sosa:resultTime ?m_date .
                ?results gs-api:nplwrh1 ?nplwrh1 .
                ?results gs-api:nplwrh2 ?nplwrh2 .
                ?results gs-api:wsht30_rh ?wsht30_rh .
                ?results gs-api:uv ?uv .
                #?results gs-api:pyranometer ?pyranometer .
                #?results gs-api:pressure ?pressure .
                #?results gs-api:velocity ?velocity .
                #?results gs-api:gust ?gust .
                #?results gs-api:vr_winddir ?vr_winddir .
                #?results gs-api:rain ?rain .
                #?results gs-api:nplwtemp1 ?nplwtemp1 .
                #?results gs-api:nplwtemp2 ?nplwtemp2 .
                #?results gs-api:wsht30_temp ?wsht30_temp .
                #?results gs-api:nplwlw1 ?nplwlw1 .
        }
        SERVICE <http://www.metaphacts.com/ontologies/platform/repository/federation#gaiasenseMeasurementsLocation> {
            ## inputs
                ?results fiware:validFrom ?inputfromdate .
                ?results fiware:validTo ?inputtodate .
                #?results gs-api:longInput ?inputlong .
                #?results gs-api:latInput ?inputlat .
                ##default values
                #?results sosa:madeBySensor ?inputsensors .
                #?results gs-api:limit ?inputlimit .
                #?results gs-api:locationIdInput ?inputlocationid .
                #?results gs-api:radiusInput ?inputradius .
                #?results gs-api:offset ?inputoffset .
                #?results gs-api:orderBy ?inputorder .
                
            ## outputs
                ?results dc:identifier ?locationIdOutput .
                ?results geo84:long ?longitud .
                ?results geo84:lat ?latitude .
                ?results geo84:alt ?altitude .
                ?results fiware:name ?name .
                ?results gs-api:toponym ?toponym .
                ?results fiware:status ?status .
            }
        } LIMIT 100
    """)
    try:
        return sparql.queryAndConvert()
    except Exception as e:
        print(e)

def main():
    queryType = None
    if len( sys.argv ) > 1:
        queryType = sys.argv[1]
        if queryType == "agronomy":
            print("Running agronomy query...")
            res = agronomy_query()
            print("Reuslt:\n",res)
        elif queryType == "harvest":
            print("Running harvest query...")
            res = harvest_query()
            print("Reuslt:\n",res)
        elif queryType == "irrigations":
            print("Running irrigations query...")
            res = irrigations_query()
            print("Reuslt:\n",res)
        elif queryType == "phaenological_stages":
            print("Running phaenological stages query...")
            res = phaenological_stages_query()
            print("Reuslt:\n",res)
        elif queryType == "sprays":
            print("Running sprays query...")
            res = sprays_query()
            print("Reuslt:\n",res)
        elif queryType == "sensor_measurements":
            print("Running sensor measurements query:")
            res = sensor_measurements_query()
            for r in res["results"]["bindings"]:
                print(r)
        else:
            print("Not a valid query type.")
            print("Choose one from [agronomy, harvest, irrigations, sprays, sensor_measurements, phaenological_stages]")
    else:
        print("Please provide a query type as argument.")
        print("Choose one from [agronomy, harvest, irrigations, sprays, sensor_measurements, phaenological_stages]")
        
if __name__ == "__main__":
    main()

