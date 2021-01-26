import presentation
from categorizer import categorize_by_countries
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

    def explore_popularity_of_the_app_across_countries(self):
        population, country = categorize_by_countries()
        presentation.tell_story_about_popularity_of_app_comparing_countries(population[:10], country[:10])#([100,56,33],['US','USD','UKR']))

    def explore_lifetime_value_in_united_states(self):
        us_ltv = CustomerLifetimeValue("bycountries/US.csv")
        id_ltv = CustomerLifetimeValue("bycountries/ID.csv")
        presentation.tell_story_about_lifetimevalue_comparing_countries(
            [us_ltv.compute_lifetime_value(), id_ltv.compute_lifetime_value()], ['US', 'ID'])
