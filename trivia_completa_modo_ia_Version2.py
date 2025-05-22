from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import random

Window.clearcolor = (0.1, 0.1, 0.1, 1)

NUM_PREGUNTAS_PARTIDA = 8
NUM_JUGADORES = 4

# ------------------ TUS PREGUNTAS ------------------
preguntas = {
    "Ciencia": {
        "Fácil": [
            {"pregunta": "¿Cuál es el planeta más cercano al sol?", "respuestas": ["Mercurio", "Venus", "Marte", "Júpiter"], "correcta": "Mercurio"},
            {"pregunta": "¿Qué gas es esencial para la respiración humana?", "respuestas": ["Oxígeno", "Nitrógeno", "Hidrógeno", "Helio"], "correcta": "Oxígeno"},
            {"pregunta": "¿Cuál es la fórmula química del agua?", "respuestas": ["H2O", "CO2", "NaCl", "O2"], "correcta": "H2O"},
            {"pregunta": "¿Cuántos sentidos tiene el ser humano?", "respuestas": ["5", "4", "6", "3"], "correcta": "5"},
            {"pregunta": "¿Qué órgano bombea la sangre?", "respuestas": ["Corazón", "Pulmón", "Riñón", "Hígado"], "correcta": "Corazón"},
            {"pregunta": "¿Qué astro da luz a la Tierra?", "respuestas": ["Sol", "Luna", "Marte", "Saturno"], "correcta": "Sol"},
            {"pregunta": "¿Qué color es una mezcla de azul y amarillo?", "respuestas": ["Verde", "Naranja", "Rojo", "Morado"], "correcta": "Verde"},
            {"pregunta": "¿Qué tipo de animal es un perro?", "respuestas": ["Mamífero", "Ave", "Reptil", "Anfibio"], "correcta": "Mamífero"},
            {"pregunta": "¿Cómo se llama el satélite natural de la Tierra?", "respuestas": ["Luna", "Marte", "Sol", "Júpiter"], "correcta": "Luna"},
            {"pregunta": "¿Cuál es el metal más ligero?", "respuestas": ["Litio", "Plomo", "Hierro", "Oro"], "correcta": "Litio"},
        ],
        "Medio": [
            {"pregunta": "¿Qué célula transporta oxígeno en la sangre?", "respuestas": ["Glóbulo rojo", "Glóbulo blanco", "Plaqueta", "Neurona"], "correcta": "Glóbulo rojo"},
            {"pregunta": "¿Cuál es el órgano más grande del cuerpo humano?", "respuestas": ["Piel", "Hígado", "Cerebro", "Pulmón"], "correcta": "Piel"},
            {"pregunta": "¿Qué planeta tiene un gran anillo?", "respuestas": ["Saturno", "Marte", "Neptuno", "Urano"], "correcta": "Saturno"},
            {"pregunta": "¿Qué elemento tiene el símbolo O?", "respuestas": ["Oxígeno", "Oro", "Osmio", "Ozono"], "correcta": "Oxígeno"},
            {"pregunta": "¿Qué animal pone huevos?", "respuestas": ["Gallina", "Gato", "Perro", "Ballena"], "correcta": "Gallina"},
            {"pregunta": "¿Qué parte del cuerpo se examina con un otoscopio?", "respuestas": ["Oído", "Ojo", "Boca", "Nariz"], "correcta": "Oído"},
            {"pregunta": "¿Qué gas se encuentra en mayor cantidad en la atmósfera?", "respuestas": ["Nitrógeno", "Oxígeno", "CO2", "Helio"], "correcta": "Nitrógeno"},
            {"pregunta": "¿Cómo se llama el proceso de conversión de luz en energía?", "respuestas": ["Fotosíntesis", "Evaporación", "Digestión", "Condensación"], "correcta": "Fotosíntesis"},
            {"pregunta": "¿Qué órgano produce insulina?", "respuestas": ["Páncreas", "Hígado", "Estómago", "Riñón"], "correcta": "Páncreas"},
            {"pregunta": "¿Cuál es el segundo planeta del sistema solar?", "respuestas": ["Venus", "Tierra", "Marte", "Mercurio"], "correcta": "Venus"},
        ],
        "Difícil": [
            {"pregunta": "¿Qué científico formuló la teoría de la relatividad?", "respuestas": ["Einstein", "Newton", "Galileo", "Tesla"], "correcta": "Einstein"},
            {"pregunta": "¿Qué tipo de animal es una rana?", "respuestas": ["Anfibio", "Reptil", "Mamífero", "Ave"], "correcta": "Anfibio"},
            {"pregunta": "¿Cuál es el número atómico del carbono?", "respuestas": ["6", "12", "14", "8"], "correcta": "6"},
            {"pregunta": "¿Qué partícula subatómica tiene carga negativa?", "respuestas": ["Electrón", "Protón", "Neutrón", "Quark"], "correcta": "Electrón"},
            {"pregunta": "¿Qué ley explica la gravedad?", "respuestas": ["Ley de Newton", "Ley de Ohm", "Ley de Hooke", "Ley de Boyle"], "correcta": "Ley de Newton"},
            {"pregunta": "¿Qué hueso protege el cerebro?", "respuestas": ["Cráneo", "Fémur", "Costilla", "Húmero"], "correcta": "Cráneo"},
            {"pregunta": "¿Qué se mide en hercios?", "respuestas": ["Frecuencia", "Voltaje", "Corriente", "Resistencia"], "correcta": "Frecuencia"},
            {"pregunta": "¿Qué estudia la botánica?", "respuestas": ["Plantas", "Animales", "Rocas", "Estrellas"], "correcta": "Plantas"},
            {"pregunta": "¿Qué animal tiene mayor número de dientes?", "respuestas": ["Caracol", "Tiburón", "Perro", "Elefante"], "correcta": "Caracol"},
            {"pregunta": "¿Qué es el ADN?", "respuestas": ["Ácido desoxirribonucleico", "Ácido ribonucleico", "Proteína", "Hormona"], "correcta": "Ácido desoxirribonucleico"}
        ]
    },
    "Historia": {
        "Fácil": [
            {"pregunta": "¿Quién descubrió América?", "respuestas": ["Cristóbal Colón", "Américo Vespucio", "Magallanes", "Cortés"], "correcta": "Cristóbal Colón"},
            {"pregunta": "¿En qué año fue la Revolución Francesa?", "respuestas": ["1789", "1776", "1804", "1750"], "correcta": "1789"},
            {"pregunta": "¿Cuál fue la primera civilización?", "respuestas": ["Sumeria", "Egipto", "Grecia", "Roma"], "correcta": "Sumeria"},
            {"pregunta": "¿Quién fue el primer presidente de EE.UU.?", "respuestas": ["George Washington", "Lincoln", "Jefferson", "Roosevelt"], "correcta": "George Washington"},
            {"pregunta": "¿Qué pirámides están en Egipto?", "respuestas": ["Giza", "Teotihuacán", "Chichén Itzá", "Samarra"], "correcta": "Giza"},
            {"pregunta": "¿Qué imperio construyó el Coliseo?", "respuestas": ["Romano", "Griego", "Egipcio", "Persa"], "correcta": "Romano"},
            {"pregunta": "¿Quién fue Napoleón?", "respuestas": ["Un militar francés", "Un rey español", "Un filósofo griego", "Un papa"], "correcta": "Un militar francés"},
            {"pregunta": "¿En qué continente ocurrió la Segunda Guerra Mundial?", "respuestas": ["Europa", "Asia", "África", "Oceanía"], "correcta": "Europa"},
            {"pregunta": "¿Qué país usó por primera vez bombas atómicas?", "respuestas": ["Estados Unidos", "Alemania", "Rusia", "Japón"], "correcta": "Estados Unidos"},
            {"pregunta": "¿Cuál fue la capital del Imperio Azteca?", "respuestas": ["Tenochtitlan", "Texcoco", "Teotihuacán", "Tlaxcala"], "correcta": "Tenochtitlan"},
        ],
        "Medio": [
            {"pregunta": "¿Quién escribió 'El Príncipe'?", "respuestas": ["Maquiavelo", "Platón", "Aristóteles", "Rousseau"], "correcta": "Maquiavelo"},
            {"pregunta": "¿Qué evento inició la Primera Guerra Mundial?", "respuestas": ["Asesinato del Archiduque Francisco Fernando", "Invasión de Polonia", "Ataque a Pearl Harbor", "Revolución Rusa"], "correcta": "Asesinato del Archiduque Francisco Fernando"},
            {"pregunta": "¿Qué país fue liderado por Adolf Hitler?", "respuestas": ["Alemania", "Italia", "Austria", "Rusia"], "correcta": "Alemania"},
            {"pregunta": "¿Quién fue Simón Bolívar?", "respuestas": ["Libertador de América", "Rey español", "Conquistador", "Presidente de México"], "correcta": "Libertador de América"},
            {"pregunta": "¿Qué civilización construyó Machu Picchu?", "respuestas": ["Inca", "Maya", "Azteca", "Tolteca"], "correcta": "Inca"},
            {"pregunta": "¿En qué siglo cayó Constantinopla?", "respuestas": ["XV", "XIV", "XIII", "XVI"], "correcta": "XV"},
            {"pregunta": "¿Cuál fue el conflicto entre EE.UU. y la URSS?", "respuestas": ["Guerra Fría", "Primera Guerra Mundial", "Guerra Civil", "Guerra de Vietnam"], "correcta": "Guerra Fría"},
            {"pregunta": "¿Qué cultura inventó la escritura cuneiforme?", "respuestas": ["Sumerios", "Egipcios", "Griegos", "Mayas"], "correcta": "Sumerios"},
            {"pregunta": "¿Qué país fue colonia de Portugal en América?", "respuestas": ["Brasil", "Argentina", "México", "Colombia"], "correcta": "Brasil"},
            {"pregunta": "¿Quién fue Cleopatra?", "respuestas": ["Reina de Egipto", "Filósofa griega", "Emperatriz china", "Reina vikinga"], "correcta": "Reina de Egipto"},
        ],
        "Difícil": [
            {"pregunta": "¿Qué tratado terminó la Primera Guerra Mundial?", "respuestas": ["Tratado de Versalles", "Tratado de Tordesillas", "Tratado de París", "Tratado de Viena"], "correcta": "Tratado de Versalles"},
            {"pregunta": "¿Quién fue el último emperador romano?", "respuestas": ["Rómulo Augústulo", "Nerón", "Julio César", "Trajano"], "correcta": "Rómulo Augústulo"},
            {"pregunta": "¿Dónde nació Alejandro Magno?", "respuestas": ["Macedonia", "Atenas", "Esparta", "Troya"], "correcta": "Macedonia"},
            {"pregunta": "¿Qué imperio fue derrotado en la batalla de Waterloo?", "respuestas": ["Napoleónico", "Romano", "Bizantino", "Persa"], "correcta": "Napoleónico"},
            {"pregunta": "¿Qué guerra enfrentó a las rosas blanca y roja?", "respuestas": ["Guerra de las Dos Rosas", "Guerra de los Cien Años", "Guerra Civil inglesa", "Guerra de Crimea"], "correcta": "Guerra de las Dos Rosas"},
            {"pregunta": "¿Qué país construyó la Gran Armada en 1588?", "respuestas": ["España", "Francia", "Inglaterra", "Portugal"], "correcta": "España"},
            {"pregunta": "¿Qué líder fue asesinado en Dallas en 1963?", "respuestas": ["J.F. Kennedy", "Lincoln", "Roosevelt", "Reagan"], "correcta": "J.F. Kennedy"},
            {"pregunta": "¿Qué invento revolucionó la imprenta?", "respuestas": ["Prensa de Gutenberg", "Máquina de vapor", "Telégrafo", "Papel"], "correcta": "Prensa de Gutenberg"},
            {"pregunta": "¿Qué revolución derrocó al zar Nicolás II?", "respuestas": ["Revolución Rusa", "Revolución Francesa", "Revolución Industrial", "Revolución Cubana"], "correcta": "Revolución Rusa"},
            {"pregunta": "¿Cuál era el nombre original de Estambul?", "respuestas": ["Bizancio", "Atenas", "Cartago", "Jerusalén"], "correcta": "Bizancio"}
        ]
    },
    "Cultura Pop": {
        "Fácil": [
            {"pregunta": "¿Cuál es el nombre real de Spider-Man?", "respuestas": ["Peter Parker", "Clark Kent", "Bruce Wayne", "Tony Stark"], "correcta": "Peter Parker"},
            {"pregunta": "¿Qué banda lanzó el álbum 'Thriller'?", "respuestas": ["Michael Jackson", "Queen", "The Beatles", "Nirvana"], "correcta": "Michael Jackson"},
            {"pregunta": "¿Qué saga protagoniza Harry Potter?", "respuestas": ["Harry Potter", "Los Juegos del Hambre", "El Señor de los Anillos", "Crepúsculo"], "correcta": "Harry Potter"},
            {"pregunta": "¿Qué personaje es amarillo y vive en una piña?", "respuestas": ["Bob Esponja", "Minion", "Pikachu", "Homero"], "correcta": "Bob Esponja"},
            {"pregunta": "¿En qué serie aparece 'Eleven'?", "respuestas": ["Stranger Things", "The Witcher", "Dark", "Breaking Bad"], "correcta": "Stranger Things"},
            {"pregunta": "¿Qué superhéroe es conocido como el Caballero de la Noche?", "respuestas": ["Batman", "Superman", "Iron Man", "Wolverine"], "correcta": "Batman"},
            {"pregunta": "¿Qué red social usa videos cortos y virales?", "respuestas": ["TikTok", "Instagram", "Twitter", "Facebook"], "correcta": "TikTok"},
            {"pregunta": "¿Qué personaje dice 'Yo soy tu padre'?", "respuestas": ["Darth Vader", "Yoda", "Obi-Wan", "Luke"], "correcta": "Darth Vader"},
            {"pregunta": "¿Quién canta 'Shake It Off'?", "respuestas": ["Taylor Swift", "Adele", "Selena Gomez", "Billie Eilish"], "correcta": "Taylor Swift"},
            {"pregunta": "¿Qué película animada tiene un muñeco de madera?", "respuestas": ["Pinocho", "Toy Story", "Shrek", "Frozen"], "correcta": "Pinocho"}
        ],
        "Medio": [
            {"pregunta": "¿En qué año se estrenó 'Titanic'?", "respuestas": ["1997", "1995", "2000", "1999"], "correcta": "1997"},
            {"pregunta": "¿Qué artista pintó la portada del álbum 'Sgt. Pepper's Lonely Hearts Club Band'?", "respuestas": ["Peter Blake", "Andy Warhol", "Banksy", "Picasso"], "correcta": "Peter Blake"},
            {"pregunta": "¿Quién protagoniza la serie 'The Mandalorian'?", "respuestas": ["Pedro Pascal", "Oscar Isaac", "Adam Driver", "Mark Hamill"], "correcta": "Pedro Pascal"},
            {"pregunta": "¿Qué actriz interpretó a Katniss Everdeen?", "respuestas": ["Jennifer Lawrence", "Emma Watson", "Scarlett Johansson", "Natalie Portman"], "correcta": "Jennifer Lawrence"},
            {"pregunta": "¿Qué película popularizó el tema 'Let It Go'?", "respuestas": ["Frozen", "Moana", "Enredados", "Valiente"], "correcta": "Frozen"},
            {"pregunta": "¿En qué ciudad se celebra el festival de cine de Cannes?", "respuestas": ["Cannes", "París", "Venecia", "Toronto"], "correcta": "Cannes"},
            {"pregunta": "¿Qué cantante es apodada 'La Reina del Pop'?", "respuestas": ["Madonna", "Lady Gaga", "Britney Spears", "Beyoncé"], "correcta": "Madonna"},
            {"pregunta": "¿En qué serie aparece el personaje Walter White?", "respuestas": ["Breaking Bad", "Better Call Saul", "Narcos", "The Wire"], "correcta": "Breaking Bad"},
            {"pregunta": "¿Cuál es el nombre real de The Weeknd?", "respuestas": ["Abel Tesfaye", "Drake Graham", "Kendrick Duckworth", "Calvin Harris"], "correcta": "Abel Tesfaye"},
            {"pregunta": "¿Qué famoso grupo fue liderado por Freddie Mercury?", "respuestas": ["Queen", "The Rolling Stones", "The Beatles", "Aerosmith"], "correcta": "Queen"}
        ],
        "Difícil": [
            {"pregunta": "¿Qué director dirigió 'Pulp Fiction'?", "respuestas": ["Quentin Tarantino", "Martin Scorsese", "Steven Spielberg", "Christopher Nolan"], "correcta": "Quentin Tarantino"},
            {"pregunta": "¿Qué artista creó la obra 'Campbell’s Soup Cans'?", "respuestas": ["Andy Warhol", "Jean-Michel Basquiat", "Salvador Dalí", "Jackson Pollock"], "correcta": "Andy Warhol"},
            {"pregunta": "¿Cuál fue el primer video musical transmitido en MTV?", "respuestas": ["Video Killed the Radio Star", "Thriller", "Like a Virgin", "Billie Jean"], "correcta": "Video Killed the Radio Star"},
            {"pregunta": "¿Qué banda británica lanzó 'OK Computer'?", "respuestas": ["Radiohead", "Coldplay", "The Smiths", "Blur"], "correcta": "Radiohead"},
            {"pregunta": "¿En qué país se originó el K-pop?", "respuestas": ["Corea del Sur", "Japón", "China", "Tailandia"], "correcta": "Corea del Sur"},
            {"pregunta": "¿Qué película ganó el Oscar a Mejor Película en 2020?", "respuestas": ["Parasite", "1917", "Joker", "Once Upon a Time in Hollywood"], "correcta": "Parasite"},
            {"pregunta": "¿Qué serie tiene el episodio 'Ozymandias'?", "respuestas": ["Breaking Bad", "Game of Thrones", "The Sopranos", "House of Cards"], "correcta": "Breaking Bad"},
            {"pregunta": "¿Qué actor interpreta a 'Neo' en Matrix?", "respuestas": ["Keanu Reeves", "Johnny Depp", "Brad Pitt", "Tom Cruise"], "correcta": "Keanu Reeves"},
            {"pregunta": "¿Qué película introdujo el término 'inception'?", "respuestas": ["El Origen", "Interstellar", "Memento", "Tenet"], "correcta": "El Origen"},
            {"pregunta": "¿Qué serie popular está basada en libros de George R. R. Martin?", "respuestas": ["Game of Thrones", "The Witcher", "The Expanse", "The Wheel of Time"], "correcta": "Game of Thrones"}
        ]
    },
    "Videojuegos": {
        "Fácil": [
            {"pregunta": "¿Cuál fue la primera consola de Nintendo?", "respuestas": ["NES", "SNES", "GameCube", "Wii"], "correcta": "NES"},
            {"pregunta": "¿Qué personaje recolecta anillos dorados?", "respuestas": ["Sonic", "Mario", "Link", "Pikachu"], "correcta": "Sonic"},
            {"pregunta": "¿En qué juego aparece el personaje de Mario?", "respuestas": ["Super Mario Bros", "Halo", "Zelda", "Minecraft"], "correcta": "Super Mario Bros"},
            {"pregunta": "¿Qué criatura debes atrapar en Pokémon?", "respuestas": ["Pokémon", "Monstruos", "Dragones", "Aliens"], "correcta": "Pokémon"},
            {"pregunta": "¿Qué consola es de Sony?", "respuestas": ["PlayStation", "Xbox", "Switch", "Wii U"], "correcta": "PlayStation"},
            {"pregunta": "¿Qué videojuego tiene creepers?", "respuestas": ["Minecraft", "Fortnite", "Roblox", "Among Us"], "correcta": "Minecraft"},
            {"pregunta": "¿Qué color es el sombrero de Mario?", "respuestas": ["Rojo", "Verde", "Azul", "Amarillo"], "correcta": "Rojo"},
            {"pregunta": "¿En qué juego puedes construir con bloques?", "respuestas": ["Minecraft", "Tetris", "FIFA", "Valorant"], "correcta": "Minecraft"},
            {"pregunta": "¿Qué animal es Sonic?", "respuestas": ["Erizo", "Ratón", "Zorro", "Gato"], "correcta": "Erizo"},
            {"pregunta": "¿Qué consola pertenece a Microsoft?", "respuestas": ["Xbox", "PlayStation", "Switch", "GameCube"], "correcta": "Xbox"}
        ],
        "Medio": [
            {"pregunta": "¿Quién es el protagonista de 'The Legend of Zelda'?", "respuestas": ["Link", "Zelda", "Ganon", "Navi"], "correcta": "Link"},
            {"pregunta": "¿Qué juego popular fue desarrollado por Epic Games?", "respuestas": ["Fortnite", "Call of Duty", "Overwatch", "PUBG"], "correcta": "Fortnite"},
            {"pregunta": "¿Qué género es 'League of Legends'?", "respuestas": ["MOBA", "RPG", "FPS", "Survival"], "correcta": "MOBA"},
            {"pregunta": "¿Qué juego tiene como objetivo escapar de una nave con impostores?", "respuestas": ["Among Us", "Subnautica", "Dead Space", "Outer Wilds"], "correcta": "Among Us"},
            {"pregunta": "¿Cuál es el nombre del fontanero hermano de Mario?", "respuestas": ["Luigi", "Wario", "Toad", "Yoshi"], "correcta": "Luigi"},
            {"pregunta": "¿Qué entrega de GTA se sitúa en Los Santos?", "respuestas": ["GTA V", "GTA IV", "GTA III", "GTA: Vice City"], "correcta": "GTA V"},
            {"pregunta": "¿Quién es el creador de Metal Gear?", "respuestas": ["Hideo Kojima", "Shigeru Miyamoto", "Gabe Newell", "Todd Howard"], "correcta": "Hideo Kojima"},
            {"pregunta": "¿Qué juego tiene una skin de banana llamada 'Peely'?", "respuestas": ["Fortnite", "Fall Guys", "Minecraft", "Roblox"], "correcta": "Fortnite"},
            {"pregunta": "¿Qué personaje dice '¡It's-a me, Mario!'?", "respuestas": ["Mario", "Luigi", "Toad", "Wario"], "correcta": "Mario"},
            {"pregunta": "¿Qué videojuego de puzzles fue creado en la Unión Soviética?", "respuestas": ["Tetris", "Portal", "Puyo Puyo", "Zuma"], "correcta": "Tetris"}
        ],
        "Difícil": [
            {"pregunta": "¿Qué juego es famoso por su dificultad y lema 'Prepare to die'?", "respuestas": ["Dark Souls", "Doom", "Bloodborne", "Sekiro"], "correcta": "Dark Souls"},
            {"pregunta": "¿Cuál fue el primer videojuego comercial?", "respuestas": ["Pong", "Space Invaders", "Pac-Man", "Donkey Kong"], "correcta": "Pong"},
            {"pregunta": "¿Qué empresa desarrolló el juego 'The Witcher'?", "respuestas": ["CD Projekt Red", "Ubisoft", "Bethesda", "BioWare"], "correcta": "CD Projekt Red"},
            {"pregunta": "¿Qué juego presenta un mundo postapocalíptico con máquinas animales?", "respuestas": ["Horizon Zero Dawn", "Fallout", "Metro", "Days Gone"], "correcta": "Horizon Zero Dawn"},
            {"pregunta": "¿Qué consola portátil introdujo los cartuchos intercambiables?", "respuestas": ["Game Boy", "Game Gear", "PSP", "Neo Geo Pocket"], "correcta": "Game Boy"},
            {"pregunta": "¿En qué juego aparece el personaje Geralt de Rivia?", "respuestas": ["The Witcher", "Elden Ring", "Skyrim", "Dragon Age"], "correcta": "The Witcher"},
            {"pregunta": "¿Qué estudio creó 'Half-Life'?", "respuestas": ["Valve", "id Software", "Rockstar", "Epic Games"], "correcta": "Valve"},
            {"pregunta": "¿Qué juego introdujo el modo Battle Royale primero?", "respuestas": ["PUBG", "Fortnite", "Warzone", "Apex Legends"], "correcta": "PUBG"},
            {"pregunta": "¿Qué juego usa el CryEngine?", "respuestas": ["Crysis", "Doom", "Far Cry 6", "Stalker"], "correcta": "Crysis"},
            {"pregunta": "¿Qué personaje aparece en todos los juegos de Super Smash Bros.?", "respuestas": ["Mario", "Pikachu", "Samus", "Kirby"], "correcta": "Mario"}
        ]
    }
}
# ---------------------------------------------------

seleccion_categoria = "Ciencia"
nivel_dificultad = "Fácil"
modo_preguntas_ia = False

def generar_pregunta_ia():
    operaciones = [
        ("+", lambda a, b: a + b),
        ("-", lambda a, b: a - b),
        ("×", lambda a, b: a * b),
        ("/", lambda a, b: round(a / b, 2) if b != 0 else 0)
    ]
    op, func = random.choice(operaciones)
    a = random.randint(2, 50)
    b = random.randint(2, 50) if op != "/" else random.randint(2, 12)
    correcta = func(a, b)
    pregunta = f"¿Cuánto es {a} {op} {b}?"
    incorrectas = set()
    while len(incorrectas) < 3:
        delta = random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
        propuesta = correcta + delta if op != "/" else round(correcta + delta, 2)
        if propuesta != correcta:
            incorrectas.add(propuesta)
    opciones = list(incorrectas) + [correcta]
    random.shuffle(opciones)
    return {
        "pregunta": pregunta,
        "respuestas": [str(o) for o in opciones],
        "correcta": str(correcta)
    }

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Label(text='TRIVIA EXTREME', font_size='32sp', size_hint_y=0.2))
        btn_jugar = Button(text='Jugar', font_size='24sp', background_color=(0, 0.5, 1, 1))
        btn_jugar.bind(on_press=self.iniciar_juego)
        layout.add_widget(btn_jugar)
        self.btn_categoria = Button(text='Categoría: ' + seleccion_categoria, font_size='20sp')
        self.btn_categoria.bind(on_press=self.seleccionar_categoria)
        layout.add_widget(self.btn_categoria)
        self.btn_nivel = Button(text='Nivel: ' + nivel_dificultad, font_size='20sp')
        self.btn_nivel.bind(on_press=self.seleccionar_nivel)
        layout.add_widget(self.btn_nivel)
        self.btn_modo_ia = Button(text='Modo Preguntas: Fijas', font_size='20sp')
        self.btn_modo_ia.bind(on_press=self.cambiar_modo_ia)
        layout.add_widget(self.btn_modo_ia)
        self.add_widget(layout)

    def iniciar_juego(self, instance):
        juego = self.manager.get_screen('juego')
        juego.nueva_partida()
        self.manager.current = 'juego'

    def seleccionar_categoria(self, instance):
        global seleccion_categoria
        categorias = list(preguntas.keys())
        idx = (categorias.index(seleccion_categoria) + 1) % len(categorias)
        seleccion_categoria = categorias[idx]
        self.btn_categoria.text = 'Categoría: ' + seleccion_categoria

    def seleccionar_nivel(self, instance):
        global nivel_dificultad
        niveles = ['Fácil', 'Medio', 'Difícil']
        idx = (niveles.index(nivel_dificultad) + 1) % len(niveles)
        nivel_dificultad = niveles[idx]
        self.btn_nivel.text = 'Nivel: ' + nivel_dificultad

    def cambiar_modo_ia(self, instance):
        global modo_preguntas_ia
        modo_preguntas_ia = not modo_preguntas_ia
        if modo_preguntas_ia:
            self.btn_modo_ia.text = "Modo Preguntas: IA"
        else:
            self.btn_modo_ia.text = "Modo Preguntas: Fijas"

class JuegoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=15)
        self.label_pregunta = Label(text='', font_size='22sp', size_hint_y=0.2)
        self.layout.add_widget(self.label_pregunta)
        self.timer_label = Label(text='', font_size='18sp', size_hint_y=0.1)
        self.layout.add_widget(self.timer_label)
        self.respuestas_jugadores = []
        self.botones_respuestas = []
        for jugador in range(NUM_JUGADORES):
            jugador_box = BoxLayout(orientation='horizontal', spacing=5, size_hint_y=0.18)
            jugador_label = Label(text=f'Jugador {jugador+1}', font_size='16sp', size_hint_x=0.25)
            jugador_box.add_widget(jugador_label)
            botones = []
            for i in range(4):
                btn = Button(font_size='16sp', size_hint_x=0.18)
                btn.bind(on_press=self.verificar_respuesta)
                jugador_box.add_widget(btn)
                botones.append(btn)
            self.botones_respuestas.append(botones)
            self.layout.add_widget(jugador_box)
        self.add_widget(self.layout)
        self.reset_estado()

    def reset_estado(self):
        self.tiempo_restante = 10
        self.pregunta_actual = None
        self.preguntas_partida = []
        self.indice_pregunta = 0
        self.puntuaciones = [0 for _ in range(NUM_JUGADORES)]
        self.respuestas_jugadores = [None for _ in range(NUM_JUGADORES)]
        self.respuestas_procesadas = False

    def nueva_partida(self):
        self.reset_estado()
        if not modo_preguntas_ia:
            preguntas_categoria = list(preguntas[seleccion_categoria][nivel_dificultad])
            random.shuffle(preguntas_categoria)
            self.preguntas_partida = preguntas_categoria[:NUM_PREGUNTAS_PARTIDA]
        else:
            self.preguntas_partida = [None]*NUM_PREGUNTAS_PARTIDA
        self.indice_pregunta = 0
        self.cargar_pregunta()

    def cargar_pregunta(self):
        if self.indice_pregunta >= NUM_PREGUNTAS_PARTIDA:
            self.manager.get_screen('final').mostrar(self.puntuaciones)
            self.manager.current = 'final'
            return
        if modo_preguntas_ia:
            self.pregunta_actual = generar_pregunta_ia()
        else:
            self.pregunta_actual = self.preguntas_partida[self.indice_pregunta]
        self.label_pregunta.text = self.pregunta_actual['pregunta']
        self.respuestas_jugadores = [None for _ in range(NUM_JUGADORES)]
        self.respuestas_procesadas = False
        respuestas = list(self.pregunta_actual['respuestas'])
        random.shuffle(respuestas)
        for jugador in range(NUM_JUGADORES):
            for i, btn in enumerate(self.botones_respuestas[jugador]):
                btn.text = respuestas[i]
                btn.background_color = (1, 1, 1, 1)
                btn.disabled = False
        self.tiempo_restante = {"Fácil": 15, "Medio": 10, "Difícil": 5}[nivel_dificultad]
        self.timer_label.text = f"Tiempo: {self.tiempo_restante}s"
        Clock.unschedule(self.actualizar_timer)
        Clock.schedule_interval(self.actualizar_timer, 1)

    def actualizar_timer(self, dt):
        self.tiempo_restante -= 1
        if self.tiempo_restante <= 0:
            Clock.unschedule(self.actualizar_timer)
            self.procesar_respuestas()
        else:
            self.timer_label.text = f"Tiempo: {self.tiempo_restante}s"

    def verificar_respuesta(self, instance):
        for jugador, botones in enumerate(self.botones_respuestas):
            if instance in botones and self.respuestas_jugadores[jugador] is None:
                self.respuestas_jugadores[jugador] = instance.text
                if instance.text == self.pregunta_actual['correcta']:
                    instance.background_color = (0.2, 0.85, 0.2, 1)
                else:
                    instance.background_color = (0.95, 0.2, 0.2, 1)
                for btn in botones:
                    btn.disabled = True
                break
        if all(r is not None for r in self.respuestas_jugadores) and not self.respuestas_procesadas:
            Clock.unschedule(self.actualizar_timer)
            self.procesar_respuestas()

    def procesar_respuestas(self):
        self.respuestas_procesadas = True
        correcta = self.pregunta_actual['correcta']
        for jugador, respuesta in enumerate(self.respuestas_jugadores):
            if respuesta == correcta:
                self.puntuaciones[jugador] += 1
        for jugador, botones in enumerate(self.botones_respuestas):
            for btn in botones:
                if btn.text == correcta:
                    btn.background_color = (0.2, 0.85, 0.2, 1)
        Clock.schedule_once(lambda dt: self.mostrar_resultado(), 1.3)

    def mostrar_resultado(self):
        resultado = self.manager.get_screen('resultado')
        resultado.mostrar(self.pregunta_actual['pregunta'],
                          self.pregunta_actual['correcta'],
                          list(self.respuestas_jugadores),
                          list(self.puntuaciones))
        self.indice_pregunta += 1
        self.manager.current = 'resultado'

class ResultadoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.label_pregunta = Label(text='', font_size='18sp')
        self.labels_jugadores = [Label(text='', font_size='16sp') for _ in range(NUM_JUGADORES)]
        self.label_puntuaciones = Label(text='', font_size='16sp')
        self.layout.add_widget(self.label_pregunta)
        for label in self.labels_jugadores:
            self.layout.add_widget(label)
        self.layout.add_widget(self.label_puntuaciones)
        self.add_widget(self.layout)

    def mostrar(self, pregunta, correcta, respuestas, puntuaciones):
        self.label_pregunta.text = f"Pregunta: {pregunta}"
        for i in range(NUM_JUGADORES):
            if respuestas[i] is None:
                txt = f"Jugador {i+1}: Sin respuesta"
            elif respuestas[i] == correcta:
                txt = f"Jugador {i+1}: ✔️ '{respuestas[i]}'"
            else:
                txt = f"Jugador {i+1}: ❌ '{respuestas[i]}'"
            self.labels_jugadores[i].text = txt
        self.label_puntuaciones.text = "Puntuaciones: " + " | ".join([f"J{i+1}: {p}" for i, p in enumerate(puntuaciones)])
        Clock.schedule_once(self.continuar, 3.5)

    def continuar(self, dt):
        juego = self.manager.get_screen('juego')
        juego.cargar_pregunta()
        self.manager.current = 'juego'

class FinalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.label_final = Label(text='', font_size='24sp')
        self.label_detalle = Label(text='', font_size='18sp')
        self.btn_menu = Button(text='Volver al Menú', font_size='20sp', background_color=(0, 0.5, 1, 1))
        self.btn_menu.bind(on_press=self.volver_menu)
        self.layout.add_widget(self.label_final)
        self.layout.add_widget(self.label_detalle)
        self.layout.add_widget(self.btn_menu)
        self.add_widget(self.layout)

    def mostrar(self, puntuaciones):
        max_puntos = max(puntuaciones)
        ganadores = [i+1 for i, p in enumerate(puntuaciones) if p == max_puntos]
        if len(ganadores) == 1:
            self.label_final.text = f"¡Ganador: Jugador {ganadores[0]}!"
        else:
            self.label_final.text = "¡Empate!"
        self.label_detalle.text = "Puntuaciones finales:\n" + "\n".join([f"Jugador {i+1}: {p}" for i, p in enumerate(puntuaciones)])

    def volver_menu(self, instance):
        self.manager.current = 'menu'

class TriviaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(JuegoScreen(name='juego'))
        sm.add_widget(ResultadoScreen(name='resultado'))
        sm.add_widget(FinalScreen(name='final'))
        return sm

if __name__ == '__main__':
    TriviaApp().run()