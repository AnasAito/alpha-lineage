from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import generate_orgs_vertices,generate_funding_rounds_vertices


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_orgs_vertices,
                inputs=["orgs_xrefs",
                "crunchbase_organizations",
                "open_alex_organizations",
                "google_patents_organizations"],
                outputs="alpha_organizations",
                name="generate_orgs_vertices",
            ), 
       
             node(
                func=generate_funding_rounds_vertices,
                inputs=["crunchbase_funding_rounds"],
                outputs="alpha_funding_rounds",
                name="generate_funding_rounds_vertices",
            ), 
        ],
        namespace="generate_vertices",
        inputs=["orgs_xrefs",
                "crunchbase_funding_rounds",
                "crunchbase_organizations",
                "open_alex_organizations",
                "google_patents_organizations"],
        outputs=["alpha_organizations","alpha_funding_rounds"],
    )
