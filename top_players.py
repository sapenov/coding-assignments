
from pyspark.sql import DataFrame, SparkSession
from beyond_bets.base.transform import Transform
from beyond_bets.datasets.bets import Bets
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

class TopPlayers(Transform):
    def __init__(self):
        super().__init__()
        self._name: str = "TopPlayers"
        self._inputs = {"bets": Bets()}

    def _transformation(self, **kwargs: dict[str, any]) -> DataFrame:
        one_week_ago = F.current_timestamp() - F.expr('INTERVAL 1 WEEK')
        
        total_spend_per_player = (
            self.bets
            .filter(F.col("bet_timestamp") >= one_week_ago)
            .groupBy("player_id")
            .agg(F.sum("bet_amount").alias("total_spend"))
        )

        total_players = total_spend_per_player.count()
        top_percent = int(total_players * 0.01)

        return total_spend_per_player.orderBy(F.col("total_spend").desc()).limit(top_percent)
