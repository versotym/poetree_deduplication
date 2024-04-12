import json
import os
import networkx as nx
from rich.progress import Progress
from rich.table import Table
import matplotlib.pyplot as plt
from . import rules, adhoc

class Deduplication:
    '''
    Take the similarity measures stored in the JSON files and turn them
    into a networkx graph. Complete components and star components are solved
    according to rules stated in rules.py, other components are treated as specified
    in adhoc.py.
    '''

    def __init__(self, lang, path, threshold, subc_pref):
        '''
        Initialize Deduplication class
        ---
        PARAMS:
            lang      (str)   : Language of the corpus (ISO code)
            path      (str)   : Path to a folder where JSON files stored
            threshold (float) : Threshold above which a pair of poems is considered to be duplicates
            subc_pref (list)  : If there are multiple subcorpora, one may set here preferences in the form of LoL, e.g.:
                                subcorpora_preferences = [ ['subcorp1', 'subcorp2'], ['subcorp3']]
                                would always favour a poem from subcorp1 or supcorp2 over a poem from a subcorp3
        '''
        self.lang       = lang
        self.path       = path
        self.threshold  = threshold
        self.subc_pref  = subc_pref        
        progress        = Progress()
        self.console    = progress.console
        self.metadata   = dict()
        self.nodes      = set()
        self.edges      = list()
        self.duplicates = dict()


    def deduplicate(self):
        '''
        Main method - perform all deduplication steps
        '''
        self._load_metadata()
        self._create_graph()
        self._solve_complete_components()
        self._solve_star_components()
        self._solve_adhoc()
        self._print_survivors()
        return self.duplicates


    def _load_metadata(self):
        '''
        Load metadata and similarity measures from JSON files
        '''
        with Progress() as progress:
            files = os.listdir(self.path)
            task = progress.add_task(f'[red]Fetching metadata on {len(files)} poems...[/]', total=len(files))
            for file in files:
                progress.update(task, advance=1)
                if not file.endswith('.json'):
                    continue
                with open(os.path.join(self.path, file)) as f:
                    poem = json.load(f)
                self.metadata[poem['id']] = {
                    'length':         len(poem['body']),
                    'title' :         poem['title'],
                    'year_published': poem['source']['year_published'],
                    'duplicate':      False,
                    'subcorpus':      poem['source']['corpus']
                }
                if isinstance(poem['author'], list):
                    self.metadata[poem['id']]['author'] = ' + '.join([x['name'] for x in poem['author']])
                else:
                    self.metadata[poem['id']]['author'] = poem['author']['name']
                if isinstance(poem['year_created'], list):
                    self.metadata[poem['id']]['year_created'] = poem['year_created'][0]
                else:
                    self.metadata[poem['id']]['year_created'] = poem['year_created']
                for neighbor in poem['neighbors']:
                    if neighbor[1] >= self.threshold:
                        self.nodes.add(poem['id'])
                        self.nodes.add(neighbor[0])
                        self.edges.append((poem['id'], neighbor[0]))


    def _print_summary(self, label):
        '''
        Prints a summary of the current state of the graph 
        (# of nodes, # of edges, # of connected components)
        ---
        PARAMS:
            label  (str)       Label for current state
        '''
        self.console.print()
        self.console.print('─'*30 + f' {label}\n', style="magenta")
        self.console.print(f'# of nodes:                {self.g.number_of_nodes()}')                
        self.console.print(f'# of edges:                {self.g.number_of_edges()}')                        
        self.console.print(f'# of connected components: {nx.number_connected_components(self.g)}')  


    def _create_graph(self):
        '''
        Turn similarity measures into a networkx graph
        '''
        self.g = nx.Graph()
        self.g.add_nodes_from(self.nodes)
        self.g.add_edges_from(self.edges)
        self._print_summary('INITIAL STATE')


    def _solve_complete_components(self):
        '''
        Find a primary variant in complete components. These are the clusters where each pair 
        of nodes is connected by an edge to each other. Easy to solve by a set of rules stated
        in rules.py
        '''
        nodes_to_remove = []
        for nodelist in nx.connected_components(self.g):
            H = self.g.subgraph(nodelist)
            n = len(nodelist)
            if H.size() == n*(n-1)/2:
                self.duplicates.update(
                    rules.complete_component(nodelist, self.metadata, self.subc_pref)
                )
                nodes_to_remove.extend(nodelist)
        self.g.remove_nodes_from(nodes_to_remove)
        self._print_summary('COMPLETE COMPONENTS REMOVED')


    def _solve_star_components(self):
        '''
        Find a primary variant in star components. These are the clusters where all
        edges stem from a single node and this central node is the longest poem 
        among cluster members. Probably a poem that was published elsewhere 
        splitted into subpoems.
        '''
        nodes_to_remove = []
        for nodelist in nx.connected_components(self.g):
            H = self.g.subgraph(nodelist)
            highest_degree_node = max(H.nodes, key=H.degree)
            component_lengths = sorted([self.metadata[x]['length'] for x in nodelist], reverse=True)
            if (
                self.metadata[highest_degree_node]['length'] == component_lengths[0] and
                component_lengths[0] != component_lengths[1] and
                H.degree(highest_degree_node) == H.number_of_nodes() - 1
            ):
                self.duplicates.update(rules.star_component(nodelist, highest_degree_node))            
                nodes_to_remove.extend(nodelist)
        self.g.remove_nodes_from(nodes_to_remove)
        self._print_summary('STAR COMPONENTS REMOVED')


    def _solve_adhoc(self):
        '''
        Remove manually solved components (these are stored in adhoc.py)
        '''    
        ind = adhoc.adhoc_cases(self.lang)
        self.duplicates.update(ind)
        self.g.remove_nodes_from(ind.keys())    
        self.g, self.duplicates = rules.adhoc_rules(self.g, self.duplicates, self.lang, self.metadata)
        self._print_summary('AD HOC RULES APPLIED')


    def _print_survivors(self):
        '''
        Print the list of remaining unsolved components
        '''    
        self.console.print()
        self.console.print('─'*30 + ' SURVIVORS', style="magenta")
        if nx.number_connected_components(self.g) > 0:
            for i,nodelist in enumerate(nx.connected_components(self.g)):
                self.console.print()
                table = Table(
                    title = f'component # {i+1} :: {self.metadata[list(nodelist)[0]]["author"]}',
                    title_justify = 'left',
                    box = None
                )
                table.add_column("", style="cyan", no_wrap=True)
                table.add_column("poem_id", style="magenta", no_wrap=True)
                table.add_column("title", style="magenta")
                table.add_column("# of lines", style="green", no_wrap=True)
                table.add_column("created", style="green", no_wrap=True)
                table.add_column("published", style="green", no_wrap=True)
                for j, n in enumerate(nodelist):
                    table.add_row(
                        f'P{j+1}',
                        n,
                        self.metadata[n]['title'][:50],
                        str(self.metadata[n]['length']),
                        str(self.metadata[n]['year_created']),
                        str(self.metadata[n]['year_published']),
                    )
                print()
                self.console.print(table)
        else:
            print(None)
