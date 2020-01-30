import requests


def write_review_app_name(base_url, headers, ra_id):
    url = f"https://api.heroku.com/apps/{ra_id}/config-vars"

    res = requests.get(url)
    res.raise_for_status()

    # export var to a file to be used in the next pipeline step
    with open("env.sh") as writer:
        var_env = f"export HEROKU_APP_NAME={res.get('HEROKU_APP_NAME')}"
        writer.write(var_env)
