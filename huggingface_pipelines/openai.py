import os
import click
from langchain.llms import OpenAI
from typing import Optional

#  from getpass import getpass
# OPENAI_API_KEY = getpass()


def get_openai_instance(api_key: Optional[str] = None) -> Optional[OpenAI]:
    """
    Create an instance of the OpenAI API client.

    Parameters:
        api_key (str, optional): OpenAI API key.

    Returns:
        OpenAI or None: An instance of the OpenAI API client or None if API key is not provided.
    """
    if api_key is None:
        api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        print("OpenAI API key not provided or found in the environment.")
        return None

    return OpenAI(openai_api_key=api_key)


@click.command()
@click.option("--api-key", help="OpenAI API Key")
def main(api_key):
    # Get the OpenAI API key from the environment or provided as a command-line argument
    openai_api_key = api_key or os.getenv("OPENAI_API_KEY")

    if openai_api_key is None:
        print("OpenAI API key not provided.")
        return

    # Create an instance of the OpenAI object
    llm = get_openai_instance(api_key=openai_api_key)

    if llm:
        # Now you can use the llm object to interact with the OpenAI API
        print("OpenAI instance created successfully.")


if __name__ == "__main__":
    main()
