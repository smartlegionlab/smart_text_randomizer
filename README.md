# smart_text_randomizer

Smart Text Randomizer.

---

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart_text_randomizer)](https://github.com/smartlegionlab/smart_text_randomizer/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smart_text_randomizer?label=pypi%20downloads)](https://pypi.org/project/smart_text_randomizer/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart_text_randomizer)
[![PyPI](https://img.shields.io/pypi/v/smart_text_randomizer)](https://pypi.org/project/smart_text_randomizer)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smart_text_randomizer)](https://github.com/smartlegionlab/smart_text_randomizer/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smart_text_randomizer)](https://pypi.org/project/smart_text_randomizer)

***

Author and developer: ___A.A. Suvorov.___

***

## What is news:

smart_text_randomizer v0.0.2

- Fixed bugs.
- Added documentation.
- Improved security. random was replaced with secrets.

***

## Help:

`pip install smart_text_randomizer`

"Text randomization" or "variable text". It is used to create different variations of the same message.

You are using special syntax. Example: `'{Salute|Hello|Good morning} {comrade|buddy|dear friend}!'`

This syntax allows you to create variable messages by using curly braces and vertical bars to indicate alternatives.

Basic elements of syntax:

1. Curly braces {}: Used to group text options. Anything inside the curly braces will be randomly selected when generating the text.
2. Vertical bar |: Used to separate different text options within curly braces. Each option will be treated as a separate choice.

Example of use:

- Syntax: `'{Salute|Hello|Good morning} {comrade|buddy|dear friend}!'`
- Possible results:
    - Salute comrade!
    - Salute buddy!
    - Salute dear friend!
    - Hello comrade!
    - Hello buddy!
    - Hello dear friend!
    - Good morning comrade!
    - Good morning buddy!
    - Good morning dear friend!
- How to use:
  1. Create your text: Identify which parts of your message can vary and place them in curly braces.
  2. Add options: Separate alternatives with a vertical bar.
  3. Text Generation: Use RandomStringMaster() to generate a random message.

- Notes:
    - Make sure all options inside the curly braces make sense and fit the context.
    - You can use multiple randomization groups in a single message to create more complex variations.


Example of text randomization:

```python
from smart_text_randomizer import TextRandomizer

text_randomizer = TextRandomizer()

text = '{Salute|Hello|Good morning} {comrade|buddy|dear friend}!'
randomized_text = TextRandomizer.randomize(text)
print(randomized_text) # Good morning buddy!
```

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------

