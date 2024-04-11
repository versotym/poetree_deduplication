from lib import deduplication

# Perform deduplication of the PoeTree corpus
dd = deduplication.Deduplication(
    lang      = 'en',                  # Language of the corpus
    path      = '[path_to_dir]',       # Path to a folder where JSON files stored
    threshold = 0.75,                  # Threshold above which a pair of poems is considered to be duplicates    
    subc_pref = None                   # If there are multiple subcorpora, one may set preferences here in the form of LoL, e.g.:
                                       # subcorpora_preferences = [ ['subcorp1', 'subcorp2'], ['subcorp3']]
                                       # would always favour a poem from subcorp1 or supcorp2 over a poem from a subcorp3 in
                                       # complete components
)

# Returns the duplicates (structure: duplicates[poem_id] = id of the primary variant)
duplicates = dd.deduplicate()