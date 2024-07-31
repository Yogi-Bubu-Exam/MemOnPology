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
    Comparative = URIRef(spomepo.ComparativeTemplate)
    ChangeMyMind = URIRef(spomepo.ChangeMyMindTemplate)
    PoliticalCompass = URIRef(spomepo.PoliticalCompassTemplate)
    Macro = URIRef(spomepo.PoliticalImageMacro)
    SocialGroup = URIRef(spomepo.SocialGroup)
    Politician = URIRef(spomepo.Politician)
    PoliticalSupporter = URIRef(spomepo.PoliticalSupporter)
    PoliticalActivity = URIRef(spomepo.PoliticalActivity)
    UncontroversialOpinion = URIRef(spomepo.UncontroversialOpinion)
    ControversialOpinion = URIRef(spomepo.ControversialOpinion)
    NonOpinionated = URIRef(spomepo.NonOpinionated)
    Opinionated = URIRef(spomepo.Opinionated)
    tNonOpinionated = URIRef(spomepo.tNonOpinionated)
    tOpinionated = URIRef(spomepo.tOpinionated)
    ControversialMeme = URIRef(spomepo.ControversialMeme)
    MockingJuxtapositionMeme = URIRef(spomepo.MockinJuxtapositionMeme)
    NeutralJuxtapositionMeme = URIRef(spomepo.NeutralJuxtapositionMeme)
    HumorousMeme = URIRef(spomepo.HumorousMeme)
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
        if "uncontroversial" in dict["opinion"]:
            graphData.add((ca, expresses, UncontroversialOpinion))
        else:
            graphData.add((ca, expresses, ControversialOpinion))
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
        
        # Cut map: if controversial and not comparative, then controversial meme; 
        #          if personal and sarcastic/ironic and not comparativeTemp or PolComp, then Humorous
        #                   {"ControversialOpinion":{"ComparativeTemplate":"MockingJuxtapositionMeme"},
        #                    "UncontroversialOpinion":{"Motivational":"SupportiveMeme",
        #                                       "Sarcastic, Ironic":{"Comparative":"NeutralJuxtapositionMeme",
        #                                                            "Political Compass":"NeutralJuxtapositionMeme"}}
        #                                        "Offensive": "MockingJuxtapositionMeme"}
                          
        meme_frame = dict["template"]
        meme_conn = dict["connotation"]
        if dict["opinion"] == "controversial":
            if "Comparative" in meme_frame:
                graphData.add((m, RDF.type, MockingJuxtapositionMeme))
            else:
                graphData.add((m, RDF.type, ControversialMeme))
        elif meme_conn == "motivational" and meme_frame != "Political Compass":
            graphData.add((m, RDF.type, SupportiveMeme))
        elif "Comparative" not in meme_frame and meme_frame != "Political Compass":
            graphData.add((m, RDF.type, HumorousMeme))
        elif meme_conn == "offensive":
            graphData.add((m, RDF.type, MockingJuxtapositionMeme))
        else:
            graphData.add((m, RDF.type, NeutralJuxtapositionMeme))
        
        
        n += 1

    # Sending the graph to the database
    store = SPARQLUpdateStore()
    store.open((endpoint, endpoint))

    for triple in graphData.triples((None, None, None)):
        store.add(triple)

    store.close()

create_datagraph("http://192.168.1.3:9999/blazegraph/", "data.json")