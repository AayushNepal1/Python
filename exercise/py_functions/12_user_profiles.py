def build_profile(first, last, **kwargs):
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs

user_profile = build_profile('aayush', 'nepal', age=19, year=2001, month=3, day=27, location='taudaha')
print(user_profile)