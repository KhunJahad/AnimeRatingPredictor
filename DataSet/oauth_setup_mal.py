import secrets

def get_new_code_verifier():
	token = secrets.token_urlsafe(100)
	return token[:128]

code_verifier = get_new_code_verifier()
print(len(code_verifier))
print(code_verifier)

"""
the url for authenatication should be :

https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id=3904c08f1933c41b2d54c559a0b8e14f&code_challenge=whWQwwE4_fK66nA-7Gdcswq_0ilqFK9JPnjdyqSVO59mYcU6dSJa_83i6PWqvg9Y2m70mKEaeP9o7YszUM7Sr9A3TXxvKrf0bwC8_8rOy-vrENjPPsPD5R1DfypagJDr
"""