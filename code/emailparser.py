from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
class EmailParser:
    def __init__(self):
        self.model_name = "deepset/roberta-base-squad2"
        self.pipeline = pipeline('question-answering', model=self.model_name, tokenizer=self.model_name)
        
    def parseEmail(self, email_body:str):
        ''' This method is to extract the apllicaiton detail from the mail.
        Expected inputs: 
            - email: strign type, email content
        Returns:
            - name of the applicant:str
            - position applied for: str        
        '''
        qa_input = [
            {'question': 'what is the name of the candidate?', 'context':email_body},
            {'question': 'what is the job position applied for?', 'context':email_body},        
               ]
        result = self.pipeline(qa_input)
        name, position = result[0]['answer'], result[1]['answer']
        return name, position