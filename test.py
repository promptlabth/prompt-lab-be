import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "prompt-lab-383408",
        "private_key_id": "e58c5bd2ad4a0bd82d79183a0ff6c0e782a21a63",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCapJa2TV458Bhs\naIXtnk4Kee7h6dQLJIjWpXNqWWCoPr9FDD1DsYJZG1gGovP92NnCJ/ZU497m6kTq\np2HmQEHgliusemWUpcZIrz0WziqQtE8RAHumUfQXPAuRNmQDfGgbqYPSDX6FcRTg\nIu5mIWPqN/2J5ZxNWZv/vCa217/JmxhnYAiJSSZk9kcnCaNLoRgNuIK43198ee/J\n674LurTb/awql3ZrbKitut3mdAIRQ0RY8pyU++HYMzPsvy2kO+Ck8Vd4R2xRK0ww\nDNZS0UlywXCgVhadD+M2l6xWluCMtsXi7T6UB1q2YdzcVd5cpMMXcK+GZ8YHPSc2\nXkomLR6VAgMBAAECgf9kaycpzLIyi8KlryGqXFKykz5njWNtd2RYLs7oNC3xdFOb\namNqSKm9rRxLY7ZiUW6EByYTHnf1q7DkHTrvSY3G54xogDcU1eaK6t7lCJohdZ9o\nUpKjYem9vwMZPI3mR+LY7xZVK9vMCEDnlEE6u2fQ7TV5n2NyRMpptDHpfVTQGtfi\n0qri74GOnP0dOif8Ll2xAOLMZvUJkkwvo54IOVLTqnAMTiqdrDuAWI0ykViZqa+z\nzmz7aOs0Bqgnjj0F1L27U+7b+WkqjuaIMqXFifFi82QfM/y/4MbQzAqpCfedOhCi\nJIBmT/EXe+p2PmNRcplMjDQWs3qwna94xzAw/vUCgYEAziekkHJ5P+r+C9ngXc8K\nB1ADpX5h5Rfz6Yn46GqaXPej58nlIVPCnV2ty5RAjWQ1s3MNOgZZPHeRqgvuxbL6\n41CViZmu+Z+htKEa1/mFokIpBiz86mt7xTGL3wTMSeIQAHS/S9GUvyZqEZDPXJ9k\nSf36Bi9ycoMksRGP3RdAVysCgYEAwAiDsQB4eKyIAC0ThAE9kuFvxt/Ghp9BKeVC\n/sLiH7cfInZuiX+/w4vg/cIRU33QVTsCJ1Z/KN6zD24XAXzX5wzT2cEcwxGAsH+w\nAxbKS8mCLBSRsI56FL0H/RZXl36AGzk1OGViK0GnfAifFYROdeV3R+3NJWAEOwzY\ns97BgT8CgYADsJf0cegTqcwUQDkQ1MTULq1yB9oOtKgL9Qk8d7P9l/0aB/YO66Xf\nFS8oJqYlIbcIWDXTZQux1l4IEiCa70IoUWfrx5FnLGFDj2KgnPm0VsTPNHzuYTAc\n7m8XdcmGRQKOT4ig/cZQyYo6eEIN4Vh1LpOMCstcm1ZLyQmvJlxjcwKBgQCUMH3f\nw6s0BIBXEnHy9job9NgbMmizToYs3HzcuGtjah8eqyIV/X1wW6teZ7qTIY35l7XL\nwZYTZffsOlqKjVrXNDDv43RcnE8g5Qhg+d9WqMRJW/4pr2lKQ628gtdJUxds6rLF\nOIePNfUXZFfPdPBPTqrD2SDsbLIXF4zLEWVmZQKBgFKJpdYYK7QcNWSSn/BioX41\nzyH5yaN6Nsel5xTNfUKfrQIuvSmxOOS7R8taIAnud48BNpJVPusgJONFPEemiu3n\np8uyMAfJzIkr4Hj3liLyGCk39HcJKZM1F+qTxLDauCw7MV+Z/vGjSRhiXWOhpHDl\nwl6M61QD1n/2w3FbN2cX\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-i24ml@prompt-lab-383408.iam.gserviceaccount.com",
        "client_id": "102158328230916731821",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-i24ml%40prompt-lab-383408.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }

)

default_app = firebase_admin.initialize_app(cred, name="prompt_lab")


t = auth.verify_id_token(
    id_token="eyJhbGciOiJSUzI1NiIsImtpZCI6IjFiYjI2MzY4YTNkMWExNDg1YmNhNTJiNGY4M2JkYjQ5YjY0ZWM2MmYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVGFuYWNob2QgU2FrdGhhbWphcm9lbiIsInBpY3R1cmUiOiJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS82MDk3Nzg2Nzg2OTcwNjA4L3BpY3R1cmUiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcHJvbXB0LWxhYi0zODM0MDgiLCJhdWQiOiJwcm9tcHQtbGFiLTM4MzQwOCIsImF1dGhfdGltZSI6MTY4NDA2MDAwMiwidXNlcl9pZCI6Ik9xSWxUdWs0Q29odXZ6Q1BxNE81Z2xGQWdMODMiLCJzdWIiOiJPcUlsVHVrNENvaHV2ekNQcTRPNWdsRkFnTDgzIiwiaWF0IjoxNjg0MDYwMDAyLCJleHAiOjE2ODQwNjM2MDIsImVtYWlsIjoicGV0LjE0MzM2QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJmYWNlYm9vay5jb20iOlsiNjA5Nzc4Njc4Njk3MDYwOCJdLCJlbWFpbCI6WyJwZXQuMTQzMzZAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZmFjZWJvb2suY29tIn19.MS70Aki_cv7WBFzYwqKb3rJG5rX0V94qrp7dUDsNe2y4WYxki2ewX9ICNjt786p0JqLFey2jfFoeT9BZPUxf3dClLuTqaiYXDe9DTzxGyFG7u80oJJ9qDotGzBqivmqHbBz4WUEkeJSY6vM6yNUOYfRjwj0ITmFzadpAT3nW3pVhUcBVt0mIcA53zEzvJe4h7xcvOOhQMA7ZxN0hAUk_SLHJe6rTxhxtceqfhTe_XbxtyFRZF0BulFW8PDCk5b_gbYT5V65h63nrxp9YkFEInAVlTrYQJ-Dqs4KeUsNXP-Nsp-HOi3wHitThyxVK4iuM7UiVCg9uFK09OdWS8e-pdA",
    app=default_app
    )
print(t)
