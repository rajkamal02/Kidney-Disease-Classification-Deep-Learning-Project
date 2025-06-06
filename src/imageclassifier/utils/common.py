import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger  # Assuming you meant 'logger', not 'Logger'
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and returns
    Args:
        path_to_yaml (str): path like input
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type    
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create directories if not exists
    Args:
        path_to_directories (list): list of directories to be created
        verbose (bool): if True, print the directories created
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path_to_json: Path, data: dict):
    """save json file
    Args:
        path_to_json (Path): path to save json file
        data (dict): data to be saved in json file
    """
    with open(path_to_json, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path_to_json}")


@ensure_annotations
def read_json(path_to_json: Path) -> dict:
    """read json file
    Args:
        path_to_json (Path): path to json file
    Returns:
        dict: data from json file
    """
    with open(path_to_json, "r") as f:
        data = json.load(f)
    logger.info(f"json file read from: {path_to_json}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path to file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imagedata = base64.b64decode(imgstring)
    with open(fileName, "wb") as f:
        f.write(imagedata)


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

                                  