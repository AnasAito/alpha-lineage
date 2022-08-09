from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import create_model_input_table, preprocess_companies, preprocess_shuttles


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="crunchbase_organizations",
                outputs="crunchbase_organizations_preprocessed",
                name="crunchbase_preprocessing",
            ),
             node(
                func=preprocess_companies,
                inputs="crunchbase_organizations_preprocessed",
                outputs="crunchbase_organizations_deduplicated",
                name="crunchbase_inference",
            ),
             node(
                func=preprocess_companies,
                inputs="open_alex_organizations",
                outputs="open_alex_organizations_preprocessed",
                name="open_alex_preprocessing",
            ),
             node(
                func=preprocess_companies,
                inputs="open_alex_organizations_preprocessed",
                outputs="open_alex_organizations_deduplicated",
                name="open_alex_inference",
            ),
              node(
                func=preprocess_companies,
                inputs="google_patents_organizations",
                outputs="google_patents_organizations_preprocessed",
                name="google_patents_preprocessing",
            ),
             node(
                func=preprocess_companies,
                inputs="google_patents_organizations_preprocessed",
                outputs="google_patents_organizations_deduplicated",
                name="google_patents_inference",
            ),
         
          
        ],
        namespace="organization_deduplication",
        inputs=["crunchbase_organizations","open_alex_organizations","google_patents_organizations"],
        outputs=["crunchbase_organizations_deduplicated",
                 "open_alex_organizations_deduplicated",
                 "google_patents_organizations_deduplicated"],
    )
