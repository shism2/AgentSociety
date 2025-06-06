"""
This module provides a wrapper around MLflow's MlflowClient for managing experiments and runs.

Mapping Rule:
- exp_name (set by user) -> mlflow experiment name
- exp_id (generated by agentsociety) -> mlflow run name
"""

import asyncio
import os
from collections.abc import Sequence
from typing import Any, Optional

import mlflow
from mlflow.entities import Metric, Param, RunTag
from pydantic import BaseModel, Field

from ..logger import get_logger
from ..utils.decorators import lock_decorator

__all__ = [
    "MlflowClient",
    "MlflowConfig",
]


class MlflowConfig(BaseModel):
    """MLflow configuration class."""

    enabled: bool = Field(False)
    """Whether MLflow is enabled"""

    username: Optional[str] = Field(None)
    """Username for MLflow"""

    password: Optional[str] = Field(None)
    """Password for MLflow"""

    mlflow_uri: str = Field(...)
    """URI for MLflow server"""


class MlflowClient:
    """A wrapper around MLflow's MlflowClient for managing experiments and runs."""

    def __init__(
        self,
        config: MlflowConfig,
        exp_name: str,
        exp_id: str,
        current_run_id: Optional[str] = None,
    ) -> None:
        """
        Initialize the MlflowClient.

        - **Args**:
            - **config** (MlflowConfig): Configuration containing MLflow credentials and URI.
            - **exp_name** (str, optional): Name of the experiment. Defaults to a generated name.
            - **exp_id** (str): A unique identifier for the experiment.
            - **current_run_id** (str, optional): Existing MLflow run ID to attach to. Defaults to None.
        """

        self._config = config
        if not self.enabled:
            get_logger().warning("Mlflow is not enabled")
            return

        # Connect to existing run
        self._mlflow_uri = config.mlflow_uri
        if config.username is not None:
            os.environ["MLFLOW_TRACKING_USERNAME"] = config.username
        if config.password is not None:
            os.environ["MLFLOW_TRACKING_PASSWORD"] = config.password
        # Initialize MLflow client
        self._mlflow_uri = config.mlflow_uri
        self._client = mlflow.MlflowClient(tracking_uri=self._mlflow_uri)
        if current_run_id is None:
            run_name = exp_id

            # Create or get experiment
            try:
                mlflow_experiment_id = self._client.create_experiment(
                    name=exp_name,
                )
            except mlflow.MlflowException as e:
                experiment = self._client.get_experiment_by_name(exp_name)
                if experiment is None:
                    import traceback

                    traceback.print_exc()
                    raise e
                mlflow_experiment_id = experiment.experiment_id

            # Create run
            self._run = self._client.create_run(
                experiment_id=mlflow_experiment_id, run_name=run_name
            )
            self._run_id = self._run.info.run_id
        else:
            self._run_id = current_run_id
            self._run = self._client.get_run(run_id=self._run_id)

        self._lock = asyncio.Lock()

    @property
    def enabled(self):
        return self._config.enabled

    def close(self): ...

    @property
    def client(self):
        """Return the underlying MLflow client."""
        return self._client

    @property
    def run_id(self) -> str:
        """Return the current run ID."""
        return self._run_id

    @lock_decorator
    async def log_batch(
        self,
        metrics: Sequence[Metric] = (),
        params: Sequence[Param] = (),
        tags: Sequence[RunTag] = (),
    ):
        """
        Log a batch of metrics, parameters, and tags to the MLflow run.

        This method is thread-safe due to the `@lock_decorator`.
        """
        self.client.log_batch(
            run_id=self.run_id, metrics=metrics, params=params, tags=tags
        )

    @lock_decorator
    async def log_metric(
        self,
        key: str,
        value: float,
        step: Optional[int] = None,
        timestamp: Optional[int] = None,
    ):
        """
        Log a single metric to the MLflow run.

        This method is thread-safe due to the `@lock_decorator`.

        - **Args**:
            key (str): The name of the metric.
            value (float): The value of the metric.
            step (int, optional): The step at which the metric was recorded. Defaults to None.
            timestamp (int, optional): The timestamp when the metric was recorded. Defaults to None.
        """
        get_logger().info(f"Logging metric {key} with value {value} at step {step}")
        if timestamp is not None:
            timestamp = int(timestamp)
        self.client.log_metric(
            run_id=self.run_id,
            key=key,
            value=value,
            timestamp=timestamp,
            step=step,
        )
