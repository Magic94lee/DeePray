# -*- coding:utf-8 -*-
#  Copyright © 2020-2020 Hailin Fu All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  ==============================================================================
"""
Author:
    Hailin Fu, hailinfufu@outlook.com
"""
from deepray.model.model_fm import FactorizationMachine


class NeuralFactorizationMachine(FactorizationMachine):
    def build(self, input_shape):
        hidden = [int(h) for h in self.flags.deep_layers.split(',')]
        self.B_Interaction_Layer = self.build_fm()
        self.Hidden_Layers = self.build_deep(hidden)

    def build_network(self, features, is_training=None):
        """

        :param features:
        :param is_training:
        :return:
        """
        logit = self.B_Interaction_Layer(features)
        logit = self.Hidden_Layers(logit)
        return logit
