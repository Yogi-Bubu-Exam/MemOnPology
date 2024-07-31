from json import load
from rdflib import Graph, URIRef, Namespace, Literal, RDF, OWL, RDFS
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
    spomo = Namespace("https://github.com/Yogi-Bubu-Exam/MemOnPology/raw/main/SPoMO.owl#")
    project_url = "https://github.com/Yogi-Bubu-Exam/MemOnPology/"

    # Creating graph, binding namespaces
    graphData = Graph()
    graphData.bind("spomepo", spomepo)
    graphData.bind("project", project_url)

    # Creating classes
    # Background Knowledge
    BackgroundKnowledge = URIRef(spomepo.BackgroundKnowledge)
    graphData.add((BackgroundKnowledge, RDF.type, OWL.Class))
    SocioPoliticalPhenomena = URIRef(spomepo.SocioPoliticalPhenomena)
    graphData.add((SocioPoliticalPhenomena, RDF.type, OWL.Class))
    graphData.add((SocioPoliticalPhenomena, RDFS.subClassOf, BackgroundKnowledge))


    # Eventuality
    Eventuality = URIRef(spomepo.Eventuality)
    graphData.add((Eventuality, RDF.type, OWL.Class))
    PoliticalAgent = URIRef(spomepo.PoliticalAgent)
    graphData.add((PoliticalAgent, RDF.type, OWL.Class))
    graphData.add((PoliticalAgent, RDFS.subClassOf, Eventuality))
    SocialGroup = URIRef(spomepo.SocialGroup)
    graphData.add((SocialGroup, RDF.type, OWL.Class))
    graphData.add((SocialGroup, RDFS.subClassOf, Eventuality))
    Politician = URIRef(spomepo.Politician)
    graphData.add((Politician, RDF.type, OWL.Class))
    graphData.add((Politician, RDFS.subClassOf, PoliticalAgent))
    PoliticalSupporter = URIRef(spomepo.PoliticalSupporter)
    graphData.add((PoliticalSupporter, RDF.type, OWL.Class))
    graphData.add((PoliticalSupporter, RDFS.subClassOf, PoliticalAgent))   
    PoliticalActivity = URIRef(spomepo.PoliticalActivity)
    graphData.add((PoliticalActivity, RDF.type, OWL.Class))
    graphData.add((PoliticalActivity, RDFS.subClassOf, Eventuality))


    # Lens
    Lens = URIRef(spomepo.Lens)
    graphData.add((Lens, RDF.type, OWL.Class))
    
    MemeticLens = URIRef(spomepo.MemeticLens)
    graphData.add((MemeticLens, RDF.type, OWL.Class))
    graphData.add((MemeticLens, RDFS.subClassOf, Lens))
    # Template
    Template = URIRef(spomepo.Template)
    graphData.add((Template, RDF.type, OWL.Class))
    graphData.add((Template, RDFS.subClassOf, Template))
    Comparative = URIRef(spomepo.ComparativeTemplate)
    graphData.add((Comparative, RDF.type, OWL.Class))
    graphData.add((Comparative, RDFS.subClassOf, Template))
    ChangeMyMind = URIRef(spomepo.ChangeMyMindTemplate)
    graphData.add((ChangeMyMind, RDF.type, OWL.Class))
    graphData.add((ChangeMyMind, RDFS.subClassOf, Template))
    PoliticalCompass = URIRef(spomepo.PoliticalCompassTemplate)
    graphData.add((PoliticalCompass, RDF.type, OWL.Class))
    graphData.add((PoliticalCompass, RDFS.subClassOf, Template))
    Macro = URIRef(spomepo.PoliticalImageMacro)
    graphData.add((Macro, RDF.type, OWL.Class))
    graphData.add((Macro, RDFS.subClassOf, Template))

    # Mediaframe
    MediaFrame = URIRef(spomepo.MediaFrame)
    graphData.add((MediaFrame, RDF.type, OWL.Class))
    Caption = URIRef(spomepo.Caption)
    graphData.add((Caption, RDF.type, OWL.Class))
    graphData.add((Caption, RDFS.subClassOf, MediaFrame))
    GraphicContent = URIRef(spomepo.GraphicContent)
    graphData.add((GraphicContent, RDF.type, OWL.Class))
    graphData.add((GraphicContent, RDFS.subClassOf, MediaFrame))
    
    #Connotation
    Connotation = URIRef(spomepo.Connotation)
    graphData.add((Connotation, RDF.type, OWL.Class))

    # Cut
    Cut = URIRef(spomepo.Cut)
    graphData.add((Cut, RDF.type, OWL.Class))
    SocioPoliticalMeme = URIRef(spomo.SocioPoliticalMeme)
    graphData.add((SocioPoliticalMeme, RDF.type, OWL.Class))
    graphData.add((SocioPoliticalMeme, RDFS.subClassOf, Cut))
    ControversialMeme = URIRef(spomepo.ControversialMeme)
    graphData.add((ControversialMeme, RDF.type, OWL.Class))
    graphData.add((ControversialMeme, RDFS.subClassOf, SocioPoliticalMeme))
    MockingJuxtapositionMeme = URIRef(spomepo.MockingJuxtapositionMeme)
    graphData.add((MockingJuxtapositionMeme, RDF.type, OWL.Class))
    graphData.add((MockingJuxtapositionMeme, RDFS.subClassOf, SocioPoliticalMeme))
    NeutralJuxtapositionMeme = URIRef(spomepo.NeutralJuxtapositionMeme)
    graphData.add((NeutralJuxtapositionMeme, RDF.type, OWL.Class))
    graphData.add((NeutralJuxtapositionMeme, RDFS.subClassOf, SocioPoliticalMeme))
    HumorousMeme = URIRef(spomepo.HumorousMeme)
    graphData.add((HumorousMeme, RDF.type, OWL.Class))
    graphData.add((HumorousMeme, RDFS.subClassOf, SocioPoliticalMeme))
    SupportiveMeme = URIRef(spomepo.SupportiveMeme)
    graphData.add((SupportiveMeme, RDF.type, OWL.Class))
    graphData.add((SupportiveMeme, RDFS.subClassOf, SocioPoliticalMeme))
    
    # Opinion
    Opinion = URIRef(spomepo.Opinion)
    graphData.add((Opinion, RDF.type, OWL.Class))
    UncontroversialOpinion = URIRef(spomepo.UncontroversialOpinion)
    graphData.add((UncontroversialOpinion, RDF.type, OWL.Class))
    graphData.add((UncontroversialOpinion, RDFS.subClassOf, Opinion))
    ControversialOpinion = URIRef(spomepo.ControversialOpinion)
    graphData.add((ControversialOpinion, RDF.type, OWL.Class))
    graphData.add((ControversialOpinion, RDFS.subClassOf, Opinion))
    
    # Attitude
    Attitude = URIRef(spomepo.Attitude)
    graphData.add((Attitude, RDF.type, OWL.Class))

    NonTroll = URIRef(spomepo.NonTroll)
    graphData.add((NonTroll, RDF.type, OWL.Class))
    graphData.add((NonTroll, RDFS.subClassOf, Attitude))

    NonOpinionated = URIRef(spomepo.NonOpinionated)
    graphData.add((NonOpinionated, RDF.type, OWL.Class))
    graphData.add((NonOpinionated, RDFS.subClassOf, NonTroll))

    Opinionated = URIRef(spomepo.Opinionated)
    graphData.add((Opinionated, RDFS.subClassOf, NonTroll))
    graphData.add((Opinionated, RDF.type, OWL.Class))

    Troll = URIRef(spomepo.Troll)
    graphData.add((Troll, RDF.type, OWL.Class))
    graphData.add((Troll, RDFS.subClassOf, Attitude))

    tNonOpinionated = URIRef(spomepo.tNonOpinionated)
    graphData.add((tNonOpinionated, RDF.type, OWL.Class))
    graphData.add((tNonOpinionated, RDFS.subClassOf, Troll))

    tOpinionated = URIRef(spomepo.tOpinionated)
    graphData.add((tOpinionated, RDFS.subClassOf, Troll))
    graphData.add((tOpinionated, RDF.type, OWL.Class))
        

    # Creating relations
    hasValue = URIRef(spomepo.hasValue)
    graphData.add((hasValue, RDF.type, OWL.DatatypeProperty))
    hasCaption = URIRef(spomepo.hasCaption)
    graphData.add((hasCaption, RDF.type, OWL.ObjectProperty))
    hasConnotation = URIRef(spomepo.hasConnotation)
    graphData.add((hasConnotation, RDF.type, OWL.ObjectProperty))   
    hasGraphicContent = URIRef(spomepo.hasGraphicContent)
    graphData.add((hasGraphicContent, RDF.type, OWL.ObjectProperty))
    hasTemplate = URIRef(spomepo.hasTemplate)
    graphData.add((hasTemplate, RDF.type, OWL.ObjectProperty))
    graphData.add((SocioPoliticalMeme, hasTemplate, Template))
    expresses = URIRef(spomepo.expresses)
    graphData.add((expresses, RDF.type, OWL.ObjectProperty))
    perspectivisedAs = URIRef(spomepo.perspectivisedAs)
    graphData.add((perspectivisedAs, RDF.type, OWL.ObjectProperty))
    graphData.add((Eventuality, perspectivisedAs, Cut))
    perspectivisedThrough = URIRef(spomepo.perspectivisedThrough)
    graphData.add((perspectivisedThrough, RDF.type, OWL.ObjectProperty))
    graphData.add((Eventuality, perspectivisedThrough, Lens))
    towards = URIRef(spomepo.towards)
    graphData.add((towards, RDF.type, OWL.ObjectProperty))
    graphData.add((Attitude, towards, Cut))
    extractedFrom = URIRef(spomepo.extractedFrom)
    graphData.add((extractedFrom, RDF.type, OWL.ObjectProperty))
    graphData.add((Eventuality, extractedFrom, SocioPoliticalPhenomena))
    isConstituentOf = URIRef(spomepo.isConstituentOf)
    graphData.add((isConstituentOf, RDF.type, OWL.ObjectProperty))
    graphData.add((MediaFrame, isConstituentOf, MemeticLens))
    graphData.add((Template, isConstituentOf, MemeticLens))
    refersTo = URIRef(spomepo.refersTo)
    graphData.add((refersTo, RDF.type, OWL.ObjectProperty))
    graphData.add((MediaFrame, refersTo, Eventuality))
    shotThrough = URIRef(spomepo.shotThrough)
    graphData.add((shotThrough, RDF.type, OWL.ObjectProperty))
    graphData.add((Cut, shotThrough, Lens))


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