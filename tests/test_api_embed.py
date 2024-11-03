from fastapi.testclient import TestClient
import numpy as np
from fastembed_api.main import app

client = TestClient(app)

def test_api_health():
    response = client.post("/embed", json={
        "paragraph": "Hola mundo"
    })

    assert response.status_code == 200
    assert "embeddings" in response.json()
    assert np.allclose(
        response.json()["embeddings"][0:6],
        [-0.008461863733828068, 0.048017505556344986, -0.005513841286301613, 0.02872159518301487, 0.06021670624613762, 0.01590537652373314]
    )
