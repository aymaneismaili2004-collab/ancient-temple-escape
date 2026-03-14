rooms = {
    "Entrance": {
        "south": "Dark Chamber",
        "east": "Sacred Room",
        "item": "ancient_relic"
    },

    "Dark Chamber": {
        "north": "Entrance",
        "south": "Shadow Corridor",
        "enemy": {
            "name": "Temple Guardian",
            "health": 30,
            "attack": 10
        }
    },

    "Sacred Room": {
        "west": "Entrance",
        "south": "Exit Gate",
        "item": "healing_scroll"
    },

    "Shadow Corridor": {
        "north": "Dark Chamber",
        "east": "Treasure Room",
        "enemy": {
            "name": "Cursed Warrior",
            "health": 40,
            "attack": 12
        }
    },

    "Treasure Room": {
        "west": "Shadow Corridor",
        "item": "golden_idol",
        "chest": "closed"
    },

    "Exit Gate": {
        "north": "Sacred Room",
        "enemy": {
            "name": "Temple Overseer",
            "health": 50,
            "attack": 14
        }
    }
}