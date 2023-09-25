import click
from langchain.llms import HuggingFacePipeline
from typing import Dict

def create_pipeline(model_id: str, task: str, model_kwargs: Dict[str, int]) -> HuggingFacePipeline:
    """
    Create a HuggingFace pipeline based on given model id, task and model parameters.
    :param model_id: Model identifier.
    :param task: Pipeline task.
    :param model_kwargs: Model parameteres.
    :returns: Pipeline instance.
    """
    return HuggingFacePipeline.from_model_id(model_id, task, model_kwargs)

@click.command()
@click.option("--model_id", default="bigscience/bloom-1b7", help="Identifier for the HuggingFace model.")
@click.option("--task", default="text-generation", help="The task to perform with the model.")
@click.option("--model_kwargs", default={"temperature": 0, "max_length": 64}, help="Additional parameters for the model.")
def main(model_id: str, task: str, model_kwargs: Dict[str, int]) -> None:
    """
    Main command line function to create a HuggingFace pipeline.
    :param model_id: Model identifier.
    :param task: Pipeline task.
    :param model_kwargs: Model parameteres.
    :returns: None.
    """
    llm = create_pipeline(model_id, task, model_kwargs)
    # ... use the pipeline


if __name__ == "__main__":
    main()
