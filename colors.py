class Colors:
    charcoal = (26, 31, 40)
    green = (13, 146, 65)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (229, 207, 0 )
    purple = (110, 0, 160)
    cyan = (3, 123, 109)
    blue = (13, 27, 146)

    @classmethod
    def cell_colors(cls):
        return [cls.charcoal, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
