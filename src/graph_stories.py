import presentation
from ltv_entity import CustomerLifetimeValue


class GraphStory():
    def __init__(self, entity: CustomerLifetimeValue):
        self.entity = entity

    def explore_total_lifetime_value(self):
        response_model = self.entity.compute_lifetime_value()
        presentation.tell_story_about_total_lifetimevalue(response_model)

    def explore_retention_of_users(self):
        response_model = self.entity.compute_classical_retention()
        presentation.tell_story_about_classical_retention_rate_as_line(response_model)

    def explore_lifetime_value_across_devices(self):
        iPad_ltv = CustomerLifetimeValue("iPad.csv")
        iPhone_ltv = CustomerLifetimeValue("iPhone.csv")
        presentation.tell_story_about_lifetimevalue_comparing_devices(iPhone_ltv.compute_lifetime_value(), iPad_ltv.compute_lifetime_value())

    def explore_lifetime_value_across_countries(self):
        iPad_ltv = CustomerLifetimeValue("iPad.csv")
        iPhone_ltv = CustomerLifetimeValue("iPhone.csv")
        presentation.tell_story_about_lifetimevalue_comparing_countries(([100,56,33],['US','USD','UKR']))
