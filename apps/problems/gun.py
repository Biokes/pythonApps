class Gun:
    bullets = 0

    def __init__(self):
        self.bullets = 0

    def count_bullet(self):
        return self.bullets

    def reload(self):
        self.bullets += 10
        pass

    def shoot(self):
        if self.bullets == 0:
            return "no bullet currently."
        self.bullets -= 1
        pass
