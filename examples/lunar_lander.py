import gymnasium as gym

import gym_text  # need to import this to register text environments


env = gym.make("LunarLander-v2-text", render_mode="human")

observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()  # this is where you would insert your policy
    observation, reward, terminated, truncated, info = env.step(action)
    print(env.get_string_observation(observation))

    if terminated or truncated:
        observation, info = env.reset()
