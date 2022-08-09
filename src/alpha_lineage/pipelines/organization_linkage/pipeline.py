from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import create_model_input_table, preprocess_companies, preprocess_shuttles , linkage_orgs



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="crunchbase_organizations_deduplicated",
                outputs="crunchbase_organizations_deduplicated_processed",
                name="crunchbase_linkage_preprocessing",
            ),
             node(
                func=preprocess_companies,
                inputs="open_alex_organizations_deduplicated",
                outputs="open_alex_organizations_deduplicated_processed",
                name="open_alex_linkage_preprocessing",
            ),
             node(
                func=linkage_orgs,
                inputs=["crunchbase_organizations_deduplicated_processed","open_alex_organizations_deduplicated_processed"],
                outputs="org_pairs_open_alex_crunchbase",
                name="open_alex_crunchbase_linkage_inference",
            ),
          
         
          
        ],
        namespace="organization_linkage",
        inputs=["open_alex_organizations_deduplicated","crunchbase_organizations_deduplicated"],
        outputs=["org_pairs_open_alex_crunchbase"],
    )
