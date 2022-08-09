"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from alpha_lineage.pipelines import organization_deduplication as org_dedub
from alpha_lineage.pipelines import organization_linkage as org_linkage


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    org_dedub_pipeline = org_dedub.create_pipeline()
    org_linkage_pipeline = org_linkage.create_pipeline()

    return {
        "__default__": org_dedub_pipeline+org_linkage_pipeline,
        'org_dedub' : org_dedub_pipeline , 
        'org_linkage' : org_linkage_pipeline
    }
