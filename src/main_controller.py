import ltv_entity
from graph_stories import GraphStory

story = GraphStory(ltv_entity.CustomerLifetimeValue("data_analytics.csv"))

story.explore_retention_of_users()
