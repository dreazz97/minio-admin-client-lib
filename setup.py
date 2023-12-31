#Minio Admin wrapper using the MinIO client (mc) that provides admin operations and others that are not supported yet by the Minio SDK.
#Please note that this requires the MinIO client (mc) to operate.


# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
    name='pyminioadmin',
    version='0.0.8',
    url="https://github.com/dreazz97/minio-admin-client-lib",
    description='A Python wrapper for the MinIO client (mc)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Iuri Peniche',
    author_email='iuripeniche@hotmail.com',
    packages=['pyminioadmin'],
    license="Apache-2.0",
)