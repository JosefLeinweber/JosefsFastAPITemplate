import os
import subprocess


def upload_env_variables(env_file_path):
    """
    Uploads variables from a .env file to the GitHub repository as repository variables using the GitHub CLI.
    """
    if not os.path.exists(env_file_path):
        print(f"Error: {env_file_path} does not exist.")
        return

    with open(env_file_path, "r") as env_file:
        for line in env_file:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                key, value = key.strip(), value.strip()

                # Use the GitHub CLI to set the repository variable
                try:
                    subprocess.run(["gh", "variable", "set", key, "--body", value], check=True)
                    print(f"Uploaded: {key}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to upload {key}: {e}")


if __name__ == "__main__":
    env_file_path = ".env"
    upload_env_variables(env_file_path)
