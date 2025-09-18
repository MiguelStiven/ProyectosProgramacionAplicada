# #### Get A Key #OBTENER UNA CLAVE
# #you can access the values in it by providing the key: #PODER ACCEDER A LOS VALORES PROPORCIONANDO LA CLAVE

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3} #CREA UN NUEVO DICCIONARIO
# print(building_heights["Burj Khalifa"]) # Prints 828 #IMPRIME EL VALOR CORRESPONDIENTE A LA CALVE "BURJ KHALIFA" UBICADO EN EL DICCIONARIO BUILDING_HEIGHTS
# print(building_heights["Ping An"]) # Prints 599 #IMPRIME EL VALOR CORRESPONDIENTE A LA CALVE "PING AN" UBICADO EN EL DICCIONARIO BUILDING_HEIGHTS

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}  #CREA UN NUEVO DICCIONARIO EN DONDE LAS CLAVES SON "WATER", "FIRE," "EARTH" Y "AIR" Y SUS VALORES SON LAS LISTAS QUE SE DESPRENDEN DE CADA UNO DE ELLOS
# print(zodiac_elements["earth"]) #IMPRIME LOS VALORES (LISTA) CORRESPONDIENTE A LA CALVE "EARTH" UBICADO EN EL DICCIONARIO ZODIAC_ELEMENTS
# print(zodiac_elements["fire"]) #IMPRIME LOS VALORES (LISTA) CORRESPONDIENTE A LA CALVE "FIRE" UBICADO EN EL DICCIONARIO ZODIAC_ELEMENTS

# ## Get an Invalid Key #OBTENER UN CLAVE NO VALIDA

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3} #CREA EL DICCIONARIO BUILDING_HEIGHTS
# print(building_heights["Landmark 81"]) #PARA IMPRIMIR UNA CLAVE QUE NO EXISTE (PYTHON LANZARA UN ERROR)

# ##One way to avoid this error is to first check if the key exists in the dictionary: #PRIMERO SE DEBE COMPROBAR SI LA CLAVE EXISTE EN EL DICCIONARIO
# key_to_check = "Landmark 81" #SE DEBE CHECAR LA CLAVE

# if key_to_check in building_heights: COMPRUBEA SI LA CLAVE ESTA EN EL DICCIONARIO 
#   print(building_heights["Landmark 81"]) #SI EXISTE, IMPRIME EL VALOR ASOCIADO A LA CLAVE 

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]} #CREA EL DICCIONARIO ZODIAC_ELEMENTS

# zodiac_elements["energy"] = "Not a Zodiac element" #MODIFICA EL DICCIONARIO AGREGANDO UNA NUEVA CLAVE (ENERGY) CON SU RESPECTIVO VALOR ("NOT A ZODIAC ELEMENT")

# if "energy" in zodiac_elements: #SI LA CLAVE EXISTE DENTRO DEL DICCIONARIO ZODIAC_ELEMENTS
#   print(zodiac_elements["energy"]) #IMPRIMIRA EL CONTENIDO DE ZOIDAC_ELEMENTS[ENERGY]

# ##Safely Get a Key #OBTENER UNA LLAVE DE FORMA SEGURA
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3} #CREA EL DICCIONARIO BUILDING_HEIGHTS

# #this line will return 632: #ESTA LINEA RETORNA 632
# building_heights.get("Shanghai Tower") #RECUPERA EL VALOR DE LA CLAVE SIN GENERAR ALGUN TIPO DE ERROR SI LA CLAVE NO EXISTE

# #this line will return None: # ESTA LINEA DEVOLVERA NONE
# building_heights.get("My House") # SI LA CLAVE NO EXISTE NO ARROJARA ERROR SINO QUE RETORNARA NONE

# ###
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384} #CREA UN DICCIONARIO LLAMADO USER_IDS
# user_ids.get("teraCoder") #RECUPERA EL VALOR DE LA CLAVE "TERACODER" SIN ERROR ALGUNO (ARROJARA 100019) (YA NO ARROJARA UN KEYERROR)

# if user_ids.get("teraCoder") == None: #COMPROBRA SI LA CLAVE NO SE ENCUENTRA EN EL DICCIONARIO Y TIENE UN VALOR VERDADERO 
#    tc_id = 1000 #SI LA CLAVE NO EXISTE ASIGNA 1000 A LA VARIABLE tc_id
# else: 
#    tc_id = user_ids.get("teraCoder") # SI LA CLAVE EXISTE, ASIGNA EL VALOR A tc_id ESTE SERA EL DE "teracorder" 

# print(tc_id) #IMPRIMIRA EL VALOR DE tc_id

# if user_ids.get("superStackSmash") == None: #COMPROBRA SI LA CLAVE NO SE ENCUENTRA EN EL DICCIONARIO Y TIENE UN VALOR VERDADERO 
#      stack_id = 100000 #SI LA CLAVE NO EXISTE TOMARA EL VALOR DE stack_id (100000)

# print(stack_id) #IMPRIME EL VALOR ASIGNADO EN LA VARIABLE stack_id

# ###Delete a Key #BORRAR UNA CLAVE
#.pop() works to delete items from a dictionary, when you know the key value. #LA FUNCION pop() ELIMINA ELEMENTOS DEL DICCIONARIO CONOCIDA SU CLAVE Y DEVUELVE SU VALOR
#raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"} #CREA EL DICCIONARIO LLAMADO raffle
#print(raffle.pop(320291, "No Prize")) # ELIMINA EL ELEMENTO ASOCIADO A LA CLAVE 320291, DEVOLVIENDO SU VALOR ASIGNADO (GIFT BASKET) Y LO IMPRIME, SI LA CLASE NO EXISTIERA RROJARIA NO PRIZE
## Prints "Gift Basket"

#print(raffle) #IMPRIME EL DICCIONARIO raffle CON LA CLAVE ELIMINADA (GIFT BASKET)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"} #ESTO ES LO QUE IMPRIMIRA, ES DECIR SIN "GIFT BASKET"
# print(raffle.pop(100000, "No Prize")) #INTENTARA ELIMINAR EL ELEMENTO ASOCIADO A LA CLAVE 100000, PERO COMO NO EXISTE IMPRIMIRA NO PRIZE
# # Prints "No Prize"

# print(raffle)#IMPRIME EL DICCIONARIO TAL CUAL COMO ESTABA YA QUE NO SE ELIMINO NINGUNA CLAVE PUESTO A QUE NO EXISTIA
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"} #ESTO ES LO QUE DEBE IMPRIMIR
# print(raffle.pop(872921, "No Prize")) #ELIMINA EL ELEMENTO ASOCIADO A LA CLAVE 872921, DEVOLVIENDO SU VALOR ASIGNADO (CONCERT TICKETS) Y LO IMPRIME, EN CASO DE QUE NO EXISTIERA IMPRIMIRIA "NO PRIZE"
# # Prints "Concert Tickets" #ESTO ES LO QUE DEBE IMPRIMIR YA QUE ES EL VALOR ASOCIADO CON LA CLAVE ELIMINDA
# print(raffle) #IMPRIMIRA EL NUEVO DICCIONARIO CON LA CLAVE ELIMINADA (CONCERT TICKETS)
# # Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"} #ESTO ES LO QUE IMPRIME

# available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30} #CREA EL DICCIONARIO LLAMADO AVAILABLE_ITEMS
# health_points = 20 #CREA LA VARIABLE HEALT_POINTS Y LE ASIGNA EL VALOR DE 20

# health_points += available_items.pop("stamina grains", 0) #SUMARA EL VALOR ASIGNADO PARA HEALTH POINTS CON EL VALOR ASOCIADO A LA CLAVE A ELIMINAR, SI LA CLAVE NO EXISTE EL VALOR PARA SUMAR SERA 0
# health_points += available_items.pop("power stew", 0) #SUMARA EL VALOR ASIGNADO PARA HEALTH POINTS CON EL VALOR ASOCIADO A LA CLAVE A ELIMINAR, SI LA CLAVE NO EXISTE EL VALOR PARA SUMAR SERA 0
# health_points += available_items.pop("mystic bread", 0) #SUMARA EL VALOR ASIGNADO PARA HEALTH POINTS CON EL VALOR ASOCIADO A LA CLAVE A ELIMINAR, SI LA CLAVE NO EXISTE EL VALOR PARA SUMAR SERA 0

# print(available_items) #IMPRIMIRA EL NUEVO DICCIONARIO CON LAS CLAVES ELIMINADAS
# print(health_points) #IMPRIMIRA EL VALOR TOTAL DE LA SUMA REALIZADA CON CADA VALOR CORRESPONDIENTE DE CADA CLAVE ELIMINADA

# ##Get All Keys #obtener todas las claves
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]} #CREA UN NUEVO DICCIONARIO LLAMADO TEST_SCORES
# print(list(test_scores)) #IMPRIME UN LISTADO CON SOLO LAS CLAVES CONTENIDAS EN EL DICCIONARIO TEST_SCORES
# # Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"] #LO QUE IMPRIME

# for student in test_scores.keys(): #ITERA (RECORRE TODAS LAS CLAVES DEL DICCIONARIO) SOBRE TODAS LAS CLAVES DEL DICCIONARIO test_scores
#  print(student) #IMPRIME CADA CLAVE (NOMBRE DEL ESTUDIANTE) UNA POR UNA

# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384} #CREA UN NUEVO DICCIONARIO LLAMADO USER_IDS
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18} #CREA UN NUEVO DICCIONARIO LLAMADO NUM_EXERCISES

# users = user_ids.keys() #DEVOLVER UN OBJETO DE VISTA (COMO UNA VENTANA) CON TODAS LAS CLAVES DEL DICCIONARIO USER_IDS
# lessons = num_exercises.keys() #DEVOLVER UN OBJETO DE VISTA (COMO UNA VENTANA) TODAS LAS CLAVES DEL DICCIONARIO NUM_EXERCISES

# print(users) #IMPRIME EL CONTENIDO DE LA VARIABLE USERS (DICT KEYS(OBJETOS DE VISTA))
# print(lessons) #IMPRIME EL CONTENIDO DE LA VARIABLE LESSONS (DICT KEYS (OBJETOS DE VISTA))

##Get All Values #OBTENER TODOS LOS VALORES
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}#CREA UN NUEVO DICCIONARIO LLAMADO TEST_SCORES

# for score_list in test_scores.values(): #ITERA (RECORRE TODOS LOS VALORES DEL DICCIONARIO) SOBRE TODOS LOS VALORES DEL DICCIONARIO test_scores
#  print(score_list) #IMPRIME CADA VALOR (PUNTUACION) UNO POR UNO
#EL FOR RECORRE CADA LISTA DE PUNTAJES

# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}#CREA UN NUEVO DICCIONARIO LLAMADO NUM_EXERCISES
# total_exercises = 0 # CREA UNA NUEVA VARIABLE Y LE ASIGNA 0

# for exercises in num_exercises.values():#ITERA (RECORRE TODOS LOS VALORES DEL DICCIONARIO) SOBRE TODOS LOS VALORES DEL DICCIONARIO num_exercises 
#EL FOR RECORRE CADA LISTA DEL NUMERO DE EJERCICIOS POR SECCION
#   total_exercises += exercises #SE REALIZA LA SUMA DE total_exercises(0) CON CADA UNO DE LOS VALORES
# print(total_exercises)#IMPRIME EL RESULTADO DE LA SUMA ENTRE total_exercises CON CADA UNO DE LOS VALORES DEL DICCIONARIO

##Get All Items #OBTENER TODOS LOS ITEMS
# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8} #SE CREA UN NUEVO DICCIONARIO LLAMADO biggest_brands

# for company, value in biggest_brands.items(): #ITERA (RECORRE TODOS PARES CLAVE-VALOR DEL DICCIONARIO) SOBRE TODOS LOS VALORES-CLAVES DEL DICCIONARIO biggest_brands 
#  print(company + " has a value of " + str(value) + " billion dollars. ")#IMPRIME LA CONCATENACION DE CADA CLAVE CON LA DE CADA VALOR SEGUN ESTE EN EL DICCIONARIO (EJEMPLO: Google has a value of 141.7 billion dollars)  

# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9} #SE CREA UN NUEVO DICCIONARIO LLAMADO pct_women_in_occupation

# for occupation, percentage in pct_women_in_occupation.items(): #ITERA (RECORRE TODOS PARES CLAVE-VALOR DEL DICCIONARIO) SOBRE TODOS LOS VALORES-CLAVES DEL DICCIONARIO pct_women_in_occupation

#   print("Women make up " + str(percentage) + " percent of " + occupation + "s.") #IMPRIME LA CONCATENACION DE CADA CLAVE CON LA DE CADA VALOR SEGUN ESTE EN EL DICCIONARIO (EJEMPLO: Women make up 40 percent of physicians)
