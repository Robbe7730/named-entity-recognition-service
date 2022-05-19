from helpers import update

@app.route("/annotate", methods=["POST"])
def annotate():
    return str(update("""
        PREFIX  ttrpg: <https://w3id.org/TTRpg#>
        PREFIX  olia: <http://purl.org/olia/olia.owl#>
        PREFIX  itsrdf: <http://www.w3.org/2005/11/its/rdf#>
        PREFIX  nif:  <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
        PREFIX  foaf: <http://xmlns.com/foaf/0.1/>

        INSERT {
          GRAPH ?g {
            ?string itsrdf:taIdentRef ?character .
          }
        }
        WHERE
          { GRAPH ?g
              { ?string   nif:posTag    olia:ProperNoun ;
                          nif:isString  ?characterName .
                ?character  a           ttrpg:Character ;
                          foaf:name     ?characterName
              }
          }
    """))
