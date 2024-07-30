# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import random
import re


class TextRandomizer:

    @classmethod
    def randomize(cls, message):
        res = re.sub(r"{(.+?)}", lambda x: random.choice(x.group(1).split("|")), message)
        return res

    def __call__(self, message):
        return self.randomize(message)
