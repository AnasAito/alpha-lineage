from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import cluster_orgs


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=cluster_orgs,
                inputs=["org_pairs_open_alex_crunchbase",
                        "org_pairs_open_alex_google_patents",
                        "org_pairs_crunchbase_google_patents",
                        "crunchbase_organizations_deduplicated",
                        "open_alex_organizations_deduplicated",
                        "google_patents_organizations_deduplicated"],
                outputs="orgs_xrefs",
                name="generate_orgs_xrefs",
            ), 
        ],
        namespace="organization_clustering",
        inputs=["org_pairs_open_alex_crunchbase",
                        "org_pairs_open_alex_google_patents",
                        "org_pairs_crunchbase_google_patents",
                        "crunchbase_organizations_deduplicated",
                        "open_alex_organizations_deduplicated",
                        "google_patents_organizations_deduplicated"],
        outputs=["orgs_xrefs"],
    )
