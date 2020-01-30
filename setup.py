from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name="heroku-review-app-deploy",
    version="0.1",
    description="Deploy a Heroku Review App from outside Github",
    long_description=readme(),
    url="https://github.com/franciscoafonsoo/heroku-review-app-deploy",
    author="Francisco Pires",
    author_email="f.pires.dev@icloud.com",
    license="gpl-3.0",
    packages=["review_app"],
    install_requires=["requests", "python-dotenv"],
    entry_points={"console_scripts": ["dpl-review-app=review_app.main:main"]},
    zip_safe=False,
)
