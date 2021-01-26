from graph_stories import GraphStory

class LTVComputeRetentionDummy():
    def compute_classical_retention(self):
        return [1234, 234, 100, 42, 6, 4]

def test_construction():
    user_story = GraphStory(LTVComputeRetentionDummy())
    user_story.explore_retention_of_users()