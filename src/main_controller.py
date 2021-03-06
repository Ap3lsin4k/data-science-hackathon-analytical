import ltv_entity
from graph_stories import GraphStory

story = GraphStory(ltv_entity.CustomerLifetimeValue("data_analytics.csv"))

story.explore_total_lifetime_value()
story.explore_retention_of_users()
story.explore_lifetime_value_across_devices()
story.explore_popularity_of_the_app_across_countries()
story.explore_lifetime_value_in_united_states()
