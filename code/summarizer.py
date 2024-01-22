from openai import OpenAI
import os

class Summarizer():
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.chaitanyamanem = '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'
        self.client = OpenAI(
            api_key=self.chaitanyamanem
            )        
    def getShortSummary(self, resume):
        prompt = f"""
        Your task is to give a short summary of the candidate based on the \
        resume which is delimited with triple backticks.

        Summary is to technical recruitor, so highlight the education, \
        number of years of work experience, technical skills, \
        Previous roles and companies and work experience.

        summary should be 2 to 3 lines
        Resume: ```{resume}```
        """
        response = self.__get_completion(prompt)
        return response
        
    def getConciseSummary(self, resume):
        prompt = f"""
        Your task is to extract relavent information from the \
        candidate resume to give it to the recruitor.

        Resume is given in the triple backtics.

        The recruitor is looking for educaiton, projects \
        and work experience.

        Summarize each section such that it should be short but should not miss the \
        technical skills and key words.

        Projects and work experience should not be more than 50 words.

        Reponse should follow the format of

        Education:
        ---------
        summary

        projects:
        --------
        summary

        Work Experience:
        ----------------
        summary


        If there are multiple projects or companies or qualifications, seperate them with new line. \
        If any of the section not there in the resume put the value blank.

        Resume: ```{resume}```
        """
        response = self.__get_completion(prompt)
        return response
    
    def getRubrics(self, prompt):        
        response = self.__get_completion(prompt)
        return response        
        
    def getScore(self, rubrics):
        
        n_questions = len(rubrics.keys())
        reponses = list(rubrics.values())
        positives = reponses.count('Yes')
        
        return positives / n_questions
    
    def __get_completion(self, prompt): 
        messages = [{"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0, # this is the degree of randomness of the model's output
        )
        
        return response.choices[0].message.content
    