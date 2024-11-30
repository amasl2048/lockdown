DEBUG = True

PLAYERS = 2
START_ROOM = "17"

INTRUDERS = ("LARVA", "CREEPER", "ADULT", "BREEDER", "QUEEN")
START_INTRUDERS_TOKENS = ["-"] + 4*["LARVA"] + ["CREEPER"] + 3*["ADULT"] + ["QUEEN"]  # 10 tokens
TOTAL_INTRUDERS_TOKENS = 8*["LARVA"] + 3*["CREEPER"] + 12*["ADULT"] + 2*["BREEDER"] + ["QUEEN"] + ["-"]  # 27 tokens
INTRUDERS_TOKENS_NUMBERS = [1, 1, 2, 2, 3, 4] 

ENDURANCE = 2*["-"] + 2*["2"] + 4*["3"] + 5*["4"] + 5*["5"] + 2*["6"]  # 20 cards
INTRUDER_ATTACKS = 4*["BITE"] + ["SLIME"] + 4*["CLAW"] + \
                   2*["TRANSFORMATION"] + 4*["SCRATCH"] + \
                   2*["TAIL"] + 2*["FRENZY"] + ["SUMMONING"]  # 20 cards

ATTACK = {
    "BITE": ["ADULT", "BREEDER", "QUEEN"],
    "SLIME": ["CREEPER", "ADULT", "BREEDER", "QUEEN"],
    "CLAW": ["ADULT", "BREEDER", "QUEEN"],
    "TRANSFORMATION": ["CREEPER"],
    "SCRATCH": ["CREEPER", "ADULT", "BREEDER", "QUEEN"],
    "TAIL": ["QUEEN"],
    "FRENZY": ["BREEDER", "QUEEN"],
    "SUMMONING": ["CREEPER", "QUEEN"]
}

EGGS_TOKENS = 8
START_EGGS = 5

COORDINATES = ["EARTH", "MARS", "VENUS", "DEEP SPACE"]

BASIC_ACTIONS_NOT_COMBAT = {
    "MOVEMENT": 1,
    "CAREFUL MOVEMENT": 2,
    "PICK UP HEAVY OBJECT": 1,
    "TRADE": 1,
    "CRAFT ITEM": 1
}
BASIC_ACTIONS_ANY = {
    "SHOOT": 1,
    "MELEE ATTACK": 1
}

NOISE_DIE = ("1", "1", "2", "2", "3", "3", "4", "4", "SILENCE", "DANGER")
COMBAT_DIE = ("-", "+", "++", "CREEPER","CREEPER", "ADULT")

FIRE_MARKERS = 8
MALFUNCTION_MARKERS = 8

CHARACTERS = ("CAPITAN", "PILOT", "SCIENTIST", "SCOUT", "SOLDIER", "MECHANIC")

EFFECTS = ("SILENCE", "DANGER", "SLIME", "FIRE", "MALFUNCTION", "DOOR")

CONTAMINATION_CARDS = 27
ESCAPE_POD_1_2 = 2
ESCAPE_POD_3_4 = 3
ESCAPE_POD_5 = 4

TIME_TRACK = 15


# FIXME
SECTIONS = ((1, 2, 17, 21),  # S1
            (3, 4, 5, 6, 7, 8, 9, 18, 22),  # S2
            (10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 23)  #S3
)

TOTAL_ROOMS = 23

ROOMS_I = (
    "Archive",
    "Cave Entrance",
    "Cooling System",
    "Decon Room",
    "Emergency Room",
    "Laboratory",
    "Cargo A", 
    "Nest",
    "Power Generator",
    "Transmitter Control"
)

ROOMS_II = (
    "Cargo B",
    "Cargo C",
    "CSS Control",
    "Defense Control",
    "Guard Control",
    "Contaminated Room",
    "Surgery Room",
    "Testing Lab",
    "Vent Control"
)

SPECIAL_ROOMS = ("Alert Room",
                 "Backup Power Supply",
                 "Elevator Room S-01",
                 "Elevator Room S-02",
                 "Elevator Room S-03",
                 "Emergency Staircases",
                 "Repository",
                 "Isolation Room")
