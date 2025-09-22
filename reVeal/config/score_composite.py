"""
config.score_composite module
"""
from typing import List

from typing_extensions import Annotated
from pydantic import model_validator, FilePath, Field

from reVeal.config.config import BaseModelStrict, BaseGridConfig
from reVeal.fileio import attribute_is_numeric


class Attribute(BaseModelStrict):
    """
    Inputs for a single attribute entry in the ScoreCompositeConfig.
    """

    # Input at instantiation
    attribute: str
    weight: Annotated[float, Field(strict=True, gt=0, le=1)]
    dset_src: FilePath

    @model_validator(mode="after")
    def attribute_check(self):
        """
        Check that attribute is present in the input dataset and is a numeric datatype.

        Raises
        ------
        TypeError
            A TypeError will be raised if the input attribute exists in the dataset
            but is not a numeric datatype.
        """

        if not attribute_is_numeric(self.dset_src, self.attribute):
            raise TypeError(
                f"Attribute {self.attribute} in {self.dset_src} is invalid type. Must "
                "be a numeric dtype."
            )
        return self


class ScoreCompositeConfig(BaseGridConfig):
    """
    Configuration for score-composite command.
    """

    attributes: List[Attribute]

    @model_validator(mode="before")
    def propagate_grid(self):
        """
        Propagate the top level grid parameter down to elements of
        attributes before validation.

        Returns
        -------
        self
            Returns self.
        """
        for attribute in self["attributes"]:
            if "dset_src" not in attribute:
                attribute["dset_src"] = self["grid"]

        return self

    @model_validator(mode="after")
    def validate_sum_attribute_weights(self):
        """
        Validate that the sum of all attribute weights is equal to 1.
        """

        sum_weights = 0
        for attribute in self.attributes:
            sum_weights += attribute.weight

        if sum_weights != 1:
            raise ValueError(
                "Weights of input attributes must sum to 1. "
                f"Sum of input weights is: {sum_weights}."
            )

        return self
