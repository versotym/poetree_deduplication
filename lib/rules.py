import random
import networkx as nx

def complete_component(nodelist, corpus_metadata, subcorpora_preferences=None, length_matters=True):
    '''
    Find primary node in component based on following criteria:
    (1) Limit to nodes according to subcorpora hierarchy
    (2) Primary is the longest poem
    (3) Primary is the poem that was written the earliest (if this is known)
    (4) Primary is the poem that was published the earliest (if this is known)
    (5) If multiple poems remain, pick primary by random
    ---
    PARAMS:
        nodelist               (list)     List of nodes (poem ids)
        corpus_metadata        (dict)     Metadata on poems
        subcorpora_preferences (LoL)      Preferenc hierarchy for particular subcopora   
        length_matters         (bool)     Whether to pick the longest one (default to True,
                                          False applies only in special cases set in special_rules.py) 
    RETURNS
        duplicates             (dict)     Keys are poem_ids, values are either False
                                          (for the primary variant) or poem_id of the
                                          primary variant (for duplicities)   
    '''

    # Limit candidates according to subcorpora preferences: proceed from the subcorpora
    # that have the lowest preference and if some candidates from higher ranked subcopora
    # remain, delete the lower one
    if subcorpora_preferences is not None:
        subcorpora = {x: corpus_metadata[x]['subcorpus'] for x in nodelist}       
        for subcorpus_level in reversed(subcorpora_preferences):
            if len(set(subcorpora.values()) - set(subcorpus_level)) > 0:
                subcorpora = {x: subcorpora[x] for x in subcorpora if subcorpora[x] not in subcorpus_level}                
        candidates = [x for x in subcorpora]
    else:
        candidates = nodelist

    # Limit candidates to the longest ones (in terms of number of lines)
    if length_matters:
        lengths = {x: corpus_metadata[x]['length'] for x in candidates}                
        candidates = [x for x in lengths if lengths[x] == max(lengths.values())]
    
    # Further limit candidates to the oldest ones according to year of creation
    y_created = {x: corpus_metadata[x]['year_created'] for x in candidates if corpus_metadata[x]['year_created']}                
    if len(y_created) > 0 and len(candidates) > 1:
        candidates = [x for x in y_created if y_created[x] == min(y_created.values())]

    # Further limit candidates to the oldest ones according to year of publication
    y_published = {x: corpus_metadata[x]['year_published'] for x in candidates if corpus_metadata[x]['year_published']}
    if len(y_published) > 0 and len(candidates) > 1:
        candidates = [x for x in y_published if y_published[x] == min(y_published.values())]
        
    # If multiple candidates remain, pick the primary one by random (shuffle the list)
    if len(candidates) > 0:
        random.shuffle(candidates)
            
    return _annotate_duplicates(nodelist, candidates[0])


def star_component(nodelist, highest_degree_node):
    '''
    Solve sun-like components - the ones where all edges stem from a single node and
    this central node is the longest poem among cluster members.
    Probably a poem that was published elsewhere splitted into subpoems.
    ---
    PARAMS:
        nodelist               (list)     List of nodes (poem ids)
        highest_degree_node    (str)      Central node id
    RETURNS
        duplicates             (dict)     Keys are poem_ids, values are either False
                                          (for the primary variant) or poem_id of the
                                          primary variant (for duplicities)   
    '''

    return _annotate_duplicates(nodelist, highest_degree_node)


def _annotate_duplicates(nodelist, primary):
    '''
    This function accepts the list of poem ids and the id from this group
    which is considered to be primary. It returns the dict which is then
    attached to the main list of duplicates.

    Params:
        nodelist     (set)  Nodes/poem_ids forming the component    
        primary      (str)  Id from nodelist which is the primary variant
        
    Returns:
        duplicates   (dict) Keys are poem_ids, values are either False
                            (for the primary variant) or poem_id of the
                            primary variant (for duplicities)        
    '''
    
    duplicates = dict()
    for poem_id in nodelist:
        if poem_id == primary:
            duplicates[poem_id] = False
        else:
            duplicates[poem_id] = primary       
    return duplicates


def adhoc_rules(G, duplicates, lang, corpus_metadata):
    '''
    Apply special deduplication rules to individual cases
    ---
    PARAMS:
        G               (networkx) Graph instance
        duplicates      (dict)     Duplicates found so far
        lang            (str)      Language ISO code
        corpus_metadata (dict)     Metadata on poems        
    RETURNS
        G               (networkx) Graph instance reduced
        duplicates      (dict)     Duplicates updated
    '''

    # MacDonnald: The shortest and sweetest of all songs
    # This one is just 2 lines: "come/home". It attracts completely different poems as it is easy
    # to find a way from this to a completely different text.
    # => Remove the poem and remove all nodes that were originally connected to it and now have no edge
    if lang == 'en':
        G.remove_nodes_from(('macdonald-poeticalWorks---297',))   
        G.remove_nodes_from(list(nx.isolates(G)))
                
    # Lešehrad, Emanuel: Plenty of chains of reworking
    # Special rule: As they are all of the same length (one case differ in one line only)
    # Simply keep the oldest one
    if lang == 'cs':    
        nodes_to_remove = list()
        for nodelist in nx.connected_components(G):
            H = G.subgraph(nodelist)
            if corpus_metadata[list(nodelist)[0]]['author'] != 'Lešehrad, Emanuel':
                continue
            nodes_to_remove.extend(nodelist)
            duplicates.update(complete_component(nodelist, corpus_metadata, subcorpora_preferences=None, length_matters=False)) 
        # Remove Lešehrad's components from network graph
        G.remove_nodes_from(nodes_to_remove)

    return G, duplicates