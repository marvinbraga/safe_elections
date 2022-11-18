from pathlib import Path

from invoke import task

PROJECT_ROOT = Path(__file__).parent.absolute()

DC_FILE = "docker-compose.yml"
DC_CMD = f"docker-compose -f {DC_FILE}"


@task
def build(c, dev=False):
    """
    Prepare and build docker file.
    :param c: Context
    :param dev: bool
    :return: None
    """
    cmd = " ".join(
        [
            "poetry export",
            "--without-hashes",
            "-f requirements.txt",
            "-o requirements.txt",
        ],
    )
    c.run(cmd, pty=True)
    c.run("docker build --file ./.docker/django/Dockerfile -t safe_elections .")
    c.run("rm -f requirements.txt")


@task(build)
def up(c, d=False):
    """
    Run docker-compose file.
    :param c: Context
    :param d: Detached
    :return: None
    """
    cmd = f"{DC_CMD} up"
    cmd += " -d" if d else ""
    c.run(cmd)


@task
def stop(c, container=""):
    """
    Stop docker-compose
    :param c: Context
    :param container: Name
    :return: None
    """
    cmd = f"{DC_CMD} stop"
    cmd += f" {container}" if container else ""
    c.run(cmd)


@task
def down(c):
    """
    Docker-compose down
    :param c: Context
    :return: None
    """
    cmd = f"{DC_CMD} down -v --remove-orphans"
    c.run(cmd)


@task
def logs(c, args="api"):
    """
    Docker logs
    :param c: Context
    :param args: Service name
    :return: None
    """
    cmd = f"{DC_CMD} logs --tail 200 -f {args}"
    c.run(cmd)


@task
def status(c):
    """
    Docker ps
    :param c: Context
    :return: None
    """
    c.run(f"{DC_CMD} ps")


@task
def sh(c):
    """
    Docker-compose shell
    :param c: Context
    :return: None
    """
    c.run(f"{DC_CMD} exec api bash", pty=True)


@task(down)
def prune(c, restart=False):
    """
    Docker-compose shell
    :param restart:
    :param c: Context
    :return: None
    """
    print("Cleaning docker images...")
    c.run("docker system prune --all", pty=True)
    print("Cleaning docker volumes...")
    c.run("docker volume prune", pty=True)
    if restart:
        print("Restarting docker service...")
        c.run("sudo service docker restart", pty=True)
