from torch import nn

from dot.models.shelf.cotracker2_utils.predictor import CoTrackerPredictor


class CoTracker2(nn.Module):
    def __init__(self, args):
        super().__init__()
        self.model = CoTrackerPredictor(args.patch_size, args.wind_size)

    def forward(self, video, queries, backward_tracking, cache_features=False):
        return self.model(video, queries=queries, backward_tracking=backward_tracking, cache_features=cache_features)


