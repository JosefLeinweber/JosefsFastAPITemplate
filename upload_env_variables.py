import os
import subprocess


def upload_env_file_as_secret(env_file_path):
    """
    Uploads variables from a .env file to the GitHub repository as repository secrets using the GitHub CLI.
    """
    if not os.path.exists(env_file_path):
        print(f"Error: {env_file_path} does not exist.")
        return

    try:

        subprocess.run(
            ["gh", "secret", "set", "ENV_FILE", "--body", env_file_path],
            check=True,
        )
        print(f"Uploaded {env_file_path} as a secret.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upload {env_file_path}: {e}")


def delete_all_variables():
    """
    Deletes all repository variables using the GitHub CLI.
    """

    try:
        # List all secrets and delete them one by one
        result = subprocess.run(
            ["gh", "variable", "list"],
            capture_output=True,
            text=True,
            check=True,
        )
        variables = result.stdout.splitlines()

        for variable in variables:
            variable_name = variable.split()[0]  # Get the name of the secret
            subprocess.run(
                ["gh", "variable", "delete", variable_name],
                check=True,
            )
            print(f"Deleted: {variable_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete secrets: {e}")


if __name__ == "__main__":
    env_file_path = ".env"
    upload_env_file_as_secret(env_file_path)
    # delete_all_variables()
