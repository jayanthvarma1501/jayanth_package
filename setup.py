import setuptools


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "jayanth_package"
AUTHOR_USER_NAME = "jayanthvarma1501"
SRC_REPO = "jayanth_package"

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email="jayanthvarma1501@gmail.com",
    description= "A small python package",
    long_description= long_description,
    long_description_content= "text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir= {"": "src"},
    packages= setuptools.find_packages(where="src")
)
