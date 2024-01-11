from source.utility.utility import generate_global_timestamp
from source.entity.config_entity import TrainingPipelineConfig

if __name__ == '__main__':

    generate_timestamp = generate_global_timestamp()

    train_pipeline_config = TrainingPipelineConfig()
    print(train_pipeline_config.__dict__)