from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import generate_orgs_vertices,generate_funding_rounds_vertices,generate_unlinked_vertices,generate_xrefs,generate_alpha_nodes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [node(
                func=generate_xrefs,
                inputs=["crunchbase_funding_rounds",
                        "crunchbase_topics",
                        "crunchbase_business_events"],
                outputs=["funding_rounds_xrefs",
                         "topics_xrefs",
                         "business_events_xrefs"],
                name="generate_xrefs_unlinked_vertices",
            ), 
            node(
                func=generate_alpha_nodes,
                inputs=["funding_rounds_xrefs","topics_xrefs","business_events_xrefs",
                        "crunchbase_funding_rounds","crunchbase_topics","crunchbase_business_events"],
                outputs=["alpha_funding_rounds","alpha_topics","alpha_business_events"],
                name="generate_alpha_unlinked_vertices",
            ),
            node(
                func=generate_orgs_vertices,
                inputs=["orgs_xrefs",
                "crunchbase_organizations",
                "open_alex_organizations",
                "google_patents_organizations"],
                outputs="alpha_organizations",
                name="generate_alpha_orgs_vertices",
            )
             

        ],
        namespace="generate_vertices",
        inputs=["orgs_xrefs",
                "crunchbase_organizations",
                "open_alex_organizations",
                "google_patents_organizations",
                 "crunchbase_funding_rounds",
                "crunchbase_topics",
                "crunchbase_business_events",],
        outputs=["alpha_organizations",
                "alpha_funding_rounds",
                "alpha_business_events",
                "alpha_topics"],
    )
