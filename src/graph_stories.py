import presentation
from ltv_entity import CustomerLifetimeValue


class GraphStory():
    def __init__(self, entity: CustomerLifetimeValue):
        self.entity = entity

    def explore_retention_of_users(self):
        response_model = self.entity.compute_classical_retention()
        presentation.tell_story_about_classical_retention_rate_as_line(response_model)

    def explore_total_lifetime_value(self):
        response_model = self.entity.compute_lifetime_value()
        presentation.tell_story_about_total_lifetime_value_as_one_bar(response_model)
