# Copyright 2017 AT&T Corporation.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_policy import policy

RULE_ADMIN_API = 'rule:admin_api'
RULE_DEFAULT = 'rule:default'


rules = [
    policy.RuleDefault(
        name='context_is_admin',
        check_str='role:admin'),
    policy.RuleDefault(
        name='admin_api',
        check_str='is_admin:1'),
    policy.RuleDefault(
        name='default',
        check_str='')
]


def list_rules():
    return rules
