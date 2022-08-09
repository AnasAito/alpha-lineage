"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from alpha_lineage.pipelines import organization_deduplication as org_dedub
from alpha_lineage.pipelines import organization_linkage as org_linkage
from alpha_lineage.pipelines import orgs_clustering as orgs_cluster
from alpha_lineage.pipelines import graph_vertices_generation as g_vertices_generate
def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    org_dedub_pipeline = org_dedub.create_pipeline()
    org_linkage_pipeline = org_linkage.create_pipeline()
    orgs_cluster_pipeline = orgs_cluster.create_pipeline()
    g_vertices_generate_pipeline = g_vertices_generate.create_pipeline()

    return {
        "__default__": org_dedub_pipeline+org_linkage_pipeline+orgs_cluster_pipeline+g_vertices_generate_pipeline,
        'org_dedub' : org_dedub_pipeline , 
        'org_linkage' : org_linkage_pipeline,
        'orgs_cluster':orgs_cluster_pipeline,
        "g_vertices_generate" : g_vertices_generate_pipeline
    }
