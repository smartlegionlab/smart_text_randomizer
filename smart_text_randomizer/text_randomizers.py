# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import re
import secrets


class TextRandomizer:
    @classmethod
    def randomize(cls, text: str) -> str:
        """
        Randomizes the input text by replacing patterns enclosed in curly braces with randomly selected elements.

        The method looks for patterns in the input text that are enclosed in curly braces `{}`.
        Inside the braces, multiple options can be provided, separated by a vertical bar `|`.
        For each occurrence of such a pattern, one of the options is randomly selected and
        replaces the entire pattern in the text.

        For example:
        - Input: "Hello, {Alice|Bob|Charlie}!"
        - Output: "Hello, Bob!" (or "Hello, Alice!" or "Hello, Charlie!", randomly chosen)

        :param text: The input text containing patterns to be randomized.
        :return: The randomized text with patterns replaced by randomly selected options.
        """
        return re.sub(r"{(.+?)}", lambda x: secrets.choice(x.group(1).split("|")), text)
