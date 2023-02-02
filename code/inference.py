import io
import json
import joblib
import numpy as np
import sagemaker_inference

class InferenceService(sagemaker_inference.Transformer):
    def __init__(self, model):
        self.model = model

    def default_input_fn(self, input_data, content_type):
        if content_type == 'application/json':
            return json.loads(input_data)
        raise ValueError("Unsupported content type: {}".format(content_type))

    def default_output_fn(self, predictions, accept):
        if accept == 'application/json':
            return json.dumps(predictions), accept
        raise ValueError("Unsupported accept type: {}".format(accept))

    def transform_fn(self, inputs, content_type):
        features = self.default_input_fn(inputs, content_type)
        predictions = self.model.predict(features)
        return self.default_output_fn(predictions, content_type)

def model_fn(model_dir):
    model = joblib.load(f"{model_dir}/model.joblib")
    return InferenceService(model)