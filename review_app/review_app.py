import requests


def get_config_vars(base_url, headers):
    url = f"{base_url}/apps/water-web-staging/config-vars"

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    return {
        k: v for k, v in res.json().items() if k not in ["DATABASE_URL", "REDIS_URL"]
    }


def create_review_app(base_url, source_blob_url, pipeline, branch, version, headers):
    url = f"{base_url}/review-apps"

    headers["Content-Type"] = "application/json"

    data = {
        "branch": branch,
        "pipeline": pipeline,
        "source_blob": {"url": source_blob_url, "version": f"v{version}"},
        "environment": get_config_vars(base_url, headers),
    }

    print("Creating Review app...")
    res = requests.post(url, headers=headers, json=data)
    res.raise_for_status()

    print("Done!")
    response = res.json()

    return response
