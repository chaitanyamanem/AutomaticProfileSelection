prompt_template = {
    'NLP Research Engineer': """ Your task is to answer the questions based on the \
        candidate resume which is delimited with triple backticks.

        Anwer the questions with only 'Yes' or 'No'.

        return the reponses in json fromat, qestions text as keys and response as values.

        question) First extract number of years of working experince candidate have, and anwer if candidate \
        have 5 or more years of work experience as machine learning engineer, answer only `Yes` or `No`.
        Ans)

        question) Is candidate familiar with Python, Java, and R?
        Ans)

        question) Does candidate have communication and collaboration skills?
        Ans)

        question) Have experience in building machine learning systems?
        Ans)

        question) Does candidate have MSc or MS or M.Tech or Master's level education?
        Ans)

        question) Have knowledge of machine learning frameworks, like Keras, Tensorflow or PyTorch?
        Ans) 

        question) Does cnadidate possess extensive math and computer skills, with a deep understanding \
        of probability, statistics, and algorithms?
        Ans)

        question) Have experience in training, retraining, and monitoring machine learning systems and models as needed?
        Ans)

        question) Have experience in building machine leanrign pipelines?
        Ans)

        question) Have experience in deploying machine leanrign applications to production?
        Ans)

        question) Any experience with large language models (LLMs) or transfomers?
        Ans)

        question) Have experience with natural language processing (NLP)?
        Ans)

        Resume: ```{}```
    """,

     'NLP Research Scientist': """ Your task is to answer the questions based on the \
        candidate resume which is delimited with triple backticks.

        Anwer the questions with only 'Yes' or 'No'.

        return the reponses in json fromat, qestions text as keys and response as values.

        question) First extract number of years of working experince candidate have, and anwer if candidate \
        have 5 or more years of work experience as machine learning engineer, answer only `Yes` or `No`.
        Ans)

        question) Is candidate familiar with Python, Java, and R?
        Ans)

        question) Does candidate have communication and collaboration skills?
        Ans)

        question) Have experience in building machine learning systems?
        Ans)

        question) Does candidate have phD level education?
        Ans)

        question) Have knowledge of machine learning frameworks, like Keras, Tensorflow or PyTorch?
        Ans) 

        question) Does cnadidate possess extensive math and computer skills, with a deep understanding \
        of probability, statistics, and algorithms?
        Ans)

        question) Have experience in training, retraining, and monitoring machine learning systems and models as needed?
        Ans)

        question) Have experience in building machine leanrign pipelines?
        Ans)

        question) Have experience in deploying machine leanrign applications to production?
        Ans)

        question) Any experience with large language models (LLMs) or transfomers?
        Ans)

        question) Have experience with natural language processing (NLP)?
        Ans)

        question) Are there any research publications or scientific publications?
        Ans)

        Resume: ```{}```
    """,

     'Software Engineer C++': """ Your task is to answer the questions based on the \
        candidate resume which is delimited with triple backticks.

        Anwer the questions with only 'Yes' or 'No'.

        return the reponses in json fromat, qestions text as keys and response as values.

        question) First extract number of years of working experince candidate have, and anwer if candidate \
        have 5 or more years of work experience as software engineer, answer only `Yes` or `No`.
        Ans)

        question) Is candidate familiar with c++?
        Ans)

        question) Does candidate have communication and collaboration skills?
        Ans)

        question) Have experience in OOP (Object Oriented Programming)?
        Ans)

        question) Does candidate have Bachelor’s degree?
        Ans)

        question) Have knowledge of software version control tools like git?
        Ans) 

        question) Does cnadidate possess experience with Linux operating system?
        Ans)

        question) Does candidate have good data structures and algorithm knowledge?
        Ans)

        Resume: ```{}```
    """
}