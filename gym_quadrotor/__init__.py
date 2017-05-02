from gym.envs.registration import register

register(
    id='Quadrotor-v0',
    entry_point='gym_quadrotor.envs:CopterEnv',
    max_episode_steps=200
)
