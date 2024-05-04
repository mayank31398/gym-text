from typing import List

import numpy as np
from gymnasium.envs.box2d.lunar_lander import LunarLander


class LunarLanderTextEnvironment(LunarLander):
    def get_string_observation(self, observation: np.ndarray) -> str:
        x, y, v_x, v_y, angle, w, touching_left, touching_right = observation

        if touching_left == 1:
            if touching_right == 1:
                touching = "Currently both feet of the rocket are touching the ground."
            else:
                touching = "Currently only the left foot of the rocket is touching the ground."
        else:
            if touching_right == 1:
                touching = "Currently only the right foot of the rocket is touching the ground."
            else:
                touching = "Currently none of the feet are in contact with the ground."

        input_text = f"""A rocket is trying to land on the moon. The rocket has 3 built-in engines: left orientation engine, right-orientation engine and the main engine. The rocket also has 2 feet for landing safely (left and right). Your goal is to land safely on the surface of the moon on the landing pad.

The landing pad is located at (0, 0) and the current location of the rocket is ({x:.2f}, {y:.2f}). You are going with velocity ({v_x:.2f}, {v_y:.2f}) m/s and you are pointing towards {angle:.2f} radians with angular velocity {w:.2f} radians/sec. {touching}

Decide which action to take so that you land safely at the landing pad:
1. do nothing
2. fire left-orientation engine
3. fire main engine
4. fire right-orientation engine

Action to take:"""

        return input_text

    def get_string_action_space(self, eos_token: str = "") -> List[str]:
        return [
            f"do nothing{eos_token}",
            f"fire left-orientation engine{eos_token}",
            f"fire main engine{eos_token}",
            f"fire right-orientation engine{eos_token}",
        ]
