

class enemy:
    def __init__(self, x, y, type, attack_status, health, target, target_dir):
        self.x = x
        self.y = y
        self.type = type
        self.attack_status = attack_status
        self.health = health
        self.target = target
        self.target_dir = target_dir
