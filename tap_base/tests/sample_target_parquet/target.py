"""Sample target test for target-parquet."""

import copy
import json
import sys
import os

from jsonschema import Draft4Validator, FormatChecker
from pathlib import Path
from typing import Any, Dict, Iterable, List

import pyarrow as pa
import pyarrow.parquet as pq
import singer

# Reuse the tap connection rather than create a new target connection:
from tap_base.tests.sample_tap_parquet.connection import SampleParquetConnection

from tap_base.target_base import TargetBase


PLUGIN_NAME = "sample-target-parquet"
PLUGIN_VERSION_FILE = "./VERSION"
PLUGIN_CAPABILITIES = [
    "sync",
    "catalog",
    "discover",
    "state",
]
ACCEPTED_CONFIG = ["filepath"]
REQUIRED_CONFIG_SETS = [["filepath"]]


class SampleTargetParquet(TargetBase):
    """Sample target for Parquet."""

    _conn: SampleParquetConnection
    _schemas: Dict[str, Dict]
    _validators: Dict[str, Draft4Validator]
    _key_properties: Dict[str, List[str]] = {}
    _records_to_load: Dict[str, Dict[str, Any]] = {}
    _row_count: Dict[str, int] = {}
    _stream_to_sync: Dict[str, Any] = {}
    _total_row_count: Dict[str, int] = {}

    _state = None
    _flushed_state = None

    def __init__(self, config: dict, state: dict = None) -> None:
        """Initialize the target."""
        vers = Path(PLUGIN_VERSION_FILE).read_text()
        super().__init__(
            plugin_name=PLUGIN_NAME,
            version=vers,
            capabilities=PLUGIN_CAPABILITIES,
            accepted_options=ACCEPTED_CONFIG,
            option_set_requirements=REQUIRED_CONFIG_SETS,
            connection_class=SampleParquetConnection,
            config=config,
        )