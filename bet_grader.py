
from pyspark.sql import DataFrame, SparkSession
from beyond_bets.base.transform import Transform
from beyond_bets.datasets.bets import Bets
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

class BetGrader(Transform):
    def __init__(self):
        super().__init__()
        self._name: str = "BetGrader"
        self._inputs = {"bets": Bets()}

    def _transformation(self, **kwargs: dict[str, any]) -> DataFrame:
        fifteen_minutes_ago = F.current_timestamp() - F.expr('INTERVAL 15 MINUTES')

        market_avg_bets = (
            self.bets
            .filter(F.col("bet_timestamp") >= fifteen_minutes_ago)
            .groupBy("market_id")
            .agg(F.avg("bet_amount").alias("avg_bet_amount"))
        )

        graded_bets = (
            self.bets
            .join(market_avg_bets, "market_id")
            .withColumn("bet_grade", F.col("bet_amount") / F.col("avg_bet_amount"))
            .select("bet_id", "market_id", "bet_amount", "avg_bet_amount", "bet_grade")
        )

        return graded_bets
