class Settings:
    """A class to store all settings for alien invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 3

        # Bullets settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings(None)

    def initialize_dynamic_settings(self, level):
        """Initialize settings that change throughout the game."""

        self.level = level

        if self.level == 1:
            self.ship_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 1.0
        elif self.level == 2:
            self.ship_speed = 3.0
            self.bullet_speed = 6.0
            self.alien_speed = 2.0
        elif self.level == 3:
            self.ship_speed = 4.5
            self.bullet_speed = 9.0
            self.alien_speed = 3.0

        # fleet_direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
