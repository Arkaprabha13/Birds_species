# Important imports
from app import app
from flask import request, render_template
from keras import models
import numpy as np
from PIL import Image
import string
import random
import os
from sklearn.metrics import f1_score

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'

# Loading model
model = models.load_model('app/static/model/InceptionV3_model.h5')

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():

    # Execute if request is GET
    if request.method == "GET":
        full_filename =  'images/white_bg.jpg'
        return render_template("index.html", full_filename=full_filename)

    # Execute if request is POST
    if request.method == "POST":

        # Generating unique image name
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10)) + '.png'
        full_filename = 'uploads/' + name

        image_upload = request.files['image_upload']
  
        if image_upload.filename.split('.')[-1] not in ['jpg', 'jpeg', 'png']:
            return "Unsupported file format. Please upload an image file with .jpg, .jpeg, or .png extension."

        image = Image.open(image_upload)
        image = image.resize((224, 224))
        image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], name))
        image_arr = np.array(image.convert('RGB'))

        # Predicting output
        result = model.predict(np.expand_dims(image_arr, axis=0))
        print(result)
        ind = np.argmax(result)
        classes =['ANTILLEAN EUPHONIA', 'SAYS PHOEBE', 'GREEN MAGPIE', 'BELTED KINGFISHER', 'DEMOISELLE CRANE', 'BANDED STILT', 'BLACK THROATED WARBLER', 
            'RUFOUS TREPE', 'HORNED GUAN', 'AMERICAN COOT', 'ELEGANT TROGON', 'DUNLIN',
            'VERMILION FLYCATHER', 'AFRICAN CROWNED CRANE', 'PARADISE TANAGER', 'JABIRU',
            'SANDHILL CRANE', 'WILD TURKEY', 'CLARKS GREBE', 'TASMANIAN HEN', 'JANDAYA PARAKEET',
            'CASPIAN TERN', 'CRESTED WOOD PARTRIDGE', 'BLUE GROSBEAK', 'BAND TAILED GUAN', 'IBERIAN MAGPIE',
            'EASTERN TOWEE', 'HAMERKOP', 'CRESTED AUKLET', 'DALMATIAN PELICAN', 'RED BROWED FINCH', 'GREATER PEWEE', 
            'BAY-BREASTED WARBLER', 'STRIPPED MANAKIN', 'ANHINGA', 'MILITARY MACAW', 'SPANGLED COTINGA', 'RAZORBILL', 
            'PUFFIN', 'BIRD OF PARADISE', 'ROSE BREASTED GROSBEAK', 'HYACINTH MACAW', 'SWINHOES PHEASANT',
            'LESSER ADJUTANT', 'KAKAPO', 'CHATTERING LORY', 'ANDEAN LAPWING', 'CHIPPING SPARROW',
            'TIT MOUSE', 'MALLARD DUCK', 'BLACK VULTURE', 'D-ARNAUDS BARBET', 'LAZULI BUNTING',
            'RUBY CROWNED KINGLET', 'COCK OF THE  ROCK', 'COMMON GRACKLE', 'POMARINE JAEGER',
            'KING EIDER', 'PEREGRINE FALCON', 'PATAGONIAN SIERRA FINCH', 'MARABOU STORK', 'GREY PLOVER', 
            'SNOWY PLOVER', 'YELLOW HEADED BLACKBIRD', 'RED LEGGED HONEYCREEPER', 'CHESTNET BELLIED EUPHONIA',
            'HIMALAYAN BLUETAIL', 'UMBRELLA BIRD', 'WHITE EARED HUMMINGBIRD', 'BLACK SWAN', 'INDIGO BUNTING',
            'CRESTED COUA', 'CLARKS NUTCRACKER', 'BREWERS BLACKBIRD', 'RED WISKERED BULBUL', 'STRIPED OWL', 'MANDRIN DUCK', 
            'RUFOUS KINGFISHER', 'BLACK HEADED CAIQUE', 'FOREST WAGTAIL', 'AFRICAN FIREFINCH', 'NORTHERN CARDINAL',
            'LILAC ROLLER', 'GAMBELS QUAIL', 'CAPE GLOSSY STARLING', 'TOUCHAN', 'CREAM COLORED WOODPECKER',
            'SCARLET FACED LIOCICHLA', 'BLOOD PHEASANT', 'BARRED PUFFBIRD', 'STORK BILLED KINGFISHER', 
            'SQUACCO HERON', 'ASIAN DOLLARD BIRD', 'WALL CREAPER', 'EMPEROR PENGUIN', 'LUCIFER HUMMINGBIRD', 
            'NORTHERN RED BISHOP', 'AFRICAN EMERALD CUCKOO', 'PARAKETT  AUKLET', 'EASTERN YELLOW ROBIN',
            'STEAMER DUCK', 'GRAY KINGBIRD', 'HORNED LARK', 'GREAT TINAMOU', 'VIOLET TURACO', 'NORTHERN SHOVELER',
            'HELMET VANGA', 'SPOTTED WHISTLING DUCK', 'CRANE HAWK', 'GILA WOODPECKER', 'LIMPKIN', 'PUNA TEAL',
            'PINK ROBIN', 'FRILL BACK PIGEON', 'GOULDIAN FINCH', 'HOODED MERGANSER', 'GREAT XENOPS', 'MALABAR HORNBILL', 
            'CHUKAR PARTRIDGE', 'DOWNY WOODPECKER', 'NORTHERN JACANA', 'MANGROVE CUCKOO', 'BLACK THROATED HUET',
            'CALIFORNIA QUAIL', 'ASHY THRUSHBIRD', 'JOCOTOCO ANTPITTA', 'CANVASBACK', 'GUINEA TURACO', 'RED TAILED THRUSH',
            'AMERICAN WIGEON', 'SHOEBILL', 'SCARLET IBIS', 'DOUBLE EYED FIG PARROT', 'SPOON BILED SANDPIPER',
            'MAGPIE GOOSE', 'BLUE HERON', 'PURPLE SWAMPHEN', 'PHAINOPEPLA', 'CHARA DE COLLAR', 'BLACK-THROATED SPARROW',
            'AZURE TANAGER', 'CAPPED HERON', 'SCARLET CROWNED FRUIT DOVE', 'NORTHERN FULMAR', 'SPLENDID WREN',
            'AMERICAN BITTERN', 'BRANDT CORMARANT', 'WHIMBREL', 'FLAME BOWERBIRD', 'CAPE LONGCLAW', 'TAIWAN MAGPIE',
            'EUROPEAN TURTLE DOVE', 'CINNAMON TEAL', 'APAPANE', 'ANDEAN SISKIN', 'ASIAN CRESTED IBIS', 'ZEBRA DOVE',
            'AMERICAN PIPIT', 'SNOWY OWL', 'GREY HEADED FISH EAGLE', 'TAWNY FROGMOUTH', 'CRAB PLOVER', 'INDIAN BUSTARD',
            'BUFFLEHEAD', 'WATTLED LAPWING', 'CRESTED FIREBACK', 'AFRICAN OYSTER CATCHER', 'HOOPOES', 'HARLEQUIN QUAIL',
            'MALEO', 'ANNAS HUMMINGBIRD', 'AMERICAN AVOCET', 'GOLDEN PIPIT', 'MALAGASY WHITE EYE', 'AMERICAN FLAMINGO', 
            'STRIPPED SWALLOW', 'VIOLET CUCKOO', 'YELLOW BREASTED CHAT', 'OSPREY', 'CAPE MAY WARBLER', 
            'BLACK VENTED SHEARWATER', 'CINNAMON FLYCATCHER', 'GOLDEN EAGLE', 'DOUBLE BARRED FINCH', 'SAMATRAN THRUSH', 
            'ROCK DOVE', 'BLACK SKIMMER', 'HARPY EAGLE', 'VIOLET BACKED STARLING', 'PEACOCK', 'CAPE ROCK THRUSH',
            'TREE SWALLOW', 'CACTUS WREN', 'NICOBAR PIGEON', 'VICTORIA CROWNED PIGEON', 'HARLEQUIN DUCK',
            'DARJEELING WOODPECKER', 'WHITE BREASTED WATERHEN', 'KILLDEAR', 'TAKAHE', 'BORNEAN BRISTLEHEAD',
            'IWI', 'PURPLE GALLINULE', 'HOATZIN', 'BLACKBURNIAM WARBLER', 'GO AWAY BIRD', 'BEARDED REEDLING', 
            'ARARIPE MANAKIN', 'PURPLE MARTIN', 'DOUBLE BRESTED CORMARANT', 'GUINEAFOWL', 'STRIATED CARACARA',
            'KOOKABURRA', 'ASHY STORM PETREL', 'CRESTED OROPENDOLA', 'AMERICAN DIPPER', 'GREATOR SAGE GROUSE',
            'BLUE GROUSE', 'ORIENTAL BAY OWL', 'AUSTRAL CANASTERO', 'GREAT POTOO', 'BARN OWL', 'FAN TAILED WIDOW',
            'RUDY KINGFISHER', 'GRANDALA', 'EMERALD TANAGER', 'AMERICAN REDSTART', 'ANTBIRD', 'MERLIN', 'AZURE TIT',
            'HIMALAYAN MONAL', 'CAATINGA CACHOLOTE', 'COLLARED CRESCENTCHEST', 'NORTHERN FLICKER', 'SNOWY SHEATHBILL',
            'WOOD THRUSH', 'DARK EYED JUNCO', 'LOONEY BIRDS', 'SORA', 'TEAL DUCK', 'CRESTED CARACARA', 'BANDED PITA',
            'BLUE THROATED TOUCANET', 'BURCHELLS COURSER', 'WHITE BROWED CRAKE', 'DUSKY LORY', 'ECUADORIAN HILLSTAR', 
            'PLUSH CRESTED JAY', 'GREY CUCKOOSHRIKE', 'PURPLE FINCH', 'EASTERN WIP POOR WILL', 'WHITE NECKED RAVEN',
            'GREEN WINGED DOVE', 'WHITE THROATED BEE EATER', 'EVENING GROSBEAK', 'ANDEAN GOOSE', 'COPPERY TAILED COUCAL',
            'EURASIAN MAGPIE', 'GREATER PRAIRIE CHICKEN', 'TRUMPTER SWAN', 'INDIAN ROLLER', 'CRESTED SHRIKETIT', 
            'APOSTLEBIRD', 'CHUCAO TAPACULO', 'GYRFALCON', 'BALTIMORE ORIOLE', 'MASKED LAPWING', 'CUBAN TROGON', 
            'JACK SNIPE', 'CHINESE POND HERON', 'PHILIPPINE EAGLE', 'COMMON POORWILL', 'RED FACED WARBLER', 
            'BLACK FRANCOLIN', 'SNOW PARTRIDGE', 'ROSEATE SPOONBILL', 'CASSOWARY', 'FAIRY BLUEBIRD',
            'BLUE THROATED PIPING GUAN', 'IVORY GULL', 'TURKEY VULTURE', 'RED HEADED DUCK', 'LAUGHING GULL',
            'FIRE TAILLED MYZORNIS', 'EUROPEAN GOLDFINCH', 'FASCIATED WREN', 'GANG GANG COCKATOO', 'BROWN CREPPER',
            'EARED PITA', 'RED HEADED WOODPECKER', 'COMMON LOON', 'MOURNING DOVE', 'OVENBIRD', 'VENEZUELIAN TROUPIAL',
            'GURNEYS PITTA', 'JAVA SPARROW', 'BOBOLINK', 'MALACHITE KINGFISHER', 'HORNED SUNGEM', 'HAWAIIAN GOOSE',
            'SPOTTED CATBIRD', 'QUETZAL', 'MASKED BOOBY', 'VEERY', 'PARUS MAJOR', 'KING VULTURE', 'ROSE BREASTED COCKATOO',
            'SAND MARTIN', 'ELLIOTS  PHEASANT', 'SURF SCOTER', 'SCARLET TANAGER', 'MASKED BOBWHITE', 'MIKADO  PHEASANT',
            'NORTHERN BEARDLESS TYRANNULET', 'YELLOW CACIQUE', 'GRAY PARTRIDGE', 'KNOB BILLED DUCK', 'ENGGANO MYNA',
            'AMERICAN KESTREL', 'PALM NUT VULTURE', 'BROWN HEADED COWBIRD', 'VULTURINE GUINEAFOWL', 'CEDAR WAXWING',
            'EMU', 'BLACK TAIL CRAKE', 'SCARLET MACAW', 'PALILA', 'REGENT BOWERBIRD', 'CRESTED KINGFISHER', 
            'RED BELLIED PITTA', 'TAILORBIRD', 'GOLDEN BOWER BIRD', 'INDIGO FLYCATCHER', 'BORNEAN PHEASANT', 
            'EURASIAN BULLFINCH', 'BARN SWALLOW', 'BROWN NOODY', 'BLUE MALKOHA', 'AZURE JAY', 'AMERICAN ROBIN',
            'HEPATIC TANAGER', 'FIERY MINIVET', 'ALPINE CHOUGH', 'BLACK BREASTED PUFFBIRD', 'EURASIAN GOLDEN ORIOLE',
            'CURL CRESTED ARACURI', 'MCKAYS BUNTING', 'CARMINE BEE-EATER', 'LARK BUNTING', 'ABBOTTS BABBLER',
            'INDIAN PITTA', 'BULWERS PHEASANT', 'GROVED BILLED ANI', 'TRICOLORED BLACKBIRD', 'COMMON IORA', 'FAIRY TERN',
            'BALD EAGLE', 'ALEXANDRINE PARAKEET', 'CERULEAN WARBLER', 'ALBERTS TOWHEE', 'BLACK AND YELLOW BROADBILL',
            'VERDIN', 'CRESTED SERPENT EAGLE', 'NORTHERN GOSHAWK', 'KIWI', 'CAMPO FLICKER', 'PYGMY KINGFISHER',
            'CHINESE BAMBOO PARTRIDGE', 'BLACK NECKED STILT', 'BALI STARLING', 'EASTERN ROSELLA', 'FRIGATE',
            'BLACK FACED SPOONBILL', 'WOODLAND KINGFISHER', 'FLAME TANAGER', 'WHITE CRESTED HORNBILL', 'ROYAL FLYCATCHER', 
            'VARIED THRUSH', 'BLACK-NECKED GREBE', 'ABBOTTS BOOBY', 'LONG-EARED OWL', 'HOUSE FINCH', 'HOUSE SPARROW',
            'PAINTED BUNTING', 'BLUE GRAY GNATCATCHER', 'VISAYAN HORNBILL', 'SNOW GOOSE', 'KAGU', 'CANARY', 
            'LOGGERHEAD SHRIKE', 'SNOWY EGRET', 'COMMON FIRECREST', 'OYSTER CATCHER', 'CRESTED NUTHATCH', 'AVADAVAT',
            'COMMON HOUSE MARTIN', 'BLUE COAU', 'COMMON STARLING', 'ROADRUNNER', 'HAWFINCH', 'GILDED FLICKER',
            'BLACK-CAPPED CHICKADEE', 'RING-NECKED PHEASANT', 'WOOD DUCK', 'GREEN BROADBILL', 'VIOLET GREEN SWALLOW', 
            'OSTRICH', 'GREAT ARGUS', 'GOLDEN PARAKEET', 'BLONDE CRESTED WOODPECKER', 'RED NAPED TROGON', 
            'ABYSSINIAN GROUND HORNBILL', 'BARROWS GOLDENEYE', 'WHITE CHEEKED TURACO', 'ORANGE BRESTED BUNTING',
            'CHESTNUT WINGED CUCKOO', 'ORNATE HAWK EAGLE', 'AMERICAN GOLDFINCH', 'EASTERN MEADOWLARK', 
            'AFRICAN PIED HORNBILL', 'LITTLE AUK', 'OKINAWA RAIL', 'TOWNSENDS WARBLER', 'INLAND DOTTEREL',
            'GREEN JAY', 'BALD IBIS', 'DAURIAN REDSTART', 'NORTHERN MOCKINGBIRD', 'GOLDEN CHEEKED WARBLER', 
            'NORTHERN PARULA', 'CRIMSON CHAT', 'RED BEARDED BEE EATER', 'EASTERN BLUEBONNET', 'RED CROSSBILL',
            'SUNBITTERN', 'BLACK COCKATO', 'RED TAILED HAWK', 'RED BILLED TROPICBIRD', 'COLLARED ARACARI', 
            'CAPUCHINBIRD', 'ASIAN GREEN BEE EATER', 'GRAY CATBIRD', 'BAR-TAILED GODWIT', 'INDIAN VULTURE', 
            'OCELLATED TURKEY', 'YELLOW BELLIED FLOWERPECKER', 'SUPERB STARLING', 'CUBAN TODY', 'ALBATROSS',
            'BAIKAL TEAL', 'RAINBOW LORIKEET', 'EASTERN GOLDEN WEAVER', 'INCA TERN', 'ANIANIAU', 'WILLOW PTARMIGAN',
            'JACOBIN PIGEON', 'BORNEAN LEAFBIRD', 'AUSTRALASIAN FIGBIRD', 'BLACK THROATED BUSHTIT', 
            'RUBY THROATED HUMMINGBIRD', 'WILSONS BIRD OF PARADISE', 'AUCKLAND SHAQ', 'GREAT JACAMAR', 'FAIRY PENGUIN',
            'RED FACED CORMORANT', 'CROW', 'CRIMSON SUNBIRD', 'RUDDY SHELDUCK', 'AZURE BREASTED PITTA',
            'SHORT BILLED DOWITCHER', 'CALIFORNIA GULL', 'MYNA', 'AMETHYST WOODSTAR', 'BEARDED BARBET', 
            'ORANGE BREASTED TROGON', 'EGYPTIAN GOOSE', 'OILBIRD', 'EASTERN BLUEBIRD', 'WRENTIT', 'NOISY FRIARBIRD',
            'BANDED BROADBILL', 'GOLDEN CHLOROPHONIA', 'BLACK BAZA', 'GREY HEADED CHACHALACA', 'RED FODY', 
            'AFRICAN PYGMY GOOSE', 'ROSY FACED LOVEBIRD', 'TROPICAL KINGBIRD', 'CINNAMON ATTILA', 'WATTLED CURASSOW',
            'PYRRHULOXIA', 'COCKATOO', 'GLOSSY IBIS', 'AZARAS SPINETAIL', 'RED SHOULDERED HAWK', 'BEARDED BELLBIRD',
            'SMITHS LONGSPUR', 'RUFUOS MOTMOT', 'ASIAN OPENBILL STORK', 'IVORY BILLED ARACARI', 'TURQUOISE MOTMOT', 
            'SRI LANKA BLUE MAGPIE', 'JAPANESE ROBIN', 'GREAT GRAY OWL', 'NORTHERN GANNET', 'RED KNOT', 'ROUGH LEG BUZZARD', 
            'FIORDLAND PENGUIN', 'WHITE TAILED TROPIC', 'GOLD WING WARBLER', 'IMPERIAL SHAQ', 'COPPERSMITH BARBET', 
            'BLUE DACNIS', 'RED WINGED BLACKBIRD', 'CABOTS TRAGOPAN', 'GREAT KISKADEE', 'IBISBILL', 'BANANAQUIT', 
            'BROWN THRASHER', 'ALTAMIRA YELLOWTHROAT', 'DUSKY ROBIN', 'BUSH TURKEY', 'SATYR TRAGOPAN', 'CALIFORNIA CONDOR', 
            'GOLDEN PHEASANT']
        print("index ->",ind,"class ->",classes[ind])
        # Returning template, filename, and prediction
        return render_template('index.html', full_filename=full_filename, pred=classes[ind])

# Main function
if __name__ == '__main__':
    app.run(debug=True)
