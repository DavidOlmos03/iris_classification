import subprocess
import requests

def test_docker_build():
    result = subprocess.run(["docker", "build", "-t", "iris-api", "."], capture_output=True)
    assert result.returncode == 0, f"Docker build failed: {result.stderr.decode()}"

def test_docker_run():
    subprocess.run(["docker", "run", "-d", "-p", "8000:8000", "--name", "iris-container", "iris-api"], capture_output=True)
    try:
        response = requests.get("http://localhost:8000/info")
        assert response.status_code == 200
    finally:
        subprocess.run(["docker", "stop", "iris-container"], capture_output=True)
        subprocess.run(["docker", "rm", "iris-container"], capture_output=True)
