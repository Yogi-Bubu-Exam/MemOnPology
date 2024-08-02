from json import load
from rdflib import Graph, URIRef, Namespace, Literal, RDF, OWL, RDFS
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
    cons = Namespace("http://www.ontologydesignpatterns.org/cp/owl/constituency.owl#")
    persp = Namespace("ontologydesignpatterns.org/ont/persp/perspectivisation.owl#")
    project_url = "https://github.com/Yogi-Bubu-Exam/MemOnPology/"

    # Creating graph, binding namespaces
    graphData = Graph()
    graphData.bind("spomepo", spomepo)
    graphData.bind("spomo", spomo)
    graphData.bind("cons", cons)
    graphData.bind("persp", persp)
    graphData.bind("project", project_url)

    # Creating classes
    # Background Knowledge
    BackgroundKnowledge = URIRef(persp.BackgroundKnowledge)
    graphData.add((BackgroundKnowledge, RDF.type, OWL.Class))
    SocioPoliticalPhenomena = URIRef(spomepo.SocioPoliticalPhenomena)
    graphData.add((SocioPoliticalPhenomena, RDF.type, OWL.Class))
    graphData.add((SocioPoliticalPhenomena, RDFS.subClassOf, BackgroundKnowledge))


    # Eventuality
    Eventuality = URIRef(persp.Eventuality)
    graphData.add((Eventuality, RDF.type, OWL.Class))
    PoliticalAgent = URIRef(spomo.PoliticalAgent)
    graphData.add((PoliticalAgent, RDF.type, OWL.Class))
    graphData.add((PoliticalAgent, RDFS.subClassOf, Eventuality))
    SocialGroup = URIRef(spomo.SocialGroup)
    graphData.add((SocialGroup, RDF.type, OWL.Class))
    graphData.add((SocialGroup, RDFS.subClassOf, Eventuality))
    Politician = URIRef(spomo.Politician)
    graphData.add((Politician, RDF.type, OWL.Class))
    graphData.add((Politician, RDFS.subClassOf, PoliticalAgent))
    PoliticalSupporter = URIRef(spomo.PoliticalSupporter)
    graphData.add((PoliticalSupporter, RDF.type, OWL.Class))
    graphData.add((PoliticalSupporter, RDFS.subClassOf, PoliticalAgent))   
    PoliticalActivity = URIRef(spomo.PoliticalActivity)
    graphData.add((PoliticalActivity, RDF.type, OWL.Class))
    graphData.add((PoliticalActivity, RDFS.subClassOf, Eventuality))


    # Lens
    Lens = URIRef(persp.Lens)
    graphData.add((Lens, RDF.type, OWL.Class))
    
    MemeticLens = URIRef(spomepo.MemeticLens)
    graphData.add((MemeticLens, RDF.type, OWL.Class))
    graphData.add((MemeticLens, RDFS.subClassOf, Lens))
    # Template
    Template = URIRef(spomo.Template)
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
    MediaFrame = URIRef(spomo.MediaFrame)
    graphData.add((MediaFrame, RDF.type, OWL.Class))
    Caption = URIRef(spomo.Caption)
    graphData.add((Caption, RDF.type, OWL.Class))
    graphData.add((Caption, RDFS.subClassOf, MediaFrame))
    GraphicContent = URIRef(spomo.GraphicContent)
    graphData.add((GraphicContent, RDF.type, OWL.Class))
    graphData.add((GraphicContent, RDFS.subClassOf, MediaFrame))
    
    #Connotation
    Connotation = URIRef(spomo.Connotation)
    graphData.add((Connotation, RDF.type, OWL.Class))

    # Cut
    Cut = URIRef(persp.Cut)
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
    Attitude = URIRef(persp.Attitude)
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
    hasValue = URIRef(spomo.hasValue)
    graphData.add((hasValue, RDF.type, OWL.DatatypeProperty))
    hasCaption = URIRef(spomo.hasCaption)
    graphData.add((hasCaption, RDF.type, OWL.ObjectProperty))
    hasConnotation = URIRef(spomo.hasConnotation)
    graphData.add((hasConnotation, RDF.type, OWL.ObjectProperty))   
    hasGraphicContent = URIRef(spomo.hasGraphicContent)
    graphData.add((hasGraphicContent, RDF.type, OWL.ObjectProperty))
    hasTemplate = URIRef(spomo.hasTemplate)
    graphData.add((hasTemplate, RDF.type, OWL.ObjectProperty))
    graphData.add((SocioPoliticalMeme, hasTemplate, Template))
    expresses = URIRef(spomepo.expresses)
    graphData.add((expresses, RDF.type, OWL.ObjectProperty))
    perspectivisedAs = URIRef(persp.perspectivisedAs)
    graphData.add((perspectivisedAs, RDF.type, OWL.ObjectProperty))
    graphData.add((Eventuality, perspectivisedAs, Cut))
    perspectivisedThrough = URIRef(persp.perspectivisedThrough)
    graphData.add((perspectivisedThrough, RDF.type, OWL.ObjectProperty))
    graphData.add((Eventuality, perspectivisedThrough, Lens))
    towards = URIRef(persp.towards)
    graphData.add((towards, RDF.type, OWL.ObjectProperty))
    graphData.add((Attitude, towards, Cut))
    extractedFrom = URIRef(persp.extractedFrom)
    graphData.add((extractedFrom, RDF.type, OWL.ObjectProperty))
    graphData.add((Eventuality, extractedFrom, SocioPoliticalPhenomena))
    isConstituentOf = URIRef(cons.isConstituentOf)
    graphData.add((isConstituentOf, RDF.type, OWL.ObjectProperty))
    graphData.add((MediaFrame, isConstituentOf, MemeticLens))
    graphData.add((Template, isConstituentOf, MemeticLens))
    refersTo = URIRef(spomo.refersTo)
    graphData.add((refersTo, RDF.type, OWL.ObjectProperty))
    graphData.add((MediaFrame, refersTo, Eventuality))
    shotThrough = URIRef(persp.shotThrough)
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
        if dict["opinion"] == "controversial" or meme_conn == "offensive":
            if "Comparative" in meme_frame:
                graphData.add((m, RDF.type, MockingJuxtapositionMeme))
            else:
                graphData.add((m, RDF.type, ControversialMeme))
        elif meme_conn == "motivational":
            graphData.add((m, RDF.type, SupportiveMeme))

        elif "Comparative" in meme_frame and meme_conn == "sarcastic":
            graphData.add((m, RDF.type, MockingJuxtapositionMeme))
            
        elif meme_frame != "Political Compass" or ("Comparative" in meme_frame and meme_conn == "ironic"):
            graphData.add((m, RDF.type, HumorousMeme))
        else:
            graphData.add((m, RDF.type, NeutralJuxtapositionMeme))
        
        
        n += 1

    # Sending the graph to the database
    store = SPARQLUpdateStore()
    store.open((endpoint, endpoint))

    for triple in graphData.triples((None, None, None)):
        store.add(triple)

    store.close()

create_datagraph("http://192.168.1.54:9999/blazegraph/", "data.json")