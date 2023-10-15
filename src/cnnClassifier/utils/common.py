import os
import yaml
import json
import joblib
import base64
from typing import Any
from pathlib import Path
from box import ConfigBox, Box
from typing import List, Dict
from cnnClassifier import configure_logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError

logger = configure_logger("logs", "loggings.log")

@ensure_annotations
def read_yaml(path: Path) -> Box:
    """
    Read and parse a YAML file from the given path.

    Args:
        path (Path): The path to the YAML file.

    Returns:
        Box: A parsed YAML content stored in a Box object.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For other unexpected exceptions during file reading or parsing.
    """
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file '{path}' loaded successfully.")
            return Box(content)
    except BoxValueError as e:
        raise ValueError(f"Error parsing YAML file '{path}': {str(e)}")
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file '{path}' not found.")
    except Exception as e:
        logger.error(f"An error occurred while reading YAML file '{path}': {str(e)}")
        raise


@ensure_annotations
def create_directories(paths_list: list, verbose=True):
    """
    Create directories specified in the paths_list.

    Args:
        paths_list (List[str]): A list of directory paths to create.
        verbose (bool, optional): If True, log directory creation messages. Defaults to True.

    Returns:
        None
    """
    try:
        for path in paths_list:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
    except Exception as e:
        logger.error(f"An error occurred while creating directories: {str(e)}")
        raise
    
@ensure_annotations
def save_json(path: Path, data: Dict) -> None:
    """
    Save data as JSON to the specified file path.

    Args:
        path (Path): The path to the JSON file.
        data (Dict): The data to be saved as JSON.

    Returns:
        None

    Raises:
        IOError: If there is an issue while writing to the file.
    """
    try:
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
        logger.info(f"JSON data saved to: {path}")
    except IOError as e:
        logger.error(f"Error saving JSON data to '{path}': {str(e)}")
        raise

@ensure_annotations
def load_json(path: Path) -> Box:
    """
    Load JSON data from the specified file path.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        Box: A Box object containing the loaded JSON data.

    Raises:
        FileNotFoundError: If the JSON file is not found.
        json.JSONDecodeError: If there is an issue while decoding the JSON data.
    """
    try:
        with open(path) as file:
            content = json.load(file)
        logger.info(f"JSON data loaded successfully from path: {path}")
        return Box(content)
    except FileNotFoundError:
        logger.error(f"JSON file not found at path: {path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON data from '{path}': {str(e)}")
        raise

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Save binary data to the specified file path.

    Args:
        data (Any): The data to be saved in binary format.
        path (Path): The path to the binary file.

    Returns:
        None

    Raises:
        Exception: If there is an issue while saving the binary data.
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary data saved successfully to path: {path}")
    except Exception as e:
        logger.error(f"Error saving binary data to '{path}': {str(e)}")
        raise

@ensure_annotations
def load_bin(path: Path):
    """
    Load binary data from the specified file path.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The loaded binary data.

    Raises:
        FileNotFoundError: If the binary file is not found.
        Exception: If there is an issue while loading the binary data.
    """
    try:
        if not path.exists():
            raise FileNotFoundError(f"Binary file not found at path: {path}")

        data = joblib.load(path)
        logger.info(f"Binary data loaded successfully from path: {path}")
        return data
    except FileNotFoundError:
        logger.error(f"Binary file not found at path: {path}")
        raise
    except Exception as e:
        logger.error(f"Error loading binary data from '{path}': {str(e)}")
        raise

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in kilobytes (KB) and return it as a formatted string.

    Args:
        path (Path): The path to the file.

    Returns:
        str: The file size in KB as a formatted string (e.g., "~123 KB").

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    try:
        if not path.exists():
            raise FileNotFoundError(f"File not found at path: {path}")

        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~{size_in_kb} KB"
    except FileNotFoundError:
        raise

def decode_image(encoded_image: str, file_name):
    """
    Decode a base64-encoded image and save it to a file.

    Args:
        encoded_image (str): The base64-encoded image data as a string.
        file_name (str): The name of the file to save the decoded image.

    Returns:
        None

    Raises:
        ValueError: If the encoded_image is not a valid base64 string.
        IOError: If there is an issue while writing the image data to the file.
    """
    try:
        # Decode the base64-encoded image
        img_data = base64.b64decode(encoded_image)

        # Save the decoded image to the specified file
        with open(file_name, "wb") as file:
            file.write(img_data)

    except ValueError as e:
        raise ValueError("Invalid base64-encoded image string.") from e

    except IOError as e:
        raise IOError(f"Error writing the decoded image to '{file_name}': {str(e)}") from e


def encode_image_into_base64(image_path: str):
    """
    Encode an image from the specified file path into a base64 string.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The base64-encoded image data as a string.

    Raises:
        FileNotFoundError: If the image file is not found.
        IOError: If there is an issue while reading the image data.
    """
    try:
        # Read the image data from the specified file
        with open(image_path, "rb") as file:
            image_data = file.read()

        # Encode the image data into base64
        encoded_image = base64.b64encode(image_data).decode("utf-8")

        return encoded_image

    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found at path: {image_path}")

    except IOError as e:
        raise IOError(f"Error reading the image data from '{image_path}': {str(e)}") from e
