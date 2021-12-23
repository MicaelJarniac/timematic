import nox

python_versions = ["3.8", "3.9", "3.10"]


@nox.session(python=python_versions[-1], reuse_venv=True)
def format(session: nox.Session):
    session.install("-r", "requirements-dev.txt")
    session.run("isort", ".")
    session.run("black", ".")


@nox.session(python=python_versions[-1], reuse_venv=True)
def lint(session: nox.Session):
    session.install("-r", "requirements-dev.txt")
    session.run("flake8", "src")


@nox.session(python=python_versions, reuse_venv=True)
def typecheck(session: nox.Session):
    session.install("-r", "requirements-dev.txt")
    session.install(".")
    session.run("mypy")


@nox.session(python=python_versions)
def test(session: nox.Session):
    session.install(".")
    session.install("pytest")
    session.run("pytest")
