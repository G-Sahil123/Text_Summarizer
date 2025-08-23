import os 
from TextSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from TextSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)


    
    def convert_examples_to_features(self,batch):
        dialogues = [str(x) for x in batch["dialogue"]]
        summaries = [str(x) for x in batch["summary"]]

        model_inputs = self.tokenizer(
            dialogues,
            max_length=1024,
            truncation=True,
            padding="max_length"
        )

        with self.tokenizer.as_target_tokenizer():
            labels = self.tokenizer(
                summaries,
                max_length=128,
                truncation=True,
                padding="max_length"
            )

        model_inputs["labels"] = labels["input_ids"]
        return model_inputs
    

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))