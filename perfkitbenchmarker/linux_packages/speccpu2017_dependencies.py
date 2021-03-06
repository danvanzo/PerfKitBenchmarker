# Copyright 2018 PerfKitBenchmarker Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module containing installation functions for SPEC CPU 2017 dependencies."""

from perfkitbenchmarker.linux_packages import INSTALL_DIR

LLVM_TAR = 'clang+llvm-3.9.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz'
LLVM_TAR_URL = 'http://releases.llvm.org/3.9.0/{0}'.format(LLVM_TAR)
OPENMP_TAR = 'libomp_20160808_oss.tgz'
OPENMP_TAR_URL = 'https://www.openmprtl.org/sites/default/files/{0}'.format(
    OPENMP_TAR)


def Install(vm):
  """Installs SPECCPU 2017 dependencies."""
  vm.RemoteCommand('cd {0} && wget {1} && tar xf {2}'.format(
      INSTALL_DIR, LLVM_TAR_URL, LLVM_TAR))
  vm.RemoteCommand('cd {0} && wget {1} && tar xf {2}'.format(
      INSTALL_DIR, OPENMP_TAR_URL, OPENMP_TAR))
  vm.RemoteCommand('sudo apt-get install libjemalloc1 libjemalloc-dev')
  vm.RemoteCommand('sudo apt-get update && sudo apt-get install -y libomp-dev')
