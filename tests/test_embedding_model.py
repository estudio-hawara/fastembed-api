from fastembed_api import EmbeddingModel
import numpy as np

model = EmbeddingModel()

def test_embedding_model():
    embeddings = model.embed(["Hola mundo"])

    assert len(embeddings[0]) == 768
    assert np.allclose(
        embeddings[0][0:6],
        [-0.008461863733828068, 0.048017505556344986, -0.005513841286301613, 0.02872159518301487, 0.06021670624613762, 0.01590537652373314]
    )
