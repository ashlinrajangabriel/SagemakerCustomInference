from sagemaker.sklearn.model import SKLearnModel
# Variants
variant_a = {
    "VariantName": "variant-a",
    "InstanceType": "ml.m5.xlarge",
    "InitialInstanceCount": 1,
    "InitialVariantWeight": 1,
    "AutoScalingConfig": {
        "MinInstanceCount": 1,
        "MaxInstanceCount": 10
    }
}

variant_b = {
    "VariantName": "variant-b",
    "InstanceType": "ml.m5.2xlarge",
    "InitialInstanceCount": 1,
    "InitialVariantWeight": 1
}

# Deployment configuration
deployment_config = {
    "EndpointConfigName": "scikit-endpoint-config",
    "ProductionVariants": [variant_a, variant_b]
}

scikit_model = SKLearnModel(model_data='s3://my_bucket/pretrained_model/model.tar.gz',
                            role=role,
                            entry_point='inference.py',
                            framework_version='0.23.1',
                            py_version='py3',
                            container_registry_uri='<ECR_REGISTRY_URI>',
                            container_tag='<TAG>')

# Deploy the model with A/B testing and auto-scaling
scikit_model.deploy(initial_instance_count=1,
                    endpoint_type='variant',
                    deployment_config=deployment_config)

