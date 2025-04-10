import datetime
import os
from time import sleep

import jwt

# 密钥，用于签名和验证 JWT
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret")


def generate_tokens(user_id):
    """
    生成 access_token 和 refresh_token
    :param user_id: 用户ID
    :return: access_token, refresh_token
    """
    # 设置 access_token 过期时间为 1 秒
    access_token_payload = {
        "user_id": user_id,
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=os.getenv("JWT_EXPIRATION_DAYS", 1)),
    }
    access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm="HS256")

    # 设置 refresh_token 过期时间为 20 天
    refresh_token_payload = {
        "user_id": user_id,
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=os.getenv("JWT_REFRESH_EXPIRATION_DAYS", 20)),
    }
    refresh_token = jwt.encode(refresh_token_payload, SECRET_KEY, algorithm="HS256")

    return access_token, refresh_token


def verify_token(token):
    """
    验证 token 是否有效
    :param token: JWT token
    :return: 解码后的 payload 或 None
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token 已过期")
        return None
    except jwt.InvalidTokenError:
        print("无效的 Token")
        return None


def refresh_access_token(refresh_token):
    """
    使用 refresh_token 刷新 access_token 和 refresh_token
    :param refresh_token: 刷新 token
    :return: 新的 access_token, 新的 refresh_token 或 None
    """
    payload = verify_token(refresh_token)
    if payload:
        user_id = payload["user_id"]
        # 生成新的 access_token
        access_token_payload = {
            "user_id": user_id,
            "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=os.getenv("JWT_EXPIRATION_DAYS", 1)),
        }
        new_access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm="HS256")

        # 生成新的 refresh_token
        refresh_token_payload = {
            "user_id": user_id,
            "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=os.getenv("JWT_REFRESH_EXPIRATION_DAYS", 20)),
        }
        new_refresh_token = jwt.encode(refresh_token_payload, SECRET_KEY, algorithm="HS256")

        return new_access_token, new_refresh_token
    return None, None


# 示例使用
if __name__ == "__main__":
    user_id = 123  # 假设用户ID为123
    access_token, refresh_token = generate_tokens(user_id)
    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")

    sleep(1)
    # 验证 access_token
    payload = verify_token(access_token)
    print(f"Access Token Payload: {payload}")

    # 刷新 access_token 和 refresh_token
    new_access_token, new_refresh_token = refresh_access_token(refresh_token)
    print(f"New Access Token: {new_access_token}")
    print(f"New Refresh Token: {new_refresh_token}")
