# SDM_Lab2
Lab 2 on Knowledge Graphs

Important links
https://drive.google.com/file/d/1x7rTpYwlns187eCJKDJCr90EjJK-Kxld/view?usp=sharing
https://www.overleaf.com/3782195653zjsmrpvxkkdc#ab4d28

## Queries C

### SPARQL

#### List all drugs
PREFIX ex: <http://example.org/medical-kg/>

SELECT ?drug 
WHERE {
?drug a ex:drug .
}

#### List all diseases
PREFIX ex: <http://example.org/medical-kg/>

SELECT ?disease 
WHERE {
  ?disease a ex:disease .
}

### All pairs of drugs and diseases
PREFIX ex: <http://example.org/medical-kg/>

SELECT ?drug ?disease 
WHERE {
  ?drug ex:getAffectedBy ?disease .
}


### NEO4J

#### List of drugs

MATCH (n:Drug) RETURN n

#### List of diseases

MATCH (n:Disease) RETURN n

#### All pairs of drugs and diseases

MATCH (drug:Drug)-[:TREATS|RELIEVES|WORSENS]->(disease:Disease)
RETURN DISTINCT drug.name AS drug,
                disease.name AS disease
ORDER BY drug, disease;