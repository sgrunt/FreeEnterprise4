def apply(env):
    if env.options.flags.has('golbez_no_shadow'):
        env.add_file('scripts/golbez_no_shadow.f4c')
