class Player:
    def __init__(self):
        self.name = "Leo"
        # Real world stats
        self.max_energy = 100
        self.energy = 100
        self.burnout = 0  # Increases if quests fail
        
        # Affinities
        self.affinity = {
            "Sara": 0,
            "Diego": 0,
            "Elena": 0,
            "Camila": 0,
            "Marcos": 0
        }
        
        # JRPG Stats
        self.hp = 100
        self.max_hp = 100
        self.attack = 15
        self.defense = 10
        self.party = []
        
        # Story progression
        self.cozy_route = False
        self.day = 1

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def take_damage(self, amount):
        damage = max(1, amount - (self.defense // 2))
        self.hp = max(0, self.hp - damage)
        return damage

    def modify_energy(self, amount):
        self.energy = max(0, min(self.max_energy, self.energy + amount))
        
    def increase_burnout(self, amount):
        self.burnout += amount
        self.max_energy = max(20, self.max_energy - (amount * 10))
        self.energy = min(self.energy, self.max_energy)
