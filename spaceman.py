# Create a dictionary of words to be used in the game, with "Categories" as keys and corresponding words as values
# Limit to single words (not two-word compound entries), and entries 5 letters or more
# N.B. Dictionary derived [in part] from: http://www.enchantedlearning.com/wordlist/

# import python libraries for random selection, time, and terminal control
import random
import time
import os
import sys

# word_dictionary = {
#     "Animals" : ["aardvark", "alligator", "alpaca", "baboon", "badger", "bison", "buffalo", "camel", "caribou", "cheetah", "cougar", "crocodile", "elephant", "flamingo", "hamster", "penguin", "possum", "ocelot", "raccoon", "sheep", "tortoise", "turtle", "weasel", "whelk", "zorilla"],
#     "Art" : ["airbrush", "carving", "ceramics", "collage", "crosshatching", "decoupage", "easel", "engraving", "fresco", "glassblowing", "graffiti", "landscape", "masterpiece", "mosaic", "paintbrush", "palette", "printing", "realism", "relief", "sculpture", "watercolor"],
#     "Astronomy" : ["apogee", "asteroid", "constellation", "corona", "Earth", "heliocentric", "hypernova", "galaxy", "gravitation", "Jupiter", "Mars", "Mercury", "nebula", "Neptune", "parallax", "penumbra", "Pluto", "quasar", "Saturn", "supernova", "Uranus", "Venus", "zodiac"],
#     "Beach" : ["bikini", "boardwalk", "catamaran", "currents", "lifeguard", "longboard", "paddleboat", "popsicle", "sailboat", "sandcastle", "seashell", "seashore", "starfish", "sunbathe", "sunburn", "sunglasses", "sunscreen", "surfboard", "tsunami", "umbrella", "volleyball"],
#     "Biomes" : ["chaparral", "desert", "grassland", "jungle", "plain", "rainforest", "savanna", "swamp", "taiga", "tundra", "woodland"],
#     "Body" : ["abdomen", "ankle", "artery", "bladder", "capillary", "cartilage", "clavicle", "diaphragm", "esophagus", "femur", "intestines", "kidney", "larynx", "pharynx", "sternum", "thorax", "trachea", "urethra", "wrist"],
#     "Carpenter's Tools" : ["anvil", "chisel", "crowbar", "fastener", "hacksaw", "hammer", "screwdriver", "sharpener", "toolbox", "wedge", "workbench", "wrench"],
#     "Christmas" : ["blizzard", "caroling", "chestnuts", "chimney", "cookies", "decorations", "eggnog", "evergreen", "fireplace", "fruitcake", "gingerbread", "Krampus", "mistletoe", "nutcracker", "ornaments", "presents", "Rudolph", "sugarplums", "yuletide"],
#     "Colors" : ["amber", "amethyst", "aquamarine", "beige", "cerulean", "chartreuse", "crimson", "cyan", "ebony", "emerald", "fuchsia", "indigo", "lavendar", "lilac", "magenta", "maroon", "periwinkle", "sienna", "slate", "vermilion", "wisteria"],
#     "Computers" : ["algorithm", "application", "array", "binary", "browser", "captcha", "command", "dashboard", "desktop", "document", "domain", "download", "encryption", "hardware", "hypertext", "kernel", "malware", "phishing", "programmer", "spreadsheet", "typeface"],
#     "Cooking Tools" : ["apron", "carafe", "colander", "cookbook", "cutlery", "infuser", "grater", "juicer", "peeler", "percolater", "ramekin", "skewer", "strainer", "tablespoon", "teaspoon", "zester"],
#     "Country Names" : ["Afghanistan", "Albania", "Algeria", "Argentina", "Australia", "Azerbaijan", "Bahamas", "Bangladesh", "Bahrain", "Belgium", "Bulgaria", "Cambodia", "Canada", "Croatia", "Denmark", "Ecuador", "Finland", "Germany", "Guatemala", "Hungary", "Iceland", "Ireland", "Jamaica", "Kuwait", "Latvia", "Lebanon", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malaysia", "Mexico", "Mongolia", "Morocco", "Netherlands", "Nicaragua", "Pakistan", "Panama", "Paraguay", "Philippines", "Portugal", "Romania", "Rwanda", "Senegal", "Somalia", "Switzerland", "Tanzania", "Thailand", "Tunisia", "Uganda", "Ukraine", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Zambia", "Zimbabwe"],
#     "Desserts" : ["baklava", "biscotti", "brownies", "butterscotch", "cannoli", "cheesecake", "churros", "cobbler", "crepes", "cupcakes", "custard", "doughnut", "eclair", "fudge", "gingersnaps", "jellyroll", "ladyfingers", "macaroon", "meringue", "nougat", "parfait", "shortbread", "snickerdoodles", "souffle", "spumoni", "strudel", "sundae", "torte", "trifle", "turnover", "waffles", "zabaglione"],
#     "Dogs" : ["beagle", "bloodhound", "bulldog", "corgi", "dachshund", "dalmatian", "husky", "maltese", "poodle", "purebred", "retriever", "samoyed", "schnauser", "spaniel", "westie"],
#     "Elements" : ["actinium", "aluminum", "americium", "antimony", "argon", "barium", "beryllium", "bismuth", "bohrium", "boron", "bromine", "cadmium", "calcium", "californium", "carbon", "cerium", "cesium", "chlorine", "chromine", "cobalt", "copper", "curium", "dubnium", "dysprosium", "einsteinium", "europium", "fluorine", "francium", "gallium", "germanium", "hafnium", "helium", "hydrogen", "indium", "iodine", "iridium", "krypton", "lanthanum", "lawrencium", "lithium", "magnesium", "manganese", "mendelevium", "mercury", "molybdenum", "neptunium", "nickel", "niobium", "nitrogen", "osmium", "oxygen", "palladium", "phosphorus", "platinum", "plutonium", "polonium", "potassium", "promethium", "protactinium", "radium", "radon", "rhenium", "rhodium", "rubidium", "ruthenium", "rutherfordium", "scandium", "selenium", "silicon", "sodium", "strontium", "sulfur", "technetium", "thallium", "titanium", "tungsten", "ununtrium", "uranium", "vanadium", "xenon", "yttrium", "zirconium"],
#     "Fields of Science" : ["aerodynamics", "anatomy", "anthropology", "archaeology", "astronomy", "bacteriology", "biochemistry", "biology", "biophysics", "botany", "cartography", "chemistry", "climatology", "cosmology", "criminology", "dermatology", "ecology", "embryology", "entomology", "epidemiology", "exobiology", "genetics", "genomics", "geology", "geophysics", "gerontology", "hematology", "herpetology", "histology", "hydrology", "immunology", "kinesiology", "meteorology", "microbiology", "mineralogy", "morphology", "neurology", "neuroscience", "nutrition", "oceanography", "oncology", "ornithology", "paleontology", "pathology", "petrology", "physics", "physiology", "psychology", "radiology", "sociology", "taxonomy", "thermodynamics", "toxicology", "urology", "zoology"],
#     "Fish" : ["angelfish", "angelshark", "barracuda", "blowfish", "bonito", "catfish", "clownfish", "dogfish", "dragonfish", "flounder", "glassfish", "goldfish", "guppy", "haddock", "hagfish", "halibut", "hatchetfish", "herring", "icefish", "jackfish", "lamprey", "lanternfish", "lungfish", "mackerel", "Megalodon", "minnow", "monkfish", "mullet", "needlefish", "oarfish", "paddlefish", "parrotfish", "perch", "piranha", "pollock", "pufferfish", "quillfish", "remora", "rockfish", "salmon", "sardine", "sawfish", "sculpin", "seabass", "seadragon", "seahorse", "smelt", "snapper", "stingray", "sturgeon", "sunfish", "swordfish", "whiting", "yellowtail", "zebrafish"],
#     "Flowers" : ["azalea", "begonia", "bellflower", "bluebell", "buttercup", "calendula", "camellia", "carnation", "chrysanthemum", "cornflower", "cosmo", "daffodil", "daisies", "dandelion", "freesia", "gardenia", "hibiscus", "honeysuckle", "hydrangea", "jasmine", "laurel", "lavendar", "lilac", "lilies", "magnolia", "marigold", "mayflower", "orchids", "passionflower", "peonies", "plumeria", "poppy", "primrose", "safflower", "snapdragon", "sunflower", "tulips", "violets", "wallflower", "wildflower", "wisteria", "wolfsbane", "zinnias"],
#     "Food & Drink" : ["almonds", "anchovies", "appetizer", "appetite", "bacon", "bagel", "barbecue", "barley", "beancurd", "biscuits", "bland", "bread", "breakfast", "brisket", "broil", "brunch", "buckwheat", "burrito", "butter", "calorie", "candy", "caramel", "carbohydrate", "cashews", "cassava", "casserole", "caviar", "cereal", "cheddar", "cheese", "chicken", "chili", "chips", "chocolate", "chopsticks", "chutney", "coffee", "coleslaw", "cornflakes", "cornmeal", "crackers", "cuisine", "dessert", "digest", "dinner", "dressing", "feast", "guacamole", "hamburger", "hummus", "jellybeans", "lasagna", "lemonade", "lentils", "licorice", "lobster", "lunchmeat", "macaroni", "meatballs", "meatloaf", "milkshake", "mincemeat", "mozzarella", "mutton", "napkins", "noodles", "omelette", "omurice", "pancakes", "pepperoni", "pickles", "picnic", "pilaf", "pizza", "popcorn", "popovers", "pretzel", "quiche", "quinoa", "ravioli", "recipes", "refreshments", "refrigerator", "relish", "restaurant", "salty", "sandwich", "sauerkraut", "sausage", "savory", "scallops", "spaghetti", "spareribs", "spoon", "spork", "steak", "stirfry", "sustenance", "sweet", "tacos", "tamales", "tapioca", "teriyaki", "umami", "utensils", "vegetables", "vitamins", "water"],
#     "Fruit" : ["apple", "apricot", "avocado", "banana", "berries", "blackberry", "blueberry", "boysenberry", "breadfruit", "cantaloupe", "cherries", "citron", "citrus", "coconut", "crabapple", "cranberry", "dates", "dragonfruit", "durian", "elderberry", "grapes", "grapefruit", "guava", "honeydew", "jackfruit", "kumquat", "lemons", "limes", "lingonberry", "loquat", "lychee", "mangoes", "marionberry", "melons", "mulberry", "nectarine", "oranges", "papaya", "peaches", "pears", "persimmon", "pineapples", "plantain", "plums", "pomegranate", "pomelo", "prunes", "quince", "raspberry", "strawberry", "tangelo", "tangerine", "watermelon"],
#     "Herbs and Spices" : ["allspice", "angelica", "anise", "annato", "basil", "capers", "cardamom", "cayenne", "chervil", "chicory", "chives", "cilantro", "cinnamon", "coriander", "fennel", "garlic", "ginger", "horseradish", "nutmeg", "oregano", "paprika", "parsley", "pepper", "peppermint", "rosemary", "saffron", "spearmint", "tarragon", "thyme", "turmeric", "vanilla", "wasabi", "watercress", "wintergreen"],
#     "Holidays" : ["Christmas", "Diwali", "Easter", "Eid", "Halloween", "Hanukkah", "Juneteenth", "Kwanzaa", "Passover", "Purim", "Ramadan", "Thanksgiving"],
#     "Insects" : ["aphid", "armyworm", "bedbug", "beetle", "bumblebee", "butterfly", "caterpillar", "cicada", "cockroach", "cricket", "damselfly", "dragonfly", "earwig", "gnats", "grasshopper", "honeybee", "hornet", "junebug", "katydid", "ladybug", "lacewing", "leafhopper", "maggot", "mantid", "mantis", "mayfly", "mealworm", "monarch", "mosquito", "planthopper", "scarab", "silkworm", "termite", "waterbug", "weevil", "yellowjacket"],
#     "Languages" : ["Afrikaans", "Albanian", "Arabic", "Armenian", "Belarusan", "Bengali", "Bulgarian", "Burmese", "Cantonese", "Chinese", "Croatian", "Danish", "Dutch", "English", "Estonian", "Filipino", "Finnish", "French", "Gaelic", "German", "Greek", "Hebrew", "Hindi", "Hungarian", "Italian", "Japanese", "Korean", "Malay", "Persian", "Portuguese", "Punjabi", "Russian", "Sanskrit", "Somali", "Swedish", "Tagalog", "Tamil", "Turkish", "Ukrainian", "Urdu", "Vietnamese", "Welsh", "Yiddish"],
#     "Measurement" : ["acres", "angstrom", "bales", "bytes", "carats", "centimeter", "decigram", "deciliter", "decimal", "decimeter", "degree", "depth", "digit", "dozen", "dram", "fathom", "gallon", "grain", "gross", "gutenberg", "height", "inches", "karat", "kilogram", "kilometer", "knots", "league", "length", "lightyear", "liters", "megameter", "megapixel", "megaton", "microgram", "microliter", "micron", "milliliter", "millimeter", "minute", "nanometer", "octave", "ounces", "pennyweight", "percent", "percentile", "picogram", "picoliter", "picometer", "pints", "pixels", "pound", "quart", "radian", "ruler", "scale", "score", "smidgen", "spoonful", "standard", "thermometer", "units", "volume", "weight", "width", "yards", "zolls"],
#     "Metals" : ["alloy", "aluminum", "antimony", "brass", "bronze", "chrome", "chromium", "copper", "gold", "gunmetal", "iron", "iridium", "lead", "magnesium", "mercury", "pewter", "platinum", "silver", "steel", "titanium", "tungsten", "uranium", "zinc"],
#     "Musical Instruments" : ["accordion", "bagpipe", "banjo", "bassoon", "bugle", "castanets", "cello", "cimbalom", "clarinet", "cornet", "cowbell", "cymbals", "drums", "drumsticks", "dulcimer", "fiddle", "flute", "glockenspiel", "guitar", "harmonica", "harmonium", "harpsichord", "kazoo", "kettledrum", "keyboard", "mandolin", "maracas", "marimba", "ocarina", "organ", "piano", "piccolo", "recorder", "saxophone", "sitar", "strings", "tabla", "tambourine", "timpani", "triangle", "trombone", "trumpet", "ukelele", "vibraphone", "viola", "violin", "whistle", "woodwinds", "xylophone", "zither"],
#     "Plants" : ["agriculture", "alfalfa", "angiosperm", "autotroph", "bamboo", "berries", "biennial", "blossoms", "botany", "branches", "bulbs", "bushes", "cactus", "clover", "corolla", "dicot", "endosperm", "evergreen", "ferns", "fertilizer", "flora", "flower", "foliage", "fruits", "germinate", "ginkgo", "grains", "grass", "horticulture", "hybrids", "juniper", "leaves", "legume", "monocot", "nectar", "needle", "perennial", "petiole", "phloem", "photosynthesis", "pollen", "resin", "roots", "sapling", "seedling", "sepal", "shamrock", "stamen", "stoma", "succulents", "thorns", "tumbleweed", "vegetation", "veins", "vines", "woody", "xylem", "yucca"],
#     "Rocks and Minerals" : ["agate", "alexandrite", "amber", "amethyst", "azurite", "basalt", "calcite", "coral", "crystal", "diamond", "emerald", "fluorite", "fossil", "garnet", "gemstone", "geode", "granite", "gravel", "limestone", "magma", "magnetite", "mica", "moonstone", "nephrite", "obsidian", "pebble", "peridot", "pumice", "pyrite", "quartz", "sandstone", "sapphire", "silica", "soapstone", "stalactite", "stalagmite", "topaz", "vulcanite"],
#     "Science and Lab" : ["atoms", "beaker", "burette", "cells", "chemicals", "climate", "electrochemistry", "element", "energy", "entomology", "experiment", "flask", "funnel", "glassware", "magnetism", "molecule", "motion", "observe", "particle", "pipette", "research", "thermometer", "variable"],
#     "Shapes" : ["angle", "circle", "concave", "convex", "cuboid", "curve", "cylinder", "decagon", "dodecahedron", "ellipse", "ellipsoid", "helix", "heptagon", "hexaflexagon", "hexagon", "hexahedron", "hyperboloid", "icosahedron", "nonagon", "octagon", "octahedron", "paraboloid", "parallelogram", "pentagon", "plane", "point", "polygon", "polyhedra", "prism", "pyramid", "quadrilateral", "rectangle", "rhombus", "semicircle", "sphere", "square", "tetrahedron", "tesseract", "trapezoid", "triangle", "wedge"],
#     "Sports" : ["aerobics", "archery", "athletics", "badminton", "baseball", "basketball", "baton", "biathlon", "bicycling", "biking", "bowling", "boxing", "canoeing", "championship", "competition", "cricket", "croquet", "curling", "cycling", "deadlifting", "decathlon", "discus", "diving", "dodgeball", "fencing", "fielding", "football", "frisbee", "golfing", "gymnastics", "handball", "heptathlon", "hockey", "infielder", "javelin", "jumping", "karate", "kayaking", "lacrosse", "Olympics", "outfielder", "paddleball", "paintball", "pickleball", "pitcher", "quarterback", "racing", "racquetball", "referee", "riding", "rowing", "running", "sailing", "scoreboard", "shortstop", "skating", "skiing", "slalom", "sledding", "snorkling", "snowboarding", "softball", "squash", "swimming", "taekwondo", "teammate", "tetherball", "triathlon", "ultramarathon", "unicycling", "vaulting", "walking", "waterskiing", "weightlifting", "windsurfing", "wrestling"],
#     "Vegetables" : ["alfalfa", "artichoke", "arugula", "asparagus", "avocado", "broccoli", "carrot", "cauliflower", "celery", "chard", "cabbage", "cucumber", "daikon", "eggplant", "endive", "gourd", "greenbeans", "greens", "jicama", "kohlrabi", "lentils", "lettuce", "maize", "mushroom", "olives", "onions", "parsnip", "peapod", "peppers", "pickle", "potato", "pumpkin", "radicchio", "radish", "rhubarb", "romaine", "rutabaga", "salad", "scallion", "seaweed", "shallot", "soybean", "spinach", "sprouts", "squash", "succotash", "tomatillo", "tomato", "tuber", "turnip", "wasabi", "watercress", "yams", "zucchini"],
#     "Weather" : ["accumulation", "atmosphere", "aurora", "balmy", "barometer", "biosphere", "blizzard", "blustery", "breeze", "cirrus", "climate", "cloud", "condensation", "cumulonimbus", "cumulus", "current", "cyclone", "degree", "depression", "downdraft", "downpour", "downwind", "drizzle", "drought", "duststorm", "evaporation", "forecast", "humidity", "hurricane", "hydrosphere", "isotherm", "lightning", "meteorology", "moisture", "monsoon", "nimbus", "nimbostratus", "noreaster", "overcast", "permafrost", "precipitation", "pressure", "radar", "rainbow", "sandstorm", "snowfall", "snowstorm", "stratosphere", "stratus", "temperate", "temperature", "thermometer", "thunderstorm", "troposphere", "typhoon", "upwind", "visibility", "vortex", "weathervane", "whiteout", "zones"],
# }

# Word lists!!! <-- Dictionary didn't work ;-;
Animals = ["aardvark", "alligator", "alpaca", "baboon", "badger", "bison", "buffalo", "camel", "caribou", "cheetah", "cougar", "crocodile", "elephant", "flamingo", "hamster", "penguin", "possum", "ocelot", "raccoon", "sheep", "tortoise", "turtle", "weasel", "whelk", "zorilla"],
Art = ["airbrush", "carving", "ceramics", "collage", "crosshatching", "decoupage", "easel", "engraving", "fresco", "glassblowing", "graffiti", "landscape", "masterpiece", "mosaic", "paintbrush", "palette", "printing", "realism", "relief", "sculpture", "watercolor"],
Astronomy = ["apogee", "asteroid", "constellation", "corona", "earth", "heliocentric", "hypernova", "galaxy", "gravitation", "jupiter", "mars", "mercury", "nebula", "neptune", "parallax", "penumbra", "pluto", "quasar", "saturn", "supernova", "uranus", "venus", "zodiac"],
Beach = ["bikini", "boardwalk", "catamaran", "currents", "lifeguard", "longboard", "paddleboat", "popsicle", "sailboat", "sandcastle", "seashell", "seashore", "starfish", "sunbathe", "sunburn", "sunglasses", "sunscreen", "surfboard", "tsunami", "umbrella", "volleyball"],
Biomes = ["chaparral", "desert", "grassland", "jungle", "plain", "rainforest", "savanna", "swamp", "taiga", "tundra", "woodland"],
Body = ["abdomen", "ankle", "artery", "bladder", "capillary", "cartilage", "clavicle", "diaphragm", "esophagus", "femur", "intestines", "kidney", "larynx", "pharynx", "sternum", "thorax", "trachea", "urethra", "wrist"],
Carpenters_Tools = ["anvil", "chisel", "crowbar", "fastener", "hacksaw", "hammer", "screwdriver", "sharpener", "toolbox", "wedge", "workbench", "wrench"],
Christmas = ["blizzard", "caroling", "chestnuts", "chimney", "cookies", "decorations", "eggnog", "evergreen", "fireplace", "fruitcake", "gingerbread", "krampus", "mistletoe", "nutcracker", "ornaments", "presents", "Rudolph", "sugarplums", "yuletide"],
Colors = ["amber", "amethyst", "aquamarine", "beige", "cerulean", "chartreuse", "crimson", "cyan", "ebony", "emerald", "fuchsia", "indigo", "lavendar", "lilac", "magenta", "maroon", "periwinkle", "sienna", "slate", "vermilion", "wisteria"],
Computers = ["algorithm", "application", "array", "binary", "browser", "captcha", "command", "dashboard", "desktop", "document", "domain", "download", "encryption", "hardware", "hypertext", "kernel", "malware", "phishing", "programmer", "spreadsheet", "typeface"],
Cooking_Tools = ["apron", "carafe", "colander", "cookbook", "cutlery", "infuser", "grater", "juicer", "peeler", "percolater", "ramekin", "skewer", "strainer", "tablespoon", "teaspoon", "zester"],
Country_Names = ["afghanistan", "albania", "algeria", "argentina", "australia", "azerbaijan", "bahamas", "bangladesh", "bahrain", "belgium", "bulgaria", "cambodia", "canada", "croatia", "denmark", "ecuador", "finland", "germany", "guatemala", "hungary", "iceland", "ireland", "jamaica", "kuwait", "latvia", "lebanon", "lithuania", "luxembourg", "macedonia", "madagascar", "malaysia", "mexico", "mongolia", "morocco", "netherlands", "nicaragua", "pakistan", "panama", "paraguay", "philippines", "portugal", "romania", "rwanda", "senegal", "somalia", "switzerland", "tanzania", "thailand", "tunisia", "uganda", "ukraine", "uruguay", "uzbekistan", "venezuela", "vietnam", "zambia", "zimbabwe"],
Desserts = ["baklava", "biscotti", "brownies", "butterscotch", "cannoli", "cheesecake", "churros", "cobbler", "crepes", "cupcakes", "custard", "doughnut", "eclair", "fudge", "gingersnaps", "jellyroll", "ladyfingers", "macaroon", "meringue", "nougat", "parfait", "shortbread", "snickerdoodles", "souffle", "spumoni", "strudel", "sundae", "torte", "trifle", "turnover", "waffles", "zabaglione"],
Dogs = ["beagle", "bloodhound", "bulldog", "corgi", "dachshund", "dalmatian", "husky", "maltese", "poodle", "purebred", "retriever", "samoyed", "schnauser", "spaniel", "westie"],
Elements = ["actinium", "aluminum", "americium", "antimony", "argon", "barium", "beryllium", "bismuth", "bohrium", "boron", "bromine", "cadmium", "calcium", "californium", "carbon", "cerium", "cesium", "chlorine", "chromine", "cobalt", "copper", "curium", "dubnium", "dysprosium", "einsteinium", "europium", "fluorine", "francium", "gallium", "germanium", "hafnium", "helium", "hydrogen", "indium", "iodine", "iridium", "krypton", "lanthanum", "lawrencium", "lithium", "magnesium", "manganese", "mendelevium", "mercury", "molybdenum", "neptunium", "nickel", "niobium", "nitrogen", "osmium", "oxygen", "palladium", "phosphorus", "platinum", "plutonium", "polonium", "potassium", "promethium", "protactinium", "radium", "radon", "rhenium", "rhodium", "rubidium", "ruthenium", "rutherfordium", "scandium", "selenium", "silicon", "sodium", "strontium", "sulfur", "technetium", "thallium", "titanium", "tungsten", "ununtrium", "uranium", "vanadium", "xenon", "yttrium", "zirconium"],
Fields_of_Science = ["aerodynamics", "anatomy", "anthropology", "archaeology", "astronomy", "bacteriology", "biochemistry", "biology", "biophysics", "botany", "cartography", "chemistry", "climatology", "cosmology", "criminology", "dermatology", "ecology", "embryology", "entomology", "epidemiology", "exobiology", "genetics", "genomics", "geology", "geophysics", "gerontology", "hematology", "herpetology", "histology", "hydrology", "immunology", "kinesiology", "meteorology", "microbiology", "mineralogy", "morphology", "neurology", "neuroscience", "nutrition", "oceanography", "oncology", "ornithology", "paleontology", "pathology", "petrology", "physics", "physiology", "psychology", "radiology", "sociology", "taxonomy", "thermodynamics", "toxicology", "urology", "zoology"],
Fish = ["angelfish", "angelshark", "barracuda", "blowfish", "bonito", "catfish", "clownfish", "dogfish", "dragonfish", "flounder", "glassfish", "goldfish", "guppy", "haddock", "hagfish", "halibut", "hatchetfish", "herring", "icefish", "jackfish", "lamprey", "lanternfish", "lungfish", "mackerel", "Megalodon", "minnow", "monkfish", "mullet", "needlefish", "oarfish", "paddlefish", "parrotfish", "perch", "piranha", "pollock", "pufferfish", "quillfish", "remora", "rockfish", "salmon", "sardine", "sawfish", "sculpin", "seabass", "seadragon", "seahorse", "smelt", "snapper", "stingray", "sturgeon", "sunfish", "swordfish", "whiting", "yellowtail", "zebrafish"],
Flowers = ["azalea", "begonia", "bellflower", "bluebell", "buttercup", "calendula", "camellia", "carnation", "chrysanthemum", "cornflower", "cosmo", "daffodil", "daisies", "dandelion", "freesia", "gardenia", "hibiscus", "honeysuckle", "hydrangea", "jasmine", "laurel", "lavendar", "lilac", "lilies", "magnolia", "marigold", "mayflower", "orchids", "passionflower", "peonies", "plumeria", "poppy", "primrose", "safflower", "snapdragon", "sunflower", "tulips", "violets", "wallflower", "wildflower", "wisteria", "wolfsbane", "zinnias"],
Food_and_Drink = ["almonds", "anchovies", "appetizer", "appetite", "bacon", "bagel", "barbecue", "barley", "beancurd", "biscuits", "bland", "bread", "breakfast", "brisket", "broil", "brunch", "buckwheat", "burrito", "butter", "calorie", "candy", "caramel", "carbohydrate", "cashews", "cassava", "casserole", "caviar", "cereal", "cheddar", "cheese", "chicken", "chili", "chips", "chocolate", "chopsticks", "chutney", "coffee", "coleslaw", "cornflakes", "cornmeal", "crackers", "cuisine", "dessert", "digest", "dinner", "dressing", "feast", "guacamole", "hamburger", "hummus", "jellybeans", "lasagna", "lemonade", "lentils", "licorice", "lobster", "lunchmeat", "macaroni", "meatballs", "meatloaf", "milkshake", "mincemeat", "mozzarella", "mutton", "napkins", "noodles", "omelette", "omurice", "pancakes", "pepperoni", "pickles", "picnic", "pilaf", "pizza", "popcorn", "popovers", "pretzel", "quiche", "quinoa", "ravioli", "recipes", "refreshments", "refrigerator", "relish", "restaurant", "salty", "sandwich", "sauerkraut", "sausage", "savory", "scallops", "spaghetti", "spareribs", "spoon", "spork", "steak", "stirfry", "sustenance", "sweet", "tacos", "tamales", "tapioca", "teriyaki", "umami", "utensils", "vegetables", "vitamins", "water"],
Fruit = ["apple", "apricot", "avocado", "banana", "berries", "blackberry", "blueberry", "boysenberry", "breadfruit", "cantaloupe", "cherries", "citron", "citrus", "coconut", "crabapple", "cranberry", "dates", "dragonfruit", "durian", "elderberry", "grapes", "grapefruit", "guava", "honeydew", "jackfruit", "kumquat", "lemons", "limes", "lingonberry", "loquat", "lychee", "mangoes", "marionberry", "melons", "mulberry", "nectarine", "oranges", "papaya", "peaches", "pears", "persimmon", "pineapples", "plantain", "plums", "pomegranate", "pomelo", "prunes", "quince", "raspberry", "strawberry", "tangelo", "tangerine", "watermelon"],
Herbs_and_Spices = ["allspice", "angelica", "anise", "annato", "basil", "capers", "cardamom", "cayenne", "chervil", "chicory", "chives", "cilantro", "cinnamon", "coriander", "fennel", "garlic", "ginger", "horseradish", "nutmeg", "oregano", "paprika", "parsley", "pepper", "peppermint", "rosemary", "saffron", "spearmint", "tarragon", "thyme", "turmeric", "vanilla", "wasabi", "watercress", "wintergreen"],
Holidays = ["christmas", "diwali", "easter", "eid", "halloween", "hanukkah", "juneteenth", "kwanzaa", "passover", "purim", "ramadan", "thanksgiving"],
Insects = ["aphid", "armyworm", "bedbug", "beetle", "bumblebee", "butterfly", "caterpillar", "cicada", "cockroach", "cricket", "damselfly", "dragonfly", "earwig", "gnats", "grasshopper", "honeybee", "hornet", "junebug", "katydid", "ladybug", "lacewing", "leafhopper", "maggot", "mantid", "mantis", "mayfly", "mealworm", "monarch", "mosquito", "planthopper", "scarab", "silkworm", "termite", "waterbug", "weevil", "yellowjacket"],
Languages = ["afrikaans", "albanian", "arabic", "armenian", "belarusan", "bengali", "bulgarian", "burmese", "cantonese", "chinese", "croatian", "danish", "dutch", "english", "estonian", "filipino", "finnish", "french", "gaelic", "german", "greek", "hebrew", "hindi", "hungarian", "italian", "japanese", "korean", "malay", "persian", "portuguese", "punjabi", "russian", "sanskrit", "somali", "swedish", "tagalog", "tamil", "turkish", "ukrainian", "urdu", "vietnamese", "welsh", "yiddish"],
Measurement = ["acres", "angstrom", "bales", "bytes", "carats", "centimeter", "decigram", "deciliter", "decimal", "decimeter", "degree", "depth", "digit", "dozen", "dram", "fathom", "gallon", "grain", "gross", "gutenberg", "height", "inches", "karat", "kilogram", "kilometer", "knots", "league", "length", "lightyear", "liters", "megameter", "megapixel", "megaton", "microgram", "microliter", "micron", "milliliter", "millimeter", "minute", "nanometer", "octave", "ounces", "pennyweight", "percent", "percentile", "picogram", "picoliter", "picometer", "pints", "pixels", "pound", "quart", "radian", "ruler", "scale", "score", "smidgen", "spoonful", "standard", "thermometer", "units", "volume", "weight", "width", "yards", "zolls"],
Metals = ["alloy", "aluminum", "antimony", "brass", "bronze", "chrome", "chromium", "copper", "gold", "gunmetal", "iron", "iridium", "lead", "magnesium", "mercury", "pewter", "platinum", "silver", "steel", "titanium", "tungsten", "uranium", "zinc"],
Musical_Instruments = ["accordion", "bagpipe", "banjo", "bassoon", "bugle", "castanets", "cello", "cimbalom", "clarinet", "cornet", "cowbell", "cymbals", "drums", "drumsticks", "dulcimer", "fiddle", "flute", "glockenspiel", "guitar", "harmonica", "harmonium", "harpsichord", "kazoo", "kettledrum", "keyboard", "mandolin", "maracas", "marimba", "ocarina", "organ", "piano", "piccolo", "recorder", "saxophone", "sitar", "strings", "tabla", "tambourine", "timpani", "triangle", "trombone", "trumpet", "ukelele", "vibraphone", "viola", "violin", "whistle", "woodwinds", "xylophone", "zither"],
Plants = ["agriculture", "alfalfa", "angiosperm", "autotroph", "bamboo", "berries", "biennial", "blossoms", "botany", "branches", "bulbs", "bushes", "cactus", "clover", "corolla", "dicot", "endosperm", "evergreen", "ferns", "fertilizer", "flora", "flower", "foliage", "fruits", "germinate", "ginkgo", "grains", "grass", "horticulture", "hybrids", "juniper", "leaves", "legume", "monocot", "nectar", "needle", "perennial", "petiole", "phloem", "photosynthesis", "pollen", "resin", "roots", "sapling", "seedling", "sepal", "shamrock", "stamen", "stoma", "succulents", "thorns", "tumbleweed", "vegetation", "veins", "vines", "woody", "xylem", "yucca"],
Rocks_and_Minerals = ["agate", "alexandrite", "amber", "amethyst", "azurite", "basalt", "calcite", "coral", "crystal", "diamond", "emerald", "fluorite", "fossil", "garnet", "gemstone", "geode", "granite", "gravel", "limestone", "magma", "magnetite", "mica", "moonstone", "nephrite", "obsidian", "pebble", "peridot", "pumice", "pyrite", "quartz", "sandstone", "sapphire", "silica", "soapstone", "stalactite", "stalagmite", "topaz", "vulcanite"],
Science_and_Lab = ["atoms", "beaker", "burette", "cells", "chemicals", "climate", "electrochemistry", "element", "energy", "entomology", "experiment", "flask", "funnel", "glassware", "magnetism", "molecule", "motion", "observe", "particle", "pipette", "research", "thermometer", "variable"],
Shapes = ["angle", "circle", "concave", "convex", "cuboid", "curve", "cylinder", "decagon", "dodecahedron", "ellipse", "ellipsoid", "helix", "heptagon", "hexaflexagon", "hexagon", "hexahedron", "hyperboloid", "icosahedron", "nonagon", "octagon", "octahedron", "paraboloid", "parallelogram", "pentagon", "plane", "point", "polygon", "polyhedra", "prism", "pyramid", "quadrilateral", "rectangle", "rhombus", "semicircle", "sphere", "square", "tetrahedron", "tesseract", "trapezoid", "triangle", "wedge"],
Sports = ["aerobics", "archery", "athletics", "badminton", "baseball", "basketball", "baton", "biathlon", "bicycling", "biking", "bowling", "boxing", "canoeing", "championship", "competition", "cricket", "croquet", "curling", "cycling", "deadlifting", "decathlon", "discus", "diving", "dodgeball", "fencing", "fielding", "football", "frisbee", "golfing", "gymnastics", "handball", "heptathlon", "hockey", "infielder", "javelin", "jumping", "karate", "kayaking", "lacrosse", "Olympics", "outfielder", "paddleball", "paintball", "pickleball", "pitcher", "quarterback", "racing", "racquetball", "referee", "riding", "rowing", "running", "sailing", "scoreboard", "shortstop", "skating", "skiing", "slalom", "sledding", "snorkling", "snowboarding", "softball", "squash", "swimming", "taekwondo", "teammate", "tetherball", "triathlon", "ultramarathon", "unicycling", "vaulting", "walking", "waterskiing", "weightlifting", "windsurfing", "wrestling"],
Vegetables = ["alfalfa", "artichoke", "arugula", "asparagus", "avocado", "broccoli", "carrot", "cauliflower", "celery", "chard", "cabbage", "cucumber", "daikon", "eggplant", "endive", "gourd", "greenbeans", "greens", "jicama", "kohlrabi", "lentils", "lettuce", "maize", "mushroom", "olives", "onions", "parsnip", "peapod", "peppers", "pickle", "potato", "pumpkin", "radicchio", "radish", "rhubarb", "romaine", "rutabaga", "salad", "scallion", "seaweed", "shallot", "soybean", "spinach", "sprouts", "squash", "succotash", "tomatillo", "tomato", "tuber", "turnip", "wasabi", "watercress", "yams", "zucchini"],
Weather = ["accumulation", "atmosphere", "aurora", "balmy", "barometer", "biosphere", "blizzard", "blustery", "breeze", "cirrus", "climate", "cloud", "condensation", "cumulonimbus", "cumulus", "current", "cyclone", "degree", "depression", "downdraft", "downpour", "downwind", "drizzle", "drought", "duststorm", "evaporation", "forecast", "humidity", "hurricane", "hydrosphere", "isotherm", "lightning", "meteorology", "moisture", "monsoon", "nimbus", "nimbostratus", "noreaster", "overcast", "permafrost", "precipitation", "pressure", "radar", "rainbow", "sandstorm", "snowfall", "snowstorm", "stratosphere", "stratus", "temperate", "temperature", "thermometer", "thunderstorm", "troposphere", "typhoon", "upwind", "visibility", "vortex", "weathervane", "whiteout", "zones"],

category_list = ["Animals", "Art", "Astronomy", "Beach", "Biomes", "Body", "Carpenters_Tools", "Christmas", "Colors", "Computers", "Cooking_Tools", "Country_Names", "Desserts", "Dogs", "Elements", "Fields_of_Science", "Fish", "Flowers", "Food_and_Drink", "Fruit", "Herbs_and_Spices", "Holidays", "Insects", "Languages", "Measurement", "Metals", "Musical_Instruments", "Plants", "Rocks_and_Minerals", "Science_and_Lab", "Shapes", "Sports", "Vegetables", "Weather"]
var_list = [Animals, Art, Astronomy, Beach, Biomes, Body, Carpenters_Tools, Christmas, Colors, Computers, Cooking_Tools, Country_Names, Desserts, Dogs, Elements, Fields_of_Science, Fish, Flowers, Food_and_Drink, Fruit, Herbs_and_Spices, Holidays, Insects, Languages, Measurement, Metals, Musical_Instruments, Plants, Rocks_and_Minerals, Science_and_Lab, Shapes, Sports, Vegetables, Weather]

incorrect_guesses = []
user_progress = []
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# welcome function
def hello_user():
    print("Hello there! Welcome to spaceman, a less gruesome version of the favorite wordgame, hangman!")
    print("You will have a total of 7 guesses to guess a randomly selected word.")
    print("And should you fail, our beloved spaceman will be shot into space with no hope of return!!! (O_O)")

# ready to play function -- drawn from my madlibs app
def ready_to_play():
    print("")
    ready = str(input("Are you ready to play? (y/n): "))
    if ready == 'y' or ready == 'Y':
        print("Alright, time to put on your best thinking-cap!!!")
        time.sleep(3)
        os.system('clear')
    elif ready == 'n' or ready == 'N':
        print("Okay, goodbye.")
        time.sleep(1)
        sys.exit()
    else:
        print("Invalid input! Please try again.")
        ready_to_play()

# function for retrieving a random category
def random_category_selection():
    category = random.choice(category_list)
    cat_index = category_list.index(category)
    word_list = var_list[cat_index]

    print("Your category is " + str(category_list[cat_index]).upper())

    return word_list

# function for retrieving a word from selected category
def random_word_selection():
    for word_list in random_category_selection():
        global selected_word
        selected_word = random.choice(word_list)

    # print(selected_word)
    global num_chars
    num_chars = len(selected_word)
    print("")
    print("Can you guess the word?:")

    global blanks
    blanks = str(num_chars * "_ ")
    print(blanks)
    print("")
    return selected_word

def check_user_guess(string, sub_string):
    string = selected_word
    sub_string = input("Enter a letter you think is in this word. Please enter only lowercase letters!!!: ")
    total_user_guesses = 1

    update_user_view(selected_word, sub_string)

    while total_user_guesses < 7:
        if sub_string.isalpha() == False or sub_string.islower() == False or (len(sub_string) > 1 and len(sub_string) < len(selected_word)):
            print("Invalid input! Please try again.")
            print("")
            sub_string = input("Enter another guess or enter the word if you think you know it; lowercase letters only!: ")
            update_user_view(selected_word, sub_string)

        elif sub_string in user_progress or sub_string in incorrect_guesses:
            print("You already guessed that!")
            print("")
            sub_string = input("Enter another guess or enter the word if you think you know it; lowercase letters only!: ")
            update_user_view(selected_word, sub_string)

        elif (string.find(sub_string) == -1):
            incorrect_guesses.append(sub_string)

            print("No, sorry. Please try again.")
            print("")
            print(new_blanks)
            print("")
            print("Incorrect guesses: " + str(incorrect_guesses))
            print("Correct guesses: " + str(user_progress))
            print("")

            sub_string = input("Enter another guess or enter the word if you think you know it; lowercase letters only!: ")
            update_user_view(selected_word, sub_string)
            total_user_guesses += 1

        elif (sub_string == selected_word):
            print("")
            print("You did it!!! Spaceman gets to stay with us on planet Earth!!!")
            break

        else:
            user_progress.append(sub_string)
            print("Yes, excellent guess!")
            print("")
            # insert statement here which returns corresponding blanks filled in with correct letter
            print(new_blanks)
            print("Incorrect guesses: " + str(incorrect_guesses))
            print("Correct guesses: " + str(user_progress))
            print("")

            sub_string = input("Enter another guess or enter the full word if you think you know it; lowercase letters only!: ")
            update_user_view(selected_word, sub_string)
            total_user_guesses += 1

    else:
        print("")
        print(new_blanks)
        print("")
        print("Sorry, gameover. Your word was " + selected_word + ". Alas, spaceman must now be shot into space! ;-;")

    # print(total_user_guesses)

def update_user_view(selected_word, input):
    global new_blanks
    new_blanks = ""

    for i in range(len(selected_word)):
        if selected_word[i] == input:
            new_blanks = new_blanks + input + " " # Adds user guess to string if guess is correct
        else:
            # Add a blank at index i to the user_view if it doesn't match the guess
            new_blanks = new_blanks + "_ "

    return new_blanks

# fix this function for consistently updated blanks-- it is currently broken ;-;
def update_new_blanks(selected_word, input, new_blanks):
    for i in range(len(new_blanks)):
        if selected_word[int(i/2)] == input:
            new_blanks.replace(new_blanks[i], input)
        else:
            new_blanks.replace(new_blanks[i], "_")

    return new_blanks

# test function!!!
def test():
    # # return random key from dict
    # print(random.choice(word_dictionary.keys()))
    # # return random value from dictionary
    # print(random.choice(word_dictionary.values()))
    # # return random key AND value from dictionary
    # print(random.choice(word_dictionary.items()))

    # random_category_selection() <--DOES NOT NEED TO BE CALLED-->
    random_word_selection()
    check_user_guess(selected_word, input)

    # # test update_user_view function
    # update_user_view("chicken", "i")
    # print(new_blanks)
    # update_user_view("chicken", "m")
    # print(new_blanks)

# required function calls
# test()
hello_user()
ready_to_play()
random_word_selection()
check_user_guess(selected_word, input)
