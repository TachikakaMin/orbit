# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES, ETH Zurich, and University of Toronto
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause


import gym

from . import agents, flat_env_cfg, rough_env_cfg

##
# Register Gym environments.
##

gym.register(
    id="Isaac-Velocity-Flat-Anymal-D-v0",
    entry_point="omni.isaac.orbit.envs.rl_env:RLEnv",
    kwargs={
        "env_cfg_entry_point": flat_env_cfg.AnymalDFlatEnvCfg,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.AnymalDFlatPPORunnerCfg,
    },
)

gym.register(
    id="Isaac-Velocity-Flat-Anymal-D-Play-v0",
    entry_point="omni.isaac.orbit.envs.rl_env:RLEnv",
    kwargs={
        "env_cfg_entry_point": flat_env_cfg.AnymalDFlatEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.AnymalDFlatPPORunnerCfg,
    },
)

gym.register(
    id="Isaac-Velocity-Rough-Anymal-D-v0",
    entry_point="omni.isaac.orbit.envs.rl_env:RLEnv",
    kwargs={
        "env_cfg_entry_point": rough_env_cfg.AnymalDRoughEnvCfg,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.AnymalDRoughPPORunnerCfg,
    },
)

gym.register(
    id="Isaac-Velocity-Rough-Anymal-D-Play-v0",
    entry_point="omni.isaac.orbit.envs.rl_env:RLEnv",
    kwargs={
        "env_cfg_entry_point": rough_env_cfg.AnymalDRoughEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.AnymalDRoughPPORunnerCfg,
    },
)
