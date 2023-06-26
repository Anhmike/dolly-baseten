import truss
import baseten

dolly_v2_truss = truss.load("path/to/dolly_v2_truss")

baseten.login("PASTE_API_KEY_HERE")

baseten.deploy(dolly_v2_truss, model_name="Dolly-v2", publish=True)


model = baseten.deployed_model_version_id('YOUR_MODEL_ID')

request = {
    "prompt": "Explain to me the difference between nuclear fission and fusion."
}

response = model.predict(request)
