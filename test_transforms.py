
import pytest
from pyspark.sql import SparkSession
from beyond_bets.transforms.player_hourly import PlayerHourly
from beyond_bets.transforms.market_daily import MarketDaily
from beyond_bets.transforms.player_market_daily import PlayerMarketDaily
from beyond_bets.transforms.top_players import TopPlayers
from beyond_bets.transforms.bet_grader import BetGrader
from pyspark.sql import functions as F

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").appName("beyond_bets_tests").getOrCreate()

@pytest.fixture
def bets_df(spark):
    data = [
        {"player_id": 1, "market_id": 101, "bet_id": "b1", "bet_timestamp": "2024-10-01 10:00:00", "bet_amount": 100},
        {"player_id": 1, "market_id": 101, "bet_id": "b2", "bet_timestamp": "2024-10-01 10:15:00", "bet_amount": 200},
        {"player_id": 2, "market_id": 102, "bet_id": "b3", "bet_timestamp": "2024-10-01 11:00:00", "bet_amount": 150},
        {"player_id": 2, "market_id": 102, "bet_id": "b4", "bet_timestamp": "2024-10-02 10:00:00", "bet_amount": 300},
        {"player_id": 3, "market_id": 103, "bet_id": "b5", "bet_timestamp": "2024-10-02 10:15:00", "bet_amount": 400}
    ]
    return spark.createDataFrame(data)

def test_player_hourly(spark, bets_df):
    transform = PlayerHourly()
    result_df = transform._transformation(bets=bets_df)
    assert result_df.count() == 3  # 3 hourly aggregations expected

def test_market_daily(spark, bets_df):
    transform = MarketDaily()
    result_df = transform._transformation(bets=bets_df)
    assert result_df.count() == 3  # 3 daily aggregations expected

def test_player_market_daily(spark, bets_df):
    transform = PlayerMarketDaily()
    result_df = transform._transformation(bets=bets_df)
    assert result_df.count() == 4  # 4 player-market daily aggregations expected

def test_top_players(spark, bets_df):
    transform = TopPlayers()
    result_df = transform._transformation(bets=bets_df)
    assert result_df.count() == 1  # Top 1% of 3 players (rounded) is 1 player

def test_bet_grader(spark, bets_df):
    transform = BetGrader()
    result_df = transform._transformation(bets=bets_df)
    assert "bet_grade" in result_df.columns  # Ensure bet_grade column exists
