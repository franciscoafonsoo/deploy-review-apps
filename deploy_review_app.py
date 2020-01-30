#!/usr/bin/env python
__all__ = ("main",)


def main():
    """
    Tool to deploy a Heroku Review App in Bitbucket Pipelines.

    Variables needed for deploying:
        - Path to the project
        - settings for the Heroku Platform API
        - Bitbucket Pipelines variables
        - Heroku Project Name

    Make sure you include this envs in the pipeline:
        - HEROKU_API_KEY
        - HEROKU_PROJECT_NAME

    https://devcenter.heroku.com/articles/heroku-postgres-backups#direct-database-to-database-copies
    """
    from review_app import (
        create_review_app,
        create_source_blob,
        get_pipeline_id,
        write_review_app_name,
    )

    import os
    from pathlib import Path
    from dotenv import load_dotenv

    base_dir = Path.cwd().parent
    env_path = base_dir / ".env"

    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("HEROKU_API_KEY")
    branch = os.getenv("BITBUCKET_BRANCH")
    base_url = "https://api.heroku.com"
    project = os.getenv("HEROKU_DEV_NAME")
    heroku_pipeline_name = os.getenv("HEROKU_PIPELINE_NAME")
    version = os.getenv("BITBUCKET_COMMIT")

    headers = {
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {api_key}",
    }

    write_review_app_name(base_url, headers, res.get("app", {}).get("id"))

    pipeline_id = get_pipeline_id(base_url, headers, heroku_pipeline_name)

    source_blob_url = create_source_blob(base_url, base_dir, project, version, headers)

    res = create_review_app(
        base_url, source_blob_url, pipeline_id, branch, version, headers
    )


    return res


if __name__ == "__main__":  # pragma: no cover
    from pprint import pprint
    pprint(main())
