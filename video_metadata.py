'''
This file contains video metadata and the ImageNet class list.
'''
from collections import OrderedDict

'''
Ozan's dataset of videos basically contains the first 100 videos
for each of the YouTube searches below.

How to +
Hard Boil an Egg (6,785,176 views)
Make Jello Shots (6,440,352 views)
Make French Toast (4,362,799 views)
Bake a Potato in the Microwave (3,486,832 views)
Open a Wine Bottle Without a Corkscrew (3,096,476 views)
Make Pancakes (2,604,187 views)
*Make Scrambled Eggs (2,354,174 views)
*Poach an Egg (2,039,776 views)
Make Chocolate Chip Cookies (1,970,043 views)
Cook an Omelette (1,943,422 views)
Jump Start a Car (1,904,088 views)
Make Yogurt (1,882,532 views)
Remove a Stripped Screw (1,879,962 views)
Drive a Car (1,646,260 views)
Clean Suede Shoes (1,644,476 views)
Make a Grilled Cheese Sandwich (1,644,436 views)
Unclog a Bathtub Drain (1,581,142 views)
Tie a Tie (1,522,161 views)
'''

NOUNS_AND_VIDEO_IDS = OrderedDict([
  ('banana',
    # how to make banana icecream
    ['9uddKYGPEkg', # the classifier has a recall of 50% and precision of 100%
    ],
  ),
  ('wine',
    ['n63SWcNNWvg',
    ],
  ),
  ('egg', # This noun is not in the ImageNet set and won't be detected
          # until we use a different detector
    # how to hard boil an egg
    ['1QK-DGlRcTo',
     '7-9OEohpivA',
     'lbzhyvH74w8',
     'qX7A0LPIuKs',
     's1oUDsonIzg',
     'sSni2HTfvM',
     'wdasrVE5NOc',
     'zuMslqJKQo',
     # how to poach an egg
     'jk36el4_Rbc',
     'JrRqG9Apt6g',
     'KtZ14xEbgzg',
     'pAWduxoCgVk',
     'UMiCy8EH1go',
     'xpN1dlH3tWo',
     'yppgDL0Mn3g',
     # how to scramble an egg
     '65ifzkFi614',
     'FbLU87PYsZE',
     'Nbh64ntT3EM',
     'R4vDqlKMbrk',
     's9r-CxnCXkg',
     'TGyb7uBXe9E',
     'Be0koDmxrtQ',
     'M8SHMUBnm4A',
     'PUP7U5vTMM0',
     's9r-CxnCXkg',
     # how to make an omelet
     '1dGBRGtyzX0',
     '57afEWn-QDg',
     'AgHgbn_sVUw',
     'AJ2uBYCVHik',
     'OQyRuOEKfVk',
     'PLDUqyS2AGA',
     'PzWsyPHoSyQ',
     'r09Hgeb9-6s',
     'zglsDdaBf4g',
    ],
  ),
])

'''
Here is the list of all nouns ImageNet classifies, copied below.
  http://www.image-net.org/challenges/LSVRC/2013/browse-synsets

1000 synsets for Task 2 (same as in ILSVRC2012)

kit fox, Vulpes macrotis
English setter
Australian terrier
grey whale, gray whale, devilfish, Eschrichtius gibbosus, Eschrichtius robustus
lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens
Egyptian cat
ibex, Capra ibex
Persian cat
cougar, puma, catamount, mountain lion, painter, panther, Felis concolor
gazelle
porcupine, hedgehog
sea lion
badger
Great Dane
Scottish deerhound, deerhound
killer whale, killer, orca, grampus, sea wolf, Orcinus orca
mink
African elephant, Loxodonta africana
red wolf, maned wolf, Canis rufus, Canis niger
jaguar, panther, Panthera onca, Felis onca
hyena, hyaena
titi, titi monkey
three-toed sloth, ai, Bradypus tridactylus
sorrel
black-footed ferret, ferret, Mustela nigripes
dalmatian, coach dog, carriage dog
Staffordshire bullterrier, Staffordshire bull terrier
Bouvier des Flandres, Bouviers des Flandres
weasel
miniature poodle
bighorn, bighorn sheep, cimarron, Rocky Mountain bighorn, Rocky Mountain sheep, Ovis canadensis
fox squirrel, eastern fox squirrel, Sciurus niger
colobus, colobus monkey
tiger cat
impala, Aepyceros melampus
coyote, prairie wolf, brush wolf, Canis latrans
Yorkshire terrier
Newfoundland, Newfoundland dog
red fox, Vulpes vulpes
hartebeest
grey fox, gray fox, Urocyon cinereoargenteus
Pekinese, Pekingese, Peke
guenon, guenon monkey
mongoose
indri, indris, Indri indri, Indri brevicaudatus
tiger, Panthera tigris
wild boar, boar, Sus scrofa
zebra
ram, tup
orangutan, orang, orangutang, Pongo pygmaeus
basenji
leopard, Panthera pardus
vizsla, Hungarian pointer
squirrel monkey, Saimiri sciureus
Siamese cat, Siamese
chimpanzee, chimp, Pan troglodytes
komondor
proboscis monkey, Nasalis larvatus
guinea pig, Cavia cobaya
white wolf, Arctic wolf, Canis lupus tundrarum
ice bear, polar bear, Ursus Maritimus, Thalarctos maritimus
gorilla, Gorilla gorilla
ox
Tibetan mastiff
spider monkey, Ateles geoffroyi
Doberman, Doberman pinscher
warthog
Arabian camel, dromedary, Camelus dromedarius
siamang, Hylobates syndactylus, Symphalangus syndactylus
golden retriever
Border collie
hare
boxer
patas, hussar monkey, Erythrocebus patas
baboon
macaque
capuchin, ringtail, Cebus capucinus
flat-coated retriever
hog, pig, grunter, squealer, Sus scrofa
Eskimo dog, husky
Brittany spaniel
dial telephone, dial phone
maze, labyrinth
Gordon setter
dingo, warrigal, warragal, Canis dingo
hamster
Arctic fox, white fox, Alopex lagopus
water buffalo, water ox, Asiatic buffalo, Bubalus bubalis
American black bear, black bear, Ursus americanus, Euarctos americanus
Angora, Angora rabbit
bison
howler monkey, howler
hippopotamus, hippo, river horse, Hippopotamus amphibius
giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca
tabby, tabby cat
marmoset
Saint Bernard, St Bernard
armadillo
redbone
polecat, fitch, foulmart, foumart, Mustela putorius
marmot
gibbon, Hylobates lar
llama
wood rabbit, cottontail, cottontail rabbit
lion, king of beasts, Panthera leo
Irish setter, red setter
dugong, Dugong dugon
Indian elephant, Elephas maximus
beaver
Madagascar cat, ring-tailed lemur, Lemur catta
Rhodesian ridgeback
lynx, catamount
African hunting dog, hyena dog, Cape hunting dog, Lycaon pictus
langur
timber wolf, grey wolf, gray wolf, Canis lupus
cheetah, chetah, Acinonyx jubatus
sloth bear, Melursus ursinus, Ursus ursinus
German shepherd, German shepherd dog, German police dog, alsatian
otter
koala, koala bear, kangaroo bear, native bear, Phascolarctos cinereus
tusker
echidna, spiny anteater, anteater
wallaby, brush kangaroo
platypus, duckbill, duckbilled platypus, duck-billed platypus, Ornithorhynchus anatinus
wombat
revolver, six-gun, six-shooter
umbrella
schooner
soccer ball
accordion, piano accordion, squeeze box
ant, emmet, pismire
starfish, sea star
chambered nautilus, pearly nautilus, nautilus
grand piano, grand
laptop, laptop computer
strawberry
airliner
warplane, military plane
airship, dirigible
balloon
space shuttle
fireboat
gondola
speedboat
lifeboat
canoe
yawl
catamaran
trimaran
container ship, containership, container vessel
liner, ocean liner
pirate, pirate ship
aircraft carrier, carrier, flattop, attack aircraft carrier
submarine, pigboat, sub, U-boat
wreck
half track
tank, army tank, armored combat vehicle, armoured combat vehicle
missile
bobsled, bobsleigh, bob
dogsled, dog sled, dog sleigh
bicycle-built-for-two, tandem bicycle, tandem
mountain bike, all-terrain bike, off-roader
freight car
passenger car, coach, carriage
barrow, garden cart, lawn cart, wheelbarrow
shopping cart
motor scooter, scooter
forklift
electric locomotive
steam locomotive
amphibian, amphibious vehicle
ambulance
beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon
cab, hack, taxi, taxicab
convertible
jeep, landrover
limousine, limo
minivan
Model T
racer, race car, racing car
sports car, sport car
go-kart
golfcart, golf cart
moped
snowplow, snowplough
fire engine, fire truck
garbage truck, dustcart
pickup, pickup truck
tow truck, tow car, wrecker
trailer truck, tractor trailer, trucking rig, rig, articulated lorry, semi
moving van
police van, police wagon, paddy wagon, patrol wagon, wagon, black Maria
recreational vehicle, RV, R.V.
streetcar, tram, tramcar, trolley, trolley car
snowmobile
tractor
mobile home, manufactured home
tricycle, trike, velocipede
unicycle, monocycle
horse cart, horse-cart
mosquito net
oxcart
bassinet
cradle
crib, cot
four-poster
bookcase
china cabinet, china closet
medicine chest, medicine cabinet
chiffonier, commode
table lamp
file, file cabinet, filing cabinet
pay-phone, pay-station
park bench
barber chair
throne
folding chair
rocking chair, rocker
studio couch, day bed
toilet seat
desk
pool table, billiard table, snooker table
dining table, board
entertainment center
wardrobe, closet, press
Granny Smith
orange
lemon
fig
pineapple, ananas
banana
jackfruit, jak, jack
custard apple
pomegranate
acorn
hip, rose hip, rosehip
ear, spike, capitulum
rapeseed
corn
buckeye, horse chestnut, conker
organ, pipe organ
upright, upright piano
chime, bell, gong
drum, membranophone, tympan
gong, tam-tam
maraca
marimba, xylophone
steel drum
banjo
cello, violoncello
lampshade, lamp shade
harp
acoustic guitar
electric guitar
cornet, horn, trumpet, trump
French horn, horn
trombone
harmonica, mouth organ, harp, mouth harp
ocarina, sweet potato
panpipe, pandean pipe, syrinx
bassoon
sax, saxophone
flute, transverse flute
daisy
yellow lady's slipper, yellow lady-slipper, Cypripedium calceolus, Cypripedium parviflorum
cliff, drop, drop-off
valley, vale
alp
volcano
promontory, headland, head, foreland
sandbar, sand bar
coral reef
lakeside, lakeshore
seashore, coast, seacoast, sea-coast
geyser
hatchet
cleaver, meat cleaver, chopper
letter opener, paper knife, paperknife
plane, carpenter's plane, woodworking plane
power drill
lawn mower, mower
hammer
corkscrew, bottle screw
can opener, tin opener
plunger, plumber's helper
screwdriver
shovel
plow, plough
chain saw, chainsaw
cock
hen
ostrich, Struthio camelus
brambling, Fringilla montifringilla
goldfinch, Carduelis carduelis
house finch, linnet, Carpodacus mexicanus
junco, snowbird
indigo bunting, indigo finch, indigo bird, Passerina cyanea
robin, American robin, Turdus migratorius
bulbul
jay
magpie
chickadee
water ouzel, dipper
kite
bald eagle, American eagle, Haliaeetus leucocephalus
vulture
great grey owl, great gray owl, Strix nebulosa
black grouse
ptarmigan
ruffed grouse, partridge, Bonasa umbellus
prairie chicken, prairie grouse, prairie fowl
peacock
quail
partridge
African grey, African gray, Psittacus erithacus
macaw
sulphur-crested cockatoo, Kakatoe galerita, Cacatua galerita
lorikeet
coucal
bee eater
hornbill
hummingbird
jacamar
toucan
drake
red-breasted merganser, Mergus serrator
goose
black swan, Cygnus atratus
white stork, Ciconia ciconia
black stork, Ciconia nigra
spoonbill
flamingo
American egret, great white heron, Egretta albus
little blue heron, Egretta caerulea
bittern
crane
limpkin, Aramus pictus
American coot, marsh hen, mud hen, water hen, Fulica americana
bustard
ruddy turnstone, Arenaria interpres
red-backed sandpiper, dunlin, Erolia alpina
redshank, Tringa totanus
dowitcher
oystercatcher, oyster catcher
European gallinule, Porphyrio porphyrio
pelican
king penguin, Aptenodytes patagonica
albatross, mollymawk
great white shark, white shark, man-eater, man-eating shark, Carcharodon carcharias
tiger shark, Galeocerdo cuvieri
hammerhead, hammerhead shark
electric ray, crampfish, numbfish, torpedo
stingray
barracouta, snoek
coho, cohoe, coho salmon, blue jack, silver salmon, Oncorhynchus kisutch
tench, Tinca tinca
goldfish, Carassius auratus
eel
rock beauty, Holocanthus tricolor
anemone fish
lionfish
puffer, pufferfish, blowfish, globefish
sturgeon
gar, garfish, garpike, billfish, Lepisosteus osseus
loggerhead, loggerhead turtle, Caretta caretta
mud turtle
terrapin
box turtle, box tortoise
banded gecko
common iguana, iguana, Iguana iguana
American chameleon, anole, Anolis carolinensis
whiptail, whiptail lizard
agama
frilled lizard, Chlamydosaurus kingi
alligator lizard
Gila monster, Heloderma suspectum
green lizard, Lacerta viridis
African chameleon, Chamaeleo chamaeleon
Komodo dragon, Komodo lizard, dragon lizard, giant lizard, Varanus komodoensis
triceratops
African crocodile, Nile crocodile, Crocodylus niloticus
American alligator, Alligator mississipiensis
thunder snake, worm snake, Carphophis amoenus
ringneck snake, ring-necked snake, ring snake
hognose snake, puff adder, sand viper
green snake, grass snake
king snake, kingsnake
garter snake, grass snake
water snake
vine snake
night snake, Hypsiglena torquata
boa constrictor, Constrictor constrictor
rock python, rock snake, Python sebae
Indian cobra, Naja naja
green mamba
sea snake
horned viper, cerastes, sand viper, horned asp, Cerastes cornutus
stone wall
sidewinder, horned rattlesnake, Crotalus cerastes
European fire salamander, Salamandra salamandra
common newt, Triturus vulgaris
eft
spotted salamander, Ambystoma maculatum
axolotl, mud puppy, Ambystoma mexicanum
bullfrog, Rana catesbeiana
tree frog, tree-frog
tailed frog, bell toad, ribbed toad, tailed toad, Ascaphus trui
whistle
wing
paintbrush
oxygen mask
snorkel
loudspeaker, speaker, speaker unit, loudspeaker system, speaker system
microphone, mike
screen, CRT screen
mouse, computer mouse
electric fan, blower
oil filter
strainer
space heater
stove
guillotine
barometer
rule, ruler
odometer, hodometer, mileometer, milometer
scale, weighing machine
analog clock
digital clock
wall clock
hourglass
sundial
parking meter
stopwatch, stop watch
digital watch
stethoscope
syringe
magnetic compass
binoculars, field glasses, opera glasses
projector
sunglasses, dark glasses, shades
loupe, jeweler's loupe
radio telescope, radio reflector
bow
cannon
assault rifle, assault gun
rifle
projectile, missile
computer keyboard, keypad
typewriter keyboard
crane
lighter, light, igniter, ignitor
abacus
cash machine, cash dispenser, automated teller machine, automatic teller machine, automated teller, automatic teller, ATM
slide rule, slipstick
desktop computer
hand-held computer, hand-held microcomputer
notebook, notebook computer
padlock
harvester, reaper
thresher, thrasher, threshing machine
printer
slot, one-armed bandit
vending machine
sewing machine
joystick
switch, electric switch, electrical switch
hook, claw
car wheel
paddlewheel, paddle wheel
pinwheel
potter's wheel
gas pump, gasoline pump, petrol pump, island dispenser
carousel, carrousel, merry-go-round, roundabout, whirligig
swing
reel
radiator
puck, hockey puck
hard disc, hard disk, fixed disk
sunglass
pick, plectrum, plectron
car mirror
solar dish, solar collector, solar furnace
remote control, remote
disk brake, disc brake
buckle
hair slide
knot
combination lock
web site, website, internet site, site
nail
safety pin
screw
muzzle
seat belt, seatbelt
ski
candle, taper, wax light
jack-o'-lantern
spotlight, spot
torch
neck brace
pier
tripod
maypole
hand blower, blow dryer, blow drier, hair dryer, hair drier
mousetrap
spider web, spider's web
trilobite
harvestman, daddy longlegs, Phalangium opilio
scorpion
black and gold garden spider, Argiope aurantia
barn spider, Araneus cavaticus
garden spider, Aranea diademata
black widow, Latrodectus mactans
tarantula
wolf spider, hunting spider
tick
centipede
isopod
Dungeness crab, Cancer magister
rock crab, Cancer irroratus
fiddler crab
king crab, Alaska crab, Alaskan king crab, Alaska king crab, Paralithodes camtschatica
American lobster, Northern lobster, Maine lobster, Homarus americanus
spiny lobster, langouste, rock lobster, crawfish, crayfish, sea crawfish
crayfish, crawfish, crawdad, crawdaddy
hermit crab
tiger beetle
ladybug, ladybeetle, lady beetle, ladybird, ladybird beetle
ground beetle, carabid beetle
long-horned beetle, longicorn, longicorn beetle
leaf beetle, chrysomelid
dung beetle
rhinoceros beetle
weevil
fly
bee
grasshopper, hopper
cricket
walking stick, walkingstick, stick insect
cockroach, roach
mantis, mantid
cicada, cicala
leafhopper
lacewing, lacewing fly
dragonfly, darning needle, devil's darning needle, sewing needle, snake feeder, snake doctor, mosquito hawk, skeeter hawk
damselfly
admiral
ringlet, ringlet butterfly
monarch, monarch butterfly, milkweed butterfly, Danaus plexippus
cabbage butterfly
sulphur butterfly, sulfur butterfly
lycaenid, lycaenid butterfly
jellyfish
sea anemone, anemone
brain coral
flatworm, platyhelminth
nematode, nematode worm, roundworm
conch
snail
slug
sea slug, nudibranch
chiton, coat-of-mail shell, sea cradle, polyplacophore
sea urchin
sea cucumber, holothurian
iron, smoothing iron
espresso maker
microwave, microwave oven
Dutch oven
rotisserie
toaster
waffle iron
vacuum, vacuum cleaner
dishwasher, dish washer, dishwashing machine
refrigerator, icebox
washer, automatic washer, washing machine
Crock Pot
frying pan, frypan, skillet
wok
caldron, cauldron
coffeepot
teapot
spatula
altar
triumphal arch
patio, terrace
steel arch bridge
suspension bridge
viaduct
barn
greenhouse, nursery, glasshouse
palace
monastery
library
apiary, bee house
boathouse
church, church building
mosque
stupa, tope
planetarium
restaurant, eating house, eating place, eatery
cinema, movie theater, movie theatre, movie house, picture palace
home theater, home theatre
lumbermill, sawmill
coil, spiral, volute, whorl, helix
obelisk
totem pole
castle
prison, prison house
grocery store, grocery, food market, market
bakery, bakeshop, bakehouse
barbershop
bookshop, bookstore, bookstall
butcher shop, meat market
confectionery, confectionary, candy store
shoe shop, shoe-shop, shoe store
tobacco shop, tobacconist shop, tobacconist
toyshop
fountain
cliff dwelling
yurt
dock, dockage, docking facility
brass, memorial tablet, plaque
megalith, megalithic structure
bannister, banister, balustrade, balusters, handrail
breakwater, groin, groyne, mole, bulwark, seawall, jetty
dam, dike, dyke
chainlink fence
picket fence, paling
worm fence, snake fence, snake-rail fence, Virginia fence
diamondback, diamondback rattlesnake, Crotalus adamanteus
grille, radiator grille
sliding door
turnstile
mountain tent
scoreboard
honeycomb
plate rack
pedestal, plinth, footstall
beacon, lighthouse, beacon light, pharos
leatherback turtle, leatherback, leathery turtle, Dermochelys coriacea
mashed potato
bell pepper
head cabbage
broccoli
cauliflower
zucchini, courgette
spaghetti squash
acorn squash
butternut squash
cucumber, cuke
artichoke, globe artichoke
cardoon
mushroom
shower curtain
jean, blue jean, denim
carton
handkerchief, hankie, hanky, hankey
sandal
ashcan, trash can, garbage can, wastebin, ash bin, ash-bin, ashbin, dustbin, trash barrel, trash bin
safe
plate
necklace
croquet ball
fur coat
thimble
pajama, pyjama, pj's, jammies
running shoe
oboe, hautboy, hautbois
cocktail shaker
chest
manhole cover
modem
tub, vat
tray
balance beam, beam
bagel, beigel
violin, fiddle
prayer rug, prayer mat
kimono
hot pot, hotpot
whiskey jug
knee pad
book jacket, dust cover, dust jacket, dust wrapper
spindle
ski mask
beer bottle
crash helmet
bottlecap
tile roof
mask
maillot
Petri dish
football helmet
bathing cap, swimming cap
teddy, teddy bear
holster
pop bottle, soda bottle
photocopier
vestment
crossword puzzle, crossword
golf ball
trifle
suit, suit of clothes
water tower
feather boa, boa
cloak
red wine
drumstick
shield, buckler
Christmas stocking
hoopskirt, crinoline
menu
stage
bonnet, poke bonnet
meat loaf, meatloaf
baseball
face powder
scabbard
sunscreen, sunblock, sun blocker
beer glass
hen-of-the-woods, hen of the woods, Polyporus frondosus, Grifola frondosa
guacamole
wool, woolen, woollen
hay
bow tie, bow-tie, bowtie
mailbag, postbag
water jug
bucket, pail
dishrag, dishcloth
soup bowl
eggnog
mortar
trench coat
paddle, boat paddle
chain
swab, swob, mop
mixing bowl
potpie
wine bottle
shoji
bulletproof vest
drilling platform, offshore rig
binder, ring-binder
cardigan
sweatshirt
pot, flowerpot
birdhouse
jinrikisha, ricksha, rickshaw
hamper
ping-pong ball
pencil box, pencil case
consomme
apron
punching bag, punch bag, punching ball, punchball
backpack, back pack, knapsack, packsack, rucksack, haversack
groom, bridegroom
bearskin, busby, shako
pencil sharpener
broom
abaya
mortarboard
poncho
crutch
Polaroid camera, Polaroid Land camera
space bar
cup
racket, racquet
traffic light, traffic signal, stoplight
quill, quill pen
radio, wireless
snow leopard, ounce, Panthera uncia
dough
cuirass
military uniform
lipstick, lip rouge
shower cap
monitor
oscilloscope, scope, cathode-ray oscilloscope, CRO
mitten
brassiere, bra, bandeau
French loaf
vase
milk can
rugby ball
paper towel
earthstar
envelope
miniskirt, mini
cowboy hat, ten-gallon hat
trolleybus, trolley coach, trackless trolley
perfume, essence
bathtub, bathing tub, bath, tub
hotdog, hot dog, red hot
coral fungus
bullet train, bullet
pillow
toilet tissue, toilet paper, bathroom tissue
cassette
carpenter's kit, tool kit
ladle
stinkhorn, carrion fungus
lotion
hair spray
academic gown, academic robe, judge's robe
dome
crate
wig
burrito
pill bottle
chain mail, ring mail, mail, chain armor, chain armour, ring armor, ring armour
theater curtain, theatre curtain
window shade
barrel, cask
washbasin, handbasin, washbowl, lavabo, wash-hand basin
ballpoint, ballpoint pen, ballpen, Biro
basketball
bath towel
cowboy boot
gown
window screen
agaric
standard poodle
cellular telephone, cellular phone, cellphone, cell, mobile phone
nipple
barbell
mailbox, letter box
lab coat, laboratory coat
fire screen, fireguard
minibus
packet
brown bear, bruin, Ursus arctos
pole
horizontal bar, high bar
sombrero
pickelhaube
rain barrel
wallet, billfold, notecase, pocketbook
cassette player
comic book
piggy bank, penny bank
street sign
bell cote, bell cot
fountain pen
Windsor tie
volleyball
overskirt
sarong
purse
bolo tie, bolo, bola tie, bola
bib
parachute, chute
sleeping bag
television, television system
swimming trunks, bathing trunks
measuring cup
espresso
pizza, pizza pie
breastplate, aegis, egis
shopping basket
wooden spoon
saltshaker, salt shaker
chocolate sauce, chocolate syrup
ballplayer, baseball player
goblet
gyromitra
stretcher
water bottle
skunk, polecat, wood pussy
soap dispenser
jersey, T-shirt, tee shirt
school bus
jigsaw puzzle
plastic bag
reflex camera
diaper, nappy, napkin
Band Aid
ice lolly, lolly, lollipop, popsicle
velvet
tennis ball
gasmask, respirator, gas helmet
doormat, welcome mat
Loafer
ice cream, icecream
pretzel
quilt, comforter, comfort, puff
maillot, tank suit
tape player
clog, geta, patten, sabot
iPod
bolete
meerkat, mierkat
scuba diver
pitcher, ewer
matchstick
bikini, two-piece
sock
CD player
lens cap, lens cover
thatch, thatched roof
vault
beaker
bubble
cheeseburger
parallel bars, bars
flagpole, flagstaff
coffee mug
rubber eraser, rubber, pencil eraser
stole
carbonara
dumbbell

Synsets new in ILSVRC2012

Siberian husky
English springer, English springer spaniel
malamute, malemute, Alaskan malamute
Walker hound, Walker foxhound
Welsh springer spaniel
whippet
Weimaraner
soft-coated wheaten terrier
Dandie Dinmont, Dandie Dinmont terrier
Old English sheepdog, bobtail
otterhound, otter hound
bloodhound, sleuthhound
Airedale, Airedale terrier
giant schnauzer
black-and-tan coonhound
papillon
Mexican hairless
Cardigan, Cardigan Welsh corgi
malinois
Lhasa, Lhasa apso
Norwegian elkhound, elkhound
Rottweiler
Saluki, gazelle hound
schipperke
Brabancon griffon
West Highland white terrier
Sealyham terrier, Sealyham
Irish wolfhound
EntleBucher
French bulldog
Bernese mountain dog
Maltese dog, Maltese terrier, Maltese
Norfolk terrier
toy terrier
cairn, cairn terrier
groenendael
clumber, clumber spaniel
Afghan hound, Afghan
Japanese spaniel
borzoi, Russian wolfhound
toy poodle
Kerry blue terrier
Scotch terrier, Scottish terrier, Scottie
Boston bull, Boston terrier
Greater Swiss Mountain dog
Appenzeller
Shih-Tzu
Irish water spaniel
Pomeranian
Bedlington terrier
miniature schnauzer
collie
Irish terrier
affenpinscher, monkey pinscher, monkey dog
silky terrier, Sydney silky
beagle
Leonberg
German short-haired pointer
dhole, Cuon alpinus
Chesapeake Bay retriever
bull mastiff
kuvasz
pug, pug-dog
curly-coated retriever
Norwich terrier
keeshond
Lakeland terrier
standard schnauzer
Tibetan terrier, chrysanthemum dog
wire-haired fox terrier
basset, basset hound
chow, chow chow
American Staffordshire terrier, Staffordshire terrier, American pit bull terrier, pit bull terrier
Shetland sheepdog, Shetland sheep dog, Shetland
Great Pyrenees
Chihuahua
Labrador retriever
Samoyed, Samoyede
bluetick
kelpie
miniature pinscher
Italian greyhound
cocker spaniel, English cocker spaniel, cocker
Sussex spaniel
Pembroke, Pembroke Welsh corgi
Blenheim spaniel
Ibizan hound, Ibizan Podenco
English foxhound
briard
Border terrier
'''

