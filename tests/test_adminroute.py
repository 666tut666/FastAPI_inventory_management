import json
from fastapi import status


def test_create_user(client):
    data = {"email": "e@mail.com", "password": "test12"}
        # providing dummy data
    response = client.post("/admin", json.dumps(data))
        # gives above data in json format
        ##now we check the o/p using assert
    assert response.status_code == status.HTTP_200_OK
        # 200 ok aaucha thei ho
    assert response.json()["email"] == "e@mail.com"
        # email match check
    assert response.json()["is_active"] == True
        # is_active bool ho, thei check
    pass
