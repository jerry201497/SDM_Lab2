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

### 
PREFIX ex: <http://example.org/medical-kg/>

SELECT ?drug ?disease 
WHERE {
  ?drug ex:getAffectedBy ?disease .
}