import os
import subprocess


def upload_string_as_secret(secret_name, secret_value):
    try:
        # Use the `gh` command to create or update the secret
        result = subprocess.run(
            ["gh", "secret", "set", secret_name, "--body", secret_value],
            check=True,
            capture_output=True,
            text=True,
        )
        print(f"Secret '{secret_name}' uploaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error uploading secret '{secret_name}': {e.stderr}")


def skip_empty_or_hashtag_lines(line):
    if "#" in line:
        return True
    if len(line) < 4:
        return True
    return False


def env_file_to_string():
    file = open(".env", "r")
    lines_of_file = file.readlines()
    env_var_as_string = ""
    for line in lines_of_file:
        if skip_empty_or_hashtag_lines(line):
            pass
        else:
            env_var_as_string += f"{line.rstrip()},"

    return env_var_as_string[:-1]


if __name__ == "__main__":
    upload_string_as_secret("ENV_VARIABLES", env_file_to_string())
