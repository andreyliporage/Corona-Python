class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.viruses_left = self.ai_settings.virus_limit
