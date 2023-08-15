import pandas as pd
import numpy as np
from tqdm.auto import tqdm
import tensorflow as tf
from transformers import BertTokenizer
from sklearn.preprocessing import StandardScaler
import enums


scaler = StandardScaler()
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

classes = ['Music', 'Photos', 'Books', 'Films']


class Pobert:
    
    def __init__(self) -> None:
        self.model = tf.keras.models.load_model('./content/pobert_fast2')
        self.model.load_weights('./content/pobert_fast2_weights/trained_ckpt')
        pass

    def predict(self, input_data):
        model_input = self.prepare_input(input_data)
        probs = self.model.predict(model_input)[0]
        return classes[np.argmax(probs)]

    def prepare_input(self, input_data):
        data = [input_data.get_args()]
        df = pd.DataFrame(data=data, columns=enums.data_args_columns)

        numeric_df = df.drop(columns=enums.data_not_numeric_args)
        text_df = df['group_activity'].astype(str) + df['group_description'].astype(str) \
                + df['group_status'].astype(str) + df['post_text'].astype(str)
        
        numeric_input = self.prepare_numeric_input(numeric_df)
        pobert_input = self.prepare_pobert_input(numeric_input, text_df[0], tokenizer)

        return pobert_input

    def prepare_numeric_input(self, numeric_df):
        return numeric_df.astype('int32')

    def prepare_pobert_input(self, numeric_input, text_input, tokenizer):
        token = tokenizer.encode_plus(
            text_input,
            max_length=512, 
            truncation=True,
            padding='max_length',
            add_special_tokens=True,
            return_tensors='tf'
        )
        return {
            'input_ids': token.input_ids,
            'attention_mask': token.attention_mask,
            'numeric_inputs': numeric_input
        }
    
    def merge_input(self, numeric_input, bert_input):
        bert_input['numeric_inputs'] = numeric_input
        return bert_input