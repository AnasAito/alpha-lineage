from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import generate_edges
#


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [node(
                func=generate_edges,
                inputs=["orgs_xrefs",
                "topics_xrefs",
                "business_events_xrefs",
                "funding_rounds_xrefs",
                 "crunchbase_topic_association",
                "crunchbase_organization_hierarchy"],
                outputs=["alpha_organization_hierarchy","alpha_topic_association"],
                name="generate_alpha_edges",
            ), 
        
             

        ],
        namespace="generate_edges",
        inputs=["orgs_xrefs",
                "topics_xrefs",
                "business_events_xrefs",
                "funding_rounds_xrefs",
                "crunchbase_topic_association",
                "crunchbase_organization_hierarchy"
                ],
        outputs=["alpha_organization_hierarchy","alpha_topic_association"],
    )
