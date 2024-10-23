
from pyspark.sql import DataFrame, SparkSession
from beyond_bets.base.transform import Transform
from beyond_bets.datasets.bets import Bets
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

class PlayerMarketDaily(Transform):
    def __init__(self):
        super().__init__()
        self._name: str = "PlayerMarketDaily"
        self._inputs = {"bets": Bets()}

    def _transformation(self, **kwargs: dict[str, any]) -> DataFrame:
        return (
            self.bets
            .groupBy(
                F.col("player_id"),
                F.col("market_id"),
                F.window(F.col("bet_timestamp"), "1 day").alias("day_window")
            )
            .agg(
                F.sum("bet_amount").alias("total_bets"),
                F.count("bet_id").alias("num_bets")
            )
            .select(
                F.col("player_id"),
                F.col("market_id"),
                F.col("day_window.start").alias("day_start"),
                F.col("day_window.end").alias("day_end"),
                F.col("total_bets"),
                F.col("num_bets")
            )
        )
