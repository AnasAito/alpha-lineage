import pandas as pd

from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
#Create Schema
from pyspark.sql.types import StructType,StructField, StringType,ArrayType
def _is_true(x: pd.Series) -> pd.Series:
    return x == "t"


def _parse_percentage(x: pd.Series) -> pd.Series:
    x = x.str.replace("%", "")
    x = x.astype(float) / 100
    return x


def _parse_money(x: pd.Series) -> pd.Series:
    x = x.str.replace("$", "").str.replace(",", "")
    x = x.astype(float)
    return x


def preprocess_companies(companies: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for companies.

    Args:
        companies: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """
    companies["iata_approved"] = _is_true(companies["iata_approved"])
    companies["company_rating"] = _parse_percentage(companies["company_rating"])
    return companies


def preprocess_shuttles(shuttles: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for shuttles.

    Args:
        shuttles: Raw data.
    Returns:
        Preprocessed data, with `price` converted to a float and `d_check_complete`,
        `moon_clearance_complete` converted to boolean.
    """
    shuttles["d_check_complete"] = _is_true(shuttles["d_check_complete"])
    shuttles["moon_clearance_complete"] = _is_true(shuttles["moon_clearance_complete"])
    shuttles["price"] = _parse_money(shuttles["price"])
    return shuttles


def create_model_input_table(
    shuttles: pd.DataFrame, companies: pd.DataFrame, reviews: pd.DataFrame
) -> pd.DataFrame:
    """Combines all data to create a model input table.

    Args:
        shuttles: Preprocessed data for shuttles.
        companies: Preprocessed data for companies.
        reviews: Raw data for reviews.
    Returns:
        Model input table.

    """
    rated_shuttles = shuttles.merge(reviews, left_on="id", right_on="shuttle_id")
    model_input_table = rated_shuttles.merge(
        companies, left_on="company_id", right_on="id"
    )
    model_input_table = model_input_table.dropna()
    return model_input_table


def crunchbase_preprocessing(
    crunchbase_organizations: DataFrame,
    crunchbase_topic_association: DataFrame
) -> DataFrame:
    """Step 1 : Combines features from direct links to orgs (crunchbase_topic_association) 
    or with native features (like name and url)
       Step 2 : Preprocess all features 
       job_path : https://adb-6726284766671799.19.azuredatabricks.net/
                  ?o=6726284766671799#notebook/2552593661288685

    Args:
        crunchbase_organizations: Preprocessed data for crunchbase organizations.
    Returns:
        crunchbase_organizations_preprocessed : enriched and preprocessed org table

    """
    output_schema =StructType([
        StructField('name', StringType(), True),
        StructField('country_code', StringType(), True),
        StructField('url', StringType(), True),
        StructField('linkedin_url', StringType(), True),
        StructField('topics_list', ArrayType(StringType()), True)
        ])
    crunchbase_organizations_preprocessed \
    =  spark.createDataFrame([], output_schema)

    return crunchbase_organizations_preprocessed