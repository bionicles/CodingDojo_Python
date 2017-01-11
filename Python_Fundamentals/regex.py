list = [r"v", r"ss", r"e\b", r"b.b", r"b.+b", r"b.*b", r"aeiou", r"\b[regularexpression]+\b", r"(.)\1"]

import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 return [word for word in words if re.search(regex, word)]

for regex in list:
	print get_matching_words(regex)