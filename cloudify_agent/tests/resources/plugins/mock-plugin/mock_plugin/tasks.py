#########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.

import os

from cloudify.decorators import operation
from cloudify.utils import LocalCommandRunner


@operation
def run(**_):
    pass


@operation
def get_env_variable(env_variable, **_):
    return os.environ[env_variable]


@operation
def call_subprocess(command, **_):
    runner = LocalCommandRunner()
    result = runner.run(command)
    return result.std_out, result.std_err, result.return_code
