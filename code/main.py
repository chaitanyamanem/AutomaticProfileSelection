from datamodule import csvDataSource
from emailparser import EmailParser
from summarizer import Summarizer
from pypdf import PdfReader
from abc import ABC, abstractmethod
from filereader import *
import json
import pandas as pd
from tqdm import tqdm
from template import prompt_template as ptemplate
        
class Application:
    def __init__(self, application_id, email_id, email_body, resume_path):
        
        self.application_data = {}
        self.application_data['application_id'] = application_id
        self.application_data['email_id'] = email_id
        self.application_data['email_body'] = email_body
        self.application_data['resume_path'] = resume_path  
        
    def setNamePosition(self, name, position):
        self.application_data['applicant_name'] = name
        self.application_data['position_applid'] = position        
        
    def setShortSummary(self, short_summary):
        self.application_data['short_summary'] = short_summary        
        
    def setConciseSummary(self, concise_summary):
        self.application_data['consise_summary'] = concise_summary        
    
    def setRubrics(self, rubrics):
        self.application_data['rubrics'] = rubrics        
        
    def setScore(self, score):
        self.application_data['score'] = score        
        
    def data(self):
        return pd.DataFrame(data = self.application_data, index=[self.application_data['application_id']])


def readFile(file_path):
    extension_to_class = {
        'pdf': PdfReader,
        'doc': DocReader
    }
    
    entension = file_path.split('.')[-1]
    resume_text = extension_to_class[entension]().getText(file_path)
    return resume_text


def extractData(row, mail_parser, summarizer):
    application_id, email_id, email_body, resume_path = row['id'], row['email_id'], row['email_body'], row['resume_path']
    resume = readFile(resume_path)
    
    application = Application(application_id, email_id, email_body, resume_path)    
    
    applicant_name, position_applied = mail_parser.parseEmail(row['email_body'])    
    short_summary = summarizer.getShortSummary(resume)   
    concise_summary = summarizer.getConciseSummary(resume)    
    rubrics = summarizer.getRubrics(ptemplate[position_applied.strip()].format(resume))
    rubrics_json = json.loads(rubrics)    
    score = summarizer.getScore(rubrics_json)
    
    application.setNamePosition(applicant_name, position_applied)
    application.setShortSummary(short_summary)
    application.setConciseSummary(concise_summary)
    application.setRubrics(rubrics)
    application.setScore(score)
    
    return application.data()

def saveData(applications_data_obj, applications_data):    
    applications_data_obj.write_data(applications_data)
    

    
def main(mails_data_obj, applications_data_obj, mail_parser, summarizer):
    data_df = mails_data_obj.get_data()
    for index, row in tqdm(data_df.iterrows()):
        print(f"Preparing data from email {row['id']}")
        applications_data = extractData(row, mail_parser, summarizer)        
        print(f"Data extracted for email {row['id']}")
        saveData(applications_data_obj, applications_data)
        print(f"Data saved for email {row['id']}")
    


if __name__ == "__main__":
    mails_data_obj = csvDataSource(read_file_path = "data/emails.csv")
    applications_data_obj = csvDataSource(write_file_path = "data/applications.csv")
    
    mail_parser = EmailParser()
    summarizer = Summarizer()
    
    main(mails_data_obj, applications_data_obj, mail_parser, summarizer)