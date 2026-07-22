from pokemon_benchmark.pilot_factory_runtime import make_agent


_policy = make_agent()


def agent(obs_dict, config=None):
    return _policy(obs_dict, config)
