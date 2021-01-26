import presentation

class GraphStory():
    def __init__(self, retention):
        self.retention = retention

    def explore_retention_of_users(self):
        response_model = self.retention.compute_classical_retention()
        presentation.tell_story_about_classical_retention_rate_as_line(response_model)

