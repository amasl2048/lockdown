DEBUG = False

PLAYERS = ("HACKER", "BIOLOGIST")
INTRUDERS = ("LARVA", "CREEPER", "ADULT", "BREEDER", "QUEEN")
EFFECTS = ("SILENCE", "DANGER", "SLIME", "FIRE", "MALFUNCTION", "DOOR")

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

NOISE_DICE = ("1", "1", "2", "2", "3", "3", "4", "4", "SILENCE", "DANGER")

INTRUDERS_TOKENS = 4*["LARVA"] + ["CREEPER"] + 3*["ADULT"] + ["QUEEN"] + ["-"]
