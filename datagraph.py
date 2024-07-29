from json import load
from rdflib import Graph, URIRef, Namespace, Literal, RDF
from sparql_dataframe import get
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

# Function to create a graph from a .json file.
def create_datagraph(graphUrl, json_file): 
    with open(json_file) as f:
        list_of_dict = load(f)

    # Endpoint needed to connect to the graph
    endpoint = graphUrl + "sparql"

    # Namespace of SocioPolitical Meme Perspectivisation Ontology and
    # base url for project uris'.
    spomepo = Namespace("https://github.com/Yogi-Bubu-Exam/MemOnPology/raw/main/SPoMePO.owl#")
    project_url = "https://github.com/Yogi-Bubu-Exam/MemOnPology/"

    # Creating graph, binding namespaces
    graphData = Graph()
    graphData.bind("spomepo", spomepo)
    graphData.bind("project", project_url)

    # Creating classes
    Caption = URIRef(spomepo.Caption)
    Connotation = URIRef(spomepo.Connotation)
    GraphicContent = URIRef(spomepo.GraphicContent)
    Template = URIRef(spomepo.Template)
    Comparative = URIRef(spomepo.ComparativeTemplate)
    ChangeMyMind = URIRef(spomepo.ChangeMyMindTemplate)
    PoliticalCompass = URIRef(spomepo.PoliticalCompassTemplate)
    Macro = URIRef(spomepo.PoliticalImageMacro)
    SocialGroup = URIRef(spomepo.SocialGroup)
    Politician = URIRef(spomepo.Politician)
    PoliticalSupporter = URIRef(spomepo.PoliticalSupporter)
    PoliticalActivity = URIRef(spomepo.PoliticalActivity)
    PersonalOpinion = URIRef(spomepo.PersonalOpinion)
    ControversialOpinion = URIRef(spomepo.ControversialOpinion)
    NonTroll = URIRef(spomepo.NonTroll)
    NonOpinionated = URIRef(spomepo.NonOpinionated)
    Opinionated = URIRef(spomepo.Opinionated)
    Troll = URIRef(spomepo.Troll)
    tNonOpinionated = URIRef(spomepo.tNonOpinionated)
    tOpinionated = URIRef(spomepo.tOpinionated)
    tOpinionated = URIRef(spomepo.tOpinionated)
    SocioPoliticalMeme = URIRef(spomepo.SocioPoliticalMeme)
    ControversialMeme = URIRef(spomepo.ControversialMeme)
    MockingJuxtapositionMeme = URIRef(spomepo.MockinJuxtapositionMeme)
    NeutralJuxtapositionMeme = URIRef(spomepo.NeutralJuxtapositionMeme)
    SatyricalMeme = URIRef(spomepo.SatyricalMeme)
    SupportiveMeme = URIRef(spomepo.SupportiveMeme)
        

    # Creating relations
    hasValue = URIRef(spomepo.hasValue)
    hasCaption = URIRef(spomepo.hasCaption)
    hasConnotation = URIRef(spomepo.hasConnotation)
    hasGraphicContent = URIRef(spomepo.hasGraphicContent)
    hasTemplate = URIRef(spomepo.hasTemplate)
    expresses = URIRef(spomepo.expresses)
    perspectivisedAs = URIRef(spomepo.perspectivisedAs)
    towards = URIRef(spomepo.towards)


    n = 0
    meme_uri = URIRef(project_url + "meme_")
    caption = URIRef(project_url + "caption_")
    connotation = URIRef(project_url + "connotation_")
    graphicContent = URIRef(project_url + "graphicContent_")
    template = URIRef(project_url + "template_")
    eventuality = URIRef(project_url + "eventuality_")
    attitude = URIRef(project_url + "attitude_")
    
    
    # Adding triples to the graph
    for dict in list_of_dict:
        N = str(n)
        m = meme_uri + N
        ca = caption + N
        c = connotation + N
        g = graphicContent + N
        t = template + N
        e = eventuality + N
        a = attitude + N
        
        # Caption and Opinion
        graphData.add((m, hasCaption, ca))
        graphData.add((ca, RDF.type, Caption))
        if "controversial" in dict["opinion"]:
            graphData.add((ca, expresses, ControversialOpinion))
        elif "personal" in dict["opinion"]:
            graphData.add((ca, expresses, PersonalOpinion))
        graphData.add((ca, hasValue, Literal(dict["text"])))

        # Connotation
        graphData.add((m, hasConnotation, c))
        graphData.add((c, RDF.type, Connotation))
        graphData.add((c, hasValue, Literal(dict["connotation"])))

        # GraphicContent
        graphData.add((m, hasGraphicContent, g))
        graphData.add((g, RDF.type, GraphicContent))
        graphData.add((g, hasValue, Literal(dict["graphicalFeatures"])))

        # Template
        graphData.add((m, hasTemplate, t))
        temp = dict["template"]
        if "comparative" in temp.lower():
            graphData.add((t, RDF.type, Comparative))
        elif "macro" in temp.lower():
            graphData.add((t, RDF.type, Macro))
        elif "compass" in temp.lower():
            graphData.add((t, RDF.type, PoliticalCompass))
        elif "mind" in temp.lower():
            graphData.add((t, RDF.type, ChangeMyMind))
    
        # Eventuality 
        graphData.add((e, perspectivisedAs, m))
        temp = dict["eventuality"]["type"]
        if "politician" in temp:
            graphData.add((e, RDF.type, Politician))
        elif "event" in temp:
            graphData.add((e, RDF.type, PoliticalActivity))
        elif "supporter" in temp:
            graphData.add((e, RDF.type, PoliticalSupporter))
        elif "social" in temp:
            graphData.add((e, RDF.type, SocialGroup))
        graphData.add((e, hasValue, Literal(dict["eventuality"]["specific"])))

        # Attitude
        temp = dict["attitude"]
        troll = temp["troll"]
        opinionated = temp["opinionated"]
        graphData.add((a, towards, m))
        if troll and opinionated:
            graphData.add((a, RDF.type, tOpinionated))
        elif not troll and opinionated:
            graphData.add((a, RDF.type, Opinionated))
        elif troll and not opinionated:
            graphData.add((a, RDF.type, tNonOpinionated))
        elif not troll and not opinionated:
            graphData.add((a, RDF.type, NonOpinionated))     
        
        # Cut map
        meme_identifier = {"ControversialOpinion":{"Offensive":"ControversialMeme"},
                           "PersonalOpinion":{"PoliticalCompassTemplate":"NeutralJuxtapositionMeme",
                                              "ComparativeTemplate":"MockingJuxtapositionMeme",
                                              "Connotation":{"Motivational":"SupportiveMeme",
                                                             "Sarcastic":"SatyricalMeme",
                                                             "Ironic":"SatyricalMeme"}}}
        if dict["opinion"].lower() in "personalopinion":
            if dict["template"].lower() in meme_identifier["PersonalOpinion"]:
                if dict["template"].lower() == "politicalcompasstemplate":
                    graphData.add((m, RDF.type, NeutralJuxtapositionMeme))
                else:
                    graphData.add((m, RDF.type, MockingJuxtapositionMeme))
            elif dict["connotation"].lower().capitalize() in meme_identifier["PersonalOpinion"]["Connotation"]:
                if dict["connotation"].lower() == "ironic" or dict["connotation"].lower() == "sarcastic":
                    graphData.add((m, RDF.type, SatyricalMeme))
                else:
                    graphData.add((m, RDF.type, SupportiveMeme))
        elif dict["connotation"].lower() == "offensive":
            graphData.add((m, RDF.type, ControversialMeme))
        
        n += 1

    # Sending the graph to the database
        store = SPARQLUpdateStore()

        store.open((endpoint, endpoint))

        for triple in graphData.triples((None, None, None)):
            store.add(triple)

        store.close()

create_datagraph("http://192.168.1.56:9999/blazegraph/", "cmm.json")