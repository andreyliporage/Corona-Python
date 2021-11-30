class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        self.doctor_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 255
        self.bullets_allowed = 3
        self.virus_speed_factor = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.virus_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.doctor_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.virus_speed_factor = 1
        self.fleet_direction = 1
        self.virus_points = 50

    def increase_speed(self):
        self.doctor_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.virus_speed_factor *= self.speedup_scale
        self.virus_points = int(self.virus_points * self.score_scale)
