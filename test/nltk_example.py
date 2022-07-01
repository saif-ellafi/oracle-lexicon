from nltk_oracle import *
from model.pos import NLTKPosTagger

example = """
The sun hadn't quite risen, but now that the five men were out from
under the trees it already felt hot. Far ahead, off to the left of
the road, the spires of New Angeles gleamed dusky blue against the
departing night. The two unarmed men gazed back wistfully at the little
town, dark and asleep under its moist leafy umbrellas. The one who was
thin and had hair flecked with gray looked all intellect; the other,
young and with a curly mop, looked all feeling.

The fat man barring their way back to town mopped his head. The two
young men flanking him with shotgun and squirtgun hadn't started to
sweat yet.

The fat man stuffed the big handkerchief back in his pocket, wiped his
hands on his shirt, rested his wrists lightly on the pistols holstered
either side his stomach, looked at the two unarmed men, indicated the
hot road with a nod, and said, "There's your way, professors. Get
going."
"""

print("=================")
print("Testing NLTK Oracle")
print("=================")

tagger = parse(example)
gen(tagger, 'example', False)

print('')
print("=================")
print("Testing saving and loading")
print("=================")

tagger.save('../tagger.pickle')
loaded_tagger = NLTKPosTagger.load('../tagger.pickle')
gen(loaded_tagger, 'example', False)

print('')
print("=================")
print("Finished!")
print("=================")
