from rdflib import Graph, Namespace, RDF, RDFS, Literal

EX = Namespace("http://example.org/medical-kg/")

g = Graph()
g.bind("ex", EX)
g.bind("rdf", RDF)
g.bind("rdfs", RDFS)


# Classes from schema 
drug = EX.drug
disease = EX.disease
antibiotics = EX.antibiotics
antiInflammatory = EX.antiInflammatory
bacterialInfection = EX.bacterialInfection
inflammatoryDisease = EX.inflammatoryDisease

for cls in [
    drug,
    disease,
    antibiotics,
    antiInflammatory,
    bacterialInfection,
    inflammatoryDisease,
]:
    g.add((cls, RDF.type, RDFS.Class))

g.add((antibiotics, RDFS.subClassOf, drug))
g.add((antiInflammatory, RDFS.subClassOf, drug))

g.add((bacterialInfection, RDFS.subClassOf, disease))
g.add((inflammatoryDisease, RDFS.subClassOf, disease))



# Extra subclasses
extra_drug_subclasses = [
    "antiviral",
    "antifungal",
    "analgesic",
    "antihypertensive",
    "antidiabetic",
    "anticoagulant",
    "antidepressant",
    "bronchodilator",
]

extra_disease_subclasses = [
    "viralInfection",
    "fungalInfection",
    "painDisorder",
    "cardiovascularDisease",
    "metabolicDisease",
    "respiratoryDisease",
    "mentalHealthDisorder",
    "gastrointestinalDisease",
]

for cls_name in extra_drug_subclasses:
    cls = EX[cls_name]
    g.add((cls, RDF.type, RDFS.Class))
    g.add((cls, RDFS.subClassOf, drug))

for cls_name in extra_disease_subclasses:
    cls = EX[cls_name]
    g.add((cls, RDF.type, RDFS.Class))
    g.add((cls, RDFS.subClassOf, disease))

drug_subclasses = [
    "antibiotics",
    "antiInflammatory",
    *extra_drug_subclasses,
]

disease_subclasses = [
    "bacterialInfection",
    "inflammatoryDisease",
    *extra_disease_subclasses,
]

# Properties
getAffectedBy = EX.getAffectedBy
effect = EX.effect
treats = EX.treats
relieves = EX.relieves
worsen = EX.worsen

for prop in [getAffectedBy, effect, treats, relieves, worsen]:
    g.add((prop, RDF.type, RDF.Property))

# General relationship: drug affects disease
g.add((getAffectedBy, RDFS.domain, drug))
g.add((getAffectedBy, RDFS.range, disease))

# effect is a general kind of getAffectedBy
g.add((effect, RDFS.subPropertyOf, getAffectedBy))
g.add((effect, RDFS.domain, drug))
g.add((effect, RDFS.range, disease))

# Specific effects
for prop in [treats, relieves, worsen]:
    g.add((prop, RDFS.subPropertyOf, effect))
    g.add((prop, RDFS.domain, drug))
    g.add((prop, RDFS.range, disease))
 
# Required instances and facts from the lab
required_instances = [
    (EX.IBUPROFEN, antiInflammatory, "IBUPROFEN"),
    (EX.AMOXICILLIN, antibiotics, "AMOXICILLIN"),
    (EX.ARTHRITIS, inflammatoryDisease, "ARTHRITIS"),
    (EX.BACTERIALINFECTION, bacterialInfection, "BACTERIAL INFECTION"),
    (EX.GASTRICULCER, EX.gastrointestinalDisease, "GASTRIC ULCER"),
]

for instance, cls, label in required_instances:
    g.add((instance, RDF.type, cls))
    g.add((instance, RDFS.label, Literal(label)))

g.add((EX.IBUPROFEN, relieves, EX.ARTHRITIS))
g.add((EX.AMOXICILLIN, treats, EX.BACTERIALINFECTION))
g.add((EX.IBUPROFEN, worsen, EX.GASTRICULCER))

# Additional instances and relationships to enrich the knowledge graph
named_drugs = [
    ("AZITHROMYCIN", "antibiotics"),
    ("CIPROFLOXACIN", "antibiotics"),
    ("DOXYCYCLINE", "antibiotics"),
    ("NAPROXEN", "antiInflammatory"),
    ("ASPIRIN", "antiInflammatory"),
    ("PREDNISONE", "antiInflammatory"),
    ("ACYCLOVIR", "antiviral"),
    ("OSELTAMIVIR", "antiviral"),
    ("FLUCONAZOLE", "antifungal"),
    ("TERBINAFINE", "antifungal"),
    ("PARACETAMOL", "analgesic"),
    ("MORPHINE", "analgesic"),
    ("LISINOPRIL", "antihypertensive"),
    ("AMLODIPINE", "antihypertensive"),
    ("METFORMIN", "antidiabetic"),
    ("INSULIN", "antidiabetic"),
    ("WARFARIN", "anticoagulant"),
    ("HEPARIN", "anticoagulant"),
    ("SERTRALINE", "antidepressant"),
    ("FLUOXETINE", "antidepressant"),
    ("SALBUTAMOL", "bronchodilator"),
    ("FORMOTEROL", "bronchodilator"),
]

named_diseases = [
    ("PNEUMONIA", "bacterialInfection"),
    ("TUBERCULOSIS", "bacterialInfection"),
    ("STREPTHROAT", "bacterialInfection"),
    ("CROHNSDISEASE", "inflammatoryDisease"),
    ("PSORIASIS", "inflammatoryDisease"),
    ("LUPUS", "inflammatoryDisease"),
    ("INFLUENZA", "viralInfection"),
    ("HERPES", "viralInfection"),
    ("COVID19", "viralInfection"),
    ("ATHLETESFOOT", "fungalInfection"),
    ("CANDIDIASIS", "fungalInfection"),
    ("MIGRAINE", "painDisorder"),
    ("BACKPAIN", "painDisorder"),
    ("HYPERTENSION", "cardiovascularDisease"),
    ("HEARTFAILURE", "cardiovascularDisease"),
    ("TYPE2DIABETES", "metabolicDisease"),
    ("TYPE1DIABETES", "metabolicDisease"),
    ("ASTHMA", "respiratoryDisease"),
    ("COPD", "respiratoryDisease"),
    ("DEPRESSION", "mentalHealthDisorder"),
    ("ANXIETY", "mentalHealthDisorder"),
    ("GERD", "gastrointestinalDisease"),
]

for name, cls_name in named_drugs:
    g.add((EX[name], RDF.type, EX[cls_name]))
    g.add((EX[name], RDFS.label, Literal(name)))

for name, cls_name in named_diseases:
    g.add((EX[name], RDF.type, EX[cls_name]))
    g.add((EX[name], RDFS.label, Literal(name)))

relationships = [
    ("AMOXICILLIN", "treats", "PNEUMONIA"),
    ("DOXYCYCLINE", "treats", "TUBERCULOSIS"),
    ("AZITHROMYCIN", "treats", "STREPTHROAT"),
    ("CIPROFLOXACIN", "treats", "BACTERIALINFECTION"),
    ("IBUPROFEN", "relieves", "ARTHRITIS"),
    ("NAPROXEN", "relieves", "ARTHRITIS"),
    ("PREDNISONE", "relieves", "CROHNSDISEASE"),
    ("ASPIRIN", "relieves", "BACKPAIN"),
    ("ACYCLOVIR", "treats", "HERPES"),
    ("OSELTAMIVIR", "treats", "INFLUENZA"),
    ("FLUCONAZOLE", "treats", "CANDIDIASIS"),
    ("TERBINAFINE", "treats", "ATHLETESFOOT"),
    ("PARACETAMOL", "relieves", "MIGRAINE"),
    ("MORPHINE", "relieves", "BACKPAIN"),
    ("LISINOPRIL", "treats", "HYPERTENSION"),
    ("AMLODIPINE", "treats", "HEARTFAILURE"),
    ("METFORMIN", "treats", "TYPE2DIABETES"),
    ("INSULIN", "treats", "TYPE1DIABETES"),
    ("SALBUTAMOL", "relieves", "ASTHMA"),
    ("FORMOTEROL", "relieves", "COPD"),
    ("SERTRALINE", "treats", "DEPRESSION"),
    ("FLUOXETINE", "treats", "ANXIETY"),
    ("IBUPROFEN", "worsen", "GASTRICULCER"),
    ("ASPIRIN", "worsen", "GERD"),
    ("NAPROXEN", "worsen", "GASTRICULCER"),
]

for drug_name, relation_name, disease_name in relationships:
    g.add((EX[drug_name], EX[relation_name], EX[disease_name]))

# Add 100 relationships between the named drugs and diseases
for i in range(1, 101):
    drug_instance = EX[f"DRUGINSTANCE{i}"]
    disease_instance = EX[f"DISEASEINSTANCE{i}"]

    drug_class = EX[drug_subclasses[i % len(drug_subclasses)]]
    disease_class = EX[disease_subclasses[i % len(disease_subclasses)]]

    g.add((drug_instance, RDF.type, drug_class))
    g.add((drug_instance, RDFS.label, Literal(f"DRUG INSTANCE {i}")))

    g.add((disease_instance, RDF.type, disease_class))
    g.add((disease_instance, RDFS.label, Literal(f"DISEASE INSTANCE {i}")))

    if i % 3 == 0:
        g.add((drug_instance, treats, disease_instance))
    elif i % 3 == 1:
        g.add((drug_instance, relieves, disease_instance))
    else:
        g.add((drug_instance, worsen, disease_instance))

# Serialize the graph to a Turtle file
output_file = "medical_kg.ttl"
g.serialize(destination=output_file, format="turtle")

print(f"Created {output_file}")
print(f"Total explicit triples: {len(g)}")