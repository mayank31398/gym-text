import gymnasium as gym

from .environments import LunarLanderTextEnvironment


_CUSTOM_ENV_REGISTRY = [
    ("LunarLander-v2", LunarLanderTextEnvironment),
]


def register_environments() -> None:
    for env_id, env_class in _CUSTOM_ENV_REGISTRY:
        gym.register(f"{env_id}-text", env_class)
